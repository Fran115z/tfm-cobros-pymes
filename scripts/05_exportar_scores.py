"""
TFM Cobros PYMES - Exportación de scores por cliente.

Carga modelo y config desde modelos/, genera score_pago y riesgo por cliente,
exporta CSV a outputs/scores_clientes_YYYYMMDD.csv para Power BI y agente.
"""

from __future__ import annotations

import importlib.util
import json
from datetime import datetime
from pathlib import Path

import joblib
import pandas as pd

_scripts_dir = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "feat_eng", _scripts_dir / "04_feature_engineering.py"
)
feat_eng = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(feat_eng)
load_data = feat_eng.load_data
build_feature_df = feat_eng.build_feature_df

BASE = Path(__file__).resolve().parent.parent
MODELOS_DIR = BASE / "modelos"
OUTPUTS_DIR = BASE / "outputs"


def _risk_tier(score_pago: float, thresholds: dict) -> str:
    """Asigna Alto / Medio / Bajo según umbrales (bajo >= 0.6, medio >= 0.4)."""
    if score_pago >= thresholds.get("bajo", 0.6):
        return "Bajo"
    if score_pago >= thresholds.get("medio", 0.4):
        return "Medio"
    return "Alto"


def main() -> None:
    pipeline_path = MODELOS_DIR / "modelo_score_cliente.joblib"
    config_path = MODELOS_DIR / "modelo_score_config.json"
    if not pipeline_path.exists() or not config_path.exists():
        raise FileNotFoundError(
            "Ejecuta antes 04_modelo_score_cliente.py para entrenar y guardar el modelo."
        )

    pipeline = joblib.load(pipeline_path)
    with open(config_path, encoding="utf-8") as f:
        config = json.load(f)
    thresholds = config.get("risk_tier_thresholds", {"bajo": 0.6, "medio": 0.4})

    clientes, historial = load_data(BASE)
    X_df = build_feature_df(clientes, historial)
    meta = X_df[["cliente_id"]].copy()
    X = X_df.drop(columns=["cliente_id"])

    proba_riesgo = pipeline.predict_proba(X)[:, 1]
    score_pago = 1.0 - proba_riesgo
    riesgo = pd.Series([_risk_tier(s, thresholds) for s in score_pago], index=X.index)

    out = pd.DataFrame({
        "cliente_id": meta["cliente_id"].values,
        "score_pago": score_pago,
        "riesgo": riesgo.values,
    })
    out = out.sort_values("score_pago", ascending=False).reset_index(drop=True)

    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y%m%d")
    out_path = OUTPUTS_DIR / f"scores_clientes_{today}.csv"
    out.to_csv(out_path, index=False, encoding="utf-8-sig")

    print("=" * 60)
    print("EXPORTACIÓN DE SCORES POR CLIENTE")
    print("=" * 60)
    print(f"Modelo: {config.get('best_model', '?')}")
    print(f"Clientes: {len(out)}")
    print(f"Riesgo Alto: {(out['riesgo'] == 'Alto').sum()} | Medio: {(out['riesgo'] == 'Medio').sum()} | Bajo: {(out['riesgo'] == 'Bajo').sum()}")
    print(f"Guardado: {out_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
