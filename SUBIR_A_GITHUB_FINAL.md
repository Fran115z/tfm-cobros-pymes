# Guía Final para Subir tu Proyecto TFM a GitHub

## PASO 1: Preparación
1. Abre PowerShell como administrador
2. Navega a la carpeta del proyecto:
   cd C:\Users\frana\Documents\tfm_cobros_pymes

## PASO 2: Configurar Git (solo si no está configurado)
git config --global user.name "Fran115z"
git config --global user.email "tu-email@ejemplo.com"

## PASO 3: Crear commit con todos los archivos
git add .
git commit -m "TFM Cobros PYMES - Sistema completo de IA para priorizacion de cobros"

## PASO 4: Subir a GitHub
# Opción A: Con contraseña (más simple)
git push -u origin main

# Si te pide usuario y contraseña:
# - Usuario: Fran115z
# - Contraseña: Tu token de GitHub (ver PASO 5)

## PASO 5: Crear Token de Acceso Personal (si no lo tienes)
1. Ve a GitHub.com → Settings → Developer settings → Personal access tokens
2. Click en "Generate new token"
3. Nombre: "TFM Cobros PYMES"
4. Selecciona: repo (todos los permisos)
5. Expiration: 90 días
6. Click "Generate token"
7. Copia el token (es como una contraseña larga)

## PASO 6: Verificar la subida
Ve a: https://github.com/Fran115z/tfm-cobros-pymes
Deberías ver todos los archivos subidos.

## 📁 Estructura que se subirá:
├── datos/
│   ├── clientes.csv
│   ├── facturas.csv
│   ├── historial_pagos.csv
│   └── .gitkeep
├── scripts/
│   ├── 01_generador_datos.ipynb
│   ├── 04_feature_engineering.py
│   ├── 04_modelo_score_cliente.py
│   ├── 05_exportar_scores.py
│   └── 06_generador_script_completo.py
├── modelos/
│   ├── modelo_score_cliente.joblib
│   └── modelo_score_config.json
├── outputs/
│   ├── scores_clientes_20260128.csv
│   └── scores_clientes_20260128_completo.csv
├── claude_config/
│   ├── mcp-cobros.json
│   ├── tutorial_config_claude.md
│   └── prompts_ejemplo.txt
├── documentos/
│   └── modelo_score_cliente.md
├── README.md
├── LICENSE
├── requirements.txt
├── RUN_semanal.bat
└── .gitignore

## 🎯 Listo para tu TFM!
Tu proyecto incluye:
- ✅ Modelo predictivo de riesgo
- ✅ Dashboard para Power BI
- ✅ Agente conversacional con Claude
- ✅ Documentación completa
- ✅ Scripts de ejecución

¡Todo está listo para tu entrega!