from pathlib import Path
import re
import pandas as pd


def _base_path() -> Path:
    return Path(__file__).resolve().parent.parent


def _load_scores(scores_path: Path) -> pd.DataFrame:
    df = pd.read_csv(scores_path, encoding="utf-8-sig")
    df["score_pago"] = pd.to_numeric(df["score_pago"], errors="coerce")
    return df


def _load_clientes(datos_dir: Path) -> pd.DataFrame:
    df = pd.read_csv(datos_dir / "clientes.csv")
    df = df.rename(columns={"nombre": "nombre_cliente"})
    return df[["cliente_id", "nombre_cliente", "sector", "provincia", "scoring_externo"]]


def _load_historial(datos_dir: Path) -> pd.DataFrame:
    df = pd.read_csv(datos_dir / "historial_pagos.csv")
    df = df.rename(columns={"tasa_pago_a_tiempo": "tasa_pago_historica"})
    return df[["cliente_id", "tasa_pago_historica"]]


def _load_facturas(datos_dir: Path) -> pd.DataFrame:
    df = pd.read_csv(datos_dir / "facturas.csv")
    return df[
        [
            "factura_id",
            "cliente_id",
            "importe",
            "fecha_emision",
            "vencimiento",
            "dias_retraso",
            "estado",
        ]
    ]


def _compute_deuda_ponderada(importe: pd.Series, score: pd.Series) -> pd.Series:
    max_score = pd.to_numeric(score, errors="coerce").max()
    if pd.isna(max_score):
        return pd.Series([pd.NA] * len(score), index=score.index)
    if max_score > 1:
        return importe * (score / 100.0)
    return importe * score


def generar_csv_completo(scores_filename: str | None = None) -> Path:
    base = _base_path()
    outputs_dir = base / "outputs"
    datos_dir = base / "datos"
    if scores_filename:
        scores_path = outputs_dir / scores_filename
    else:
        candidates = sorted(outputs_dir.glob("scores_clientes_*.csv"))
        if not candidates:
            raise FileNotFoundError("No se encontró ningún scores_clientes_*.csv en outputs/")
        scores_path = candidates[-1]
    df_scores = _load_scores(scores_path)
    df_clientes = _load_clientes(datos_dir)
    df_historial = _load_historial(datos_dir)
    df_facturas = _load_facturas(datos_dir)
    df = df_facturas.merge(df_clientes, on="cliente_id", how="left")
    df = df.merge(df_scores, on="cliente_id", how="left")
    df = df.merge(df_historial, on="cliente_id", how="left")
    df["deuda_ponderada"] = _compute_deuda_ponderada(df["importe"], df["score_pago"])
    df["prioridad"] = (
        df["dias_retraso"].rank(method="first", ascending=False).astype(int)
    )
    cols = [
        "factura_id",
        "cliente_id",
        "nombre_cliente",
        "sector",
        "provincia",
        "importe",
        "dias_retraso",
        "estado",
        "score_pago",
        "riesgo",
        "fecha_emision",
        "vencimiento",
        "scoring_externo",
        "tasa_pago_historica",
        "prioridad",
        "deuda_ponderada",
    ]
    df = df[cols]
    m = re.search(r"(\d{8})", scores_path.name)
    date_str = m.group(1) if m else ""
    out_path = outputs_dir / f"scores_clientes_{date_str}_completo.csv"
    df.to_csv(out_path, index=False, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    p = generar_csv_completo("scores_clientes_20260128.csv")
    print(str(p))
