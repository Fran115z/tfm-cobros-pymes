#!/bin/bash

echo "=== TFM Cobros PYMES - Ejecucion Semanal ==="
echo ""

# Activar entorno virtual si existe
if [ -f "venv/bin/activate" ]; then
    echo "Activando entorno virtual..."
    source venv/bin/activate
fi

echo "[1/2] Exportando scores de clientes..."
python scripts/05_exportar_scores.py
if [ $? -ne 0 ]; then
    echo "ERROR: Fallo al exportar scores"
    exit 1
fi

echo ""
echo "[2/2] Generando CSV completo con facturas..."
python scripts/06_generador_script_completo.py
if [ $? -ne 0 ]; then
    echo "ERROR: Fallo al generar CSV completo"
    exit 1
fi

echo ""
echo "✅ Proceso completado exitosamente!"
echo "Los archivos actualizados están en la carpeta outputs/"
echo ""
echo "Puedes abrir Claude Desktop y empezar a consultar."