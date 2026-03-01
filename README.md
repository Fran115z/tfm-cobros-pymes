# TFM Cobros PYMES - Modelo de IA para Priorización de Cobros

## Descripción
Sistema de IA que ayuda a PYMES españolas a optimizar la gestión de cobros mediante un modelo predictivo que asigna scores de riesgo a clientes y prioriza facturas.

## Características principales
- Modelo predictivo de riesgo de impago
- Dashboard en Power BI para visualización
- Agente conversacional con Claude Desktop
- Sistema RAG para consultas en lenguaje natural
- Priorización automática de facturas críticas

## Instalación rápida
1. Clonar el repositorio
2. Instalar dependencias: `pip install -r requirements.txt`
3. Configurar Claude Desktop (ver claude_config/tutorial_config_claude.md)
4. Ejecutar el flujo semanal: `python scripts/RUN_semanal.bat`

## Estructura del proyecto
- `datos/`: CSV de entrada (clientes, facturas, historial)
- `scripts/`: Pipeline completo de modelado
- `modelos/`: Artefactos del modelo entrenado
- `outputs/`: Resultados del modelo (scores y CSV enriquecido)
- `claude_config/`: Configuración para Claude Desktop
- `documentos/`: Documentación técnica

## Uso típico
1. Subir CSV a carpeta `datos/`
2. Ejecutar pipeline: `python scripts/05_exportar_scores.py && python scripts/06_generador_script_completo.py`
3. Conectar Power BI al CSV en `outputs/`
4. Usar Claude Desktop para consultas naturales

## Impacto esperado
- Reducción del 50% en tiempo de análisis
- Aumento del 25% en cobros semana 1
- Mejora del 15% en recuperación de facturas vencidas

## Licencia
MIT License - Ver archivo LICENSE para detalles