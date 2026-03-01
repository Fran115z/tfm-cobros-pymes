# 🚀 GUÍA FINAL - Subir tu Proyecto TFM a GitHub

## 📋 RESUMEN DE LO QUE TIENES:
✅ Repositorio GitHub: https://github.com/Fran115z/tfm-cobros-pymes
✅ Proyecto completo en: C:\Users\frana\Documents\tfm_cobros_pymes
✅ Git inicializado y configurado
✅ Todos los archivos preparados

## 🎯 PASOS PARA SUBIR TODO:

### PASO 1: Abrir PowerShell
1. Presiona `Windows + X`
2. Selecciona "Windows PowerShell (Administrador)"
3. Navega a tu proyecto:
   ```powershell
   cd C:\Users\frana\Documents\tfm_cobros_pymes
   ```

### PASO 2: Configurar Git (si no está configurado)
```powershell
git config --global user.name "Fran115z"
git config --global user.email "tu-email@ejemplo.com"
```

### PASO 3: Hacer commit de todos los archivos
```powershell
git add .
git commit -m "TFM Cobros PYMES - Sistema completo de IA para priorizacion de cobros"
```

### PASO 4: Subir a GitHub
```powershell
git push -u origin main
```

### PASO 5: Si te pide autenticación:
**Opción A - Token de Acceso Personal (Recomendado):**
1. Ve a GitHub → Settings → Developer settings → Personal access tokens
2. Crea un nuevo token con permisos de repo
3. Cuando git te pida contraseña, usa el token

**Opción B - HTTPS con contraseña:**
- Usuario: Fran115z
- Contraseña: Tu contraseña de GitHub

## 📁 ESTRUCTURA COMPLETA DEL PROYECTO:
```
tfm-cobros-pymes/
├── 📁 datos/
│   ├── clientes.csv (100 clientes de ejemplo)
│   ├── facturas.csv (500 facturas de ejemplo)
│   ├── historial_pagos.csv (historial de pagos)
│   └── .gitkeep
├── 📁 scripts/
│   ├── 01_generador_datos.ipynb (generador sintético)
│   ├── 04_feature_engineering.py (features sin leakage)
│   ├── 04_modelo_score_cliente.py (entrenamiento)
│   ├── 05_exportar_scores.py (exportar scores)
│   └── 06_generador_script_completo.py (CSV enriquecido)
├── 📁 modelos/
│   ├── modelo_score_cliente.joblib (modelo entrenado)
│   ├── modelo_score_config.json (configuración)
│   └── .gitkeep
├── 📁 outputs/
│   ├── scores_clientes_20260128.csv (scores por cliente)
│   ├── scores_clientes_20260128_completo.csv (CSV completo para BI)
│   └── .gitkeep
├── 📁 claude_config/
│   ├── mcp-cobros.json (config MCP)
│   ├── tutorial_config_claude.md (guía instalación)
│   └── prompts_ejemplo.txt (20 prompts útiles)
├── 📁 documentos/
│   └── modelo_score_cliente.md (documentación técnica)
├── 📄 README.md (descripción del proyecto)
├── 📄 LICENSE (licencia MIT)
├── 📄 requirements.txt (dependencias Python)
├── 📄 RUN_semanal.bat (ejecución Windows)
├── 📄 RUN_semanal.sh (ejecución Unix/Linux)
└── 📄 .gitignore (archivos a ignorar)
```

## 🎉 LISTO PARA TU TFM!
Tu proyecto incluye:
- ✅ Modelo predictivo de riesgo de impago
- ✅ Dashboard para Power BI con todas las columnas necesarias
- ✅ Agente conversacional con Claude Desktop
- ✅ 20 prompts de ejemplo para consultas
- ✅ Documentación completa
- ✅ Scripts de ejecución automática

## 🔍 VERIFICACIÓN FINAL:
Después de subir, ve a: https://github.com/Fran115z/tfm-cobros-pymes
Deberías ver todos los archivos listados arriba.

## 📞 SI TIENES PROBLEMAS:
1. Verifica que estás en la carpeta correcta
2. Asegúrate de tener Git instalado: `git --version`
3. Si el push falla, prueba: `git push --force origin main`
4. Para errores de autenticación, usa un token personal

¡Tu proyecto TFM está listo para ser entregado! 🚀