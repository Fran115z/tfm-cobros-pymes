# Estructura del Proyecto TFM Cobros PYMES

Este archivo describe la estructura completa del proyecto para subir a GitHub.

## Carpetas principales

```
tfm-cobros-pymes/
├── datos/
│   ├── clientes.csv
│   ├── facturas.csv
│   ├── historial_pagos.csv
│   └── .gitkeep
├── documentos/
│   ├── modelo_score_cliente.md
│   └── .gitkeep
├── modelos/
│   ├── modelo_score_cliente.joblib
│   ├── modelo_score_config.json
│   └── .gitkeep
├── outputs/
│   ├── scores_clientes_20260128.csv
│   ├── scores_clientes_20260128_completo.csv
│   └── .gitkeep
├── scripts/
│   ├── 01_generador_datos.ipynb
│   ├── 01_generador_datos.ipynb .ipynb
│   ├── 02_validador_calidad.ipynb
│   ├── 03_analisis_exploratorio_EDA.ipynb
│   ├── 04_feature_engineering.py
│   ├── 04_modelo_score_cliente.py
│   ├── 05_exportar_scores.py
│   ├── 06_generador_script_completo.ipynb
│   ├── 06_generador_script_completo.py
│   └── __pycache__/
├── claude_config/
│   ├── mcp-cobros.json
│   ├── tutorial_config_claude.md
│   └── prompts_ejemplo.txt
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── RUN_semanal.bat
├── RUN_semanal.sh
└── subir_a_github.bat
└── subir_a_github.sh
```

## Archivos clave

### Configuración y documentación
- `README.md`: Descripción general del proyecto
- `LICENSE`: Licencia MIT
- `requirements.txt`: Dependencias de Python
- `.gitignore`: Archivos a ignorar por Git

### Scripts principales
- `scripts/04_feature_engineering.py`: Preparación de datos sin leakage
- `scripts/04_modelo_score_cliente.py`: Entrenamiento del modelo
- `scripts/05_exportar_scores.py`: Exportación de scores
- `scripts/06_generador_script_completo.py`: Generación de CSV completo

### Configuración Claude
- `claude_config/mcp-cobros.json`: Configuración MCP para Claude Desktop
- `claude_config/tutorial_config_claude.md`: Guía de instalación
- `claude_config/prompts_ejemplo.txt`: Prompts útiles

### Ejecución
- `RUN_semanal.bat`: Ejecución semanal en Windows
- `RUN_semanal.sh`: Ejecución semanal en Unix/Linux/macOS

## Pasos para subir a GitHub

1. Crear repositorio en https://github.com/new
2. No inicializar con README (ya tenemos uno)
3. Ejecutar el script `subir_a_github.bat` (Windows) o `subir_a_github.sh` (Unix)
4. Seguir las instrucciones del script

## Notas importantes
- Los archivos CSV en `datos/` y `outputs/` están incluidos como ejemplo
- En producción, estos datos serían específicos de cada empresa
- El modelo en `modelos/` está entrenado con datos sintéticos