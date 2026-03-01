"""
TFM Cobros PYMES - Entrenamiento del modelo de score por cliente.

Entrena LogisticRegression y RandomForest, evalúa con AUC-ROC y validación
cruzada, guarda el mejor modelo y config en modelos/.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

_scripts_dir = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "feat_eng", _scripts_dir / "04_feature_engineering.py"
)
feat_eng = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(feat_eng)
FEATURE_COLS_CAT = feat_eng.FEATURE_COLS_CAT
FEATURE_COLS_NUM = feat_eng.FEATURE_COLS_NUM
load_data = feat_eng.load_data
prepare_ml_data = feat_eng.prepare_ml_data

BASE = Path(__file__).resolve().parent.parent
MODELOS_DIR = BASE / "modelos"
DATOS_DIR = BASE / "datos"


def _build_preprocessor():
    """ColumnTransformer: OneHotEncoder (cat) + StandardScaler (num)."""
    return ColumnTransformer(
        [
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore", drop="first", sparse_output=False),
                FEATURE_COLS_CAT,
            ),
            ("num", StandardScaler(), FEATURE_COLS_NUM),
        ],
        remainder="drop",
        verbose_feature_names_out=False,
    )


def _build_pipeline(clf):
    pre = _build_preprocessor()
    return Pipeline([("preprocessor", pre), ("classifier", clf)])


def main():
    target_criterion = "tasa"
    target_threshold = 0.6
    random_state = 42
    n_splits = 5

    clientes, historial = load_data(BASE)
    X_df, y, meta = prepare_ml_data(
        clientes,
        historial,
        target_criterion=target_criterion,
        target_threshold=target_threshold,
    )
    X = X_df.reset_index(drop=True)
    y = y.reset_index(drop=True)

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=random_state
    )

    candidates = [
        ("logistic", LogisticRegression(random_state=random_state, max_iter=1000)),
        ("forest", RandomForestClassifier(random_state=random_state, n_estimators=100)),
    ]
    best_name = None
    best_pipeline = None
    best_auc = -1.0
    results = []

    for name, clf in candidates:
        pipe = _build_pipeline(clf)
        scores = cross_val_score(pipe, X_train, y_train, cv=n_splits, scoring="roc_auc")
        mean_auc = float(scores.mean())
        std_auc = float(scores.std())
        results.append({"model": name, "mean_auc": mean_auc, "std_auc": std_auc})
        if mean_auc > best_auc:
            best_auc = mean_auc
            best_name = name
            best_pipeline = pipe

    best_pipeline.fit(X_train, y_train)
    y_pred = best_pipeline.predict(X_val)
    y_proba = best_pipeline.predict_proba(X_val)[:, 1]

    val_auc = roc_auc_score(y_val, y_proba)
    val_acc = accuracy_score(y_val, y_pred)
    val_prec = precision_score(y_val, y_pred, zero_division=0)
    val_rec = recall_score(y_val, y_pred, zero_division=0)
    val_f1 = f1_score(y_val, y_pred, zero_division=0)
    cm = confusion_matrix(y_val, y_pred)

    print("=" * 60)
    print("MODELO DE SCORE POR CLIENTE - ENTRENAMIENTO")
    print("=" * 60)
    print(f"Target: riesgo_alto (criterion={target_criterion}, threshold={target_threshold})")
    aucs = [f"{r['mean_auc']:.3f}" for r in results]
    print(f"CV AUC ({n_splits}-fold): {aucs}")
    print(f"Mejor modelo: {best_name} (mean AUC = {best_auc:.3f})")
    print(f"Validación - AUC: {val_auc:.3f} | Acc: {val_acc:.3f} | P: {val_prec:.3f} | R: {val_rec:.3f} | F1: {val_f1:.3f}")
    print("Matriz de confusión (val):")
    print(cm)
    print("=" * 60)

    MODELOS_DIR.mkdir(parents=True, exist_ok=True)
    pipeline_path = MODELOS_DIR / "modelo_score_cliente.joblib"
    config_path = MODELOS_DIR / "modelo_score_config.json"

    joblib.dump(best_pipeline, pipeline_path)
    config = {
        "target_criterion": target_criterion,
        "target_threshold": target_threshold,
        "best_model": best_name,
        "feature_cols_cat": FEATURE_COLS_CAT,
        "feature_cols_num": FEATURE_COLS_NUM,
        "risk_tier_thresholds": {"bajo": 0.6, "medio": 0.4},
        "val_metrics": {
            "auc": val_auc,
            "accuracy": val_acc,
            "precision": val_prec,
            "recall": val_rec,
            "f1": val_f1,
        },
    }
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    print(f"Modelo guardado: {pipeline_path}")
    print(f"Config guardado: {config_path}")


if __name__ == "__main__":
    main()
