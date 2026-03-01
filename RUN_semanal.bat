@echo off
echo === TFM Cobros PYMES - Ejecucion Semanal ===
echo.

REM Activar entorno virtual si existe
if exist "venv\Scripts\activate.bat" (
    echo Activando entorno virtual...
    call venv\Scripts\activate.bat
)

echo [1/2] Exportando scores de clientes...
python scripts\05_exportar_scores.py
if %errorlevel% neq 0 (
    echo ERROR: Fallo al exportar scores
    pause
    exit /b 1
)

echo.
echo [2/2] Generando CSV completo con facturas...
python scripts\06_generador_script_completo.py
if %errorlevel% neq 0 (
    echo ERROR: Fallo al generar CSV completo
    pause
    exit /b 1
)

echo.
echo ✅ Proceso completado exitosamente!
echo Los archivos actualizados están en la carpeta outputs/
echo.
echo Puedes abrir Claude Desktop y empezar a consultar.
echo.
pause