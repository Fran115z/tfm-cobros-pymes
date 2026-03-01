"""
TFM Cobros PYMES - Feature Engineering para modelo de score por cliente.

Construye target (riesgo_alto) y features sin fuga de información.
NO se usan: tasa_pago_a_tiempo, avg_dias_retraso, facturas_pagadas.
"""

from pathlib import Path
import pandas as pd


def _base_path() -> Path:
    return Path(__file__).resolve().parent.parent


def load_data(base_path: Path | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Carga clientes.csv e historial_pagos.csv desde datos/."""
    base = base_path or _base_path()
    datos_dir = base / "datos"
    clientes = pd.read_csv(datos_dir / "clientes.csv")
    historial = pd.read_csv(datos_dir / "historial_pagos.csv")
    return clientes, historial


def build_target(
    historial: pd.DataFrame,
    criterion: str = "tasa",
    threshold: float = 0.6,
) -> pd.Series:
    """
    Construye variable objetivo binaria riesgo_alto (1 = mal pagador, 0 = buen pagador).

    criterion:
      - "tasa": riesgo_alto = 1 si tasa_pago_a_tiempo < threshold
      - "tercios": riesgo_alto = 1 si tasa en el tercio inferior (threshold ignorado)
    """
    if criterion == "tasa":
        y = (historial["tasa_pago_a_tiempo"] < threshold).astype(int)
    elif criterion == "tercios":
        q = historial["tasa_pago_a_tiempo"].quantile(1 / 3)
        y = (historial["tasa_pago_a_tiempo"] < q).astype(int)
    else:
        raise ValueError('criterion must be "tasa" or "tercios"')
    y.index = historial["cliente_id"]
    y.name = "riesgo_alto"
    return y


def build_feature_df(
    clientes: pd.DataFrame,
    historial: pd.DataFrame,
) -> pd.DataFrame:
    """
    Construye dataframe de features sin leakage.

    Incluye: sector, scoring_externo, provincia, facturas_totales,
    importe_promedio_historico, ticket_medio (importe_promedio / facturas_totales).
    Excluye: tasa_pago_a_tiempo, avg_dias_retraso, facturas_pagadas.
    """
    h = historial[["cliente_id", "facturas_totales", "importe_promedio_historico"]].copy()
    h["ticket_medio"] = h["importe_promedio_historico"] / h["facturas_totales"].clip(lower=1)
    c = clientes[["cliente_id", "sector", "scoring_externo", "provincia"]]
    df = c.merge(h, on="cliente_id", how="inner")
    return df


def prepare_ml_data(
    clientes: pd.DataFrame,
    historial: pd.DataFrame,
    target_criterion: str = "tasa",
    target_threshold: float = 0.6,
) -> tuple[pd.DataFrame, pd.Series, pd.DataFrame]:
    """
    Prepara dataset para ML: features + target, sin leakage.

    Returns:
        X_df: dataframe con columnas features (categóricas y numéricas).
        y: serie riesgo_alto indexada por cliente_id.
        meta: dataframe con cliente_id y columnas auxiliares para exportación.
    """
    X_df = build_feature_df(clientes, historial)
    y = build_target(historial, criterion=target_criterion, threshold=target_threshold)
    # Alinear por cliente_id
    meta = X_df[["cliente_id"]].copy()
    X_df = X_df.set_index("cliente_id")
    y = y.reindex(X_df.index).dropna()
    X_df = X_df.loc[y.index]
    meta = meta.set_index("cliente_id").loc[y.index].reset_index()
    return X_df, y, meta


# Nombres de columnas para referencia en pipeline
FEATURE_COLS_CAT = ["sector", "scoring_externo", "provincia"]
FEATURE_COLS_NUM = ["facturas_totales", "importe_promedio_historico", "ticket_medio"]
FEATURE_COLS = FEATURE_COLS_CAT + FEATURE_COLS_NUM
