@echo off
echo === Subiendo TFM Cobros PYMES a GitHub ===
echo.

REM Configurar Git (si no está configurado)
git config user.name "Fran115z"
git config user.email "fran115z@gmail.com"

echo [1/4] Haciendo commit de todos los archivos...
git add .
git commit -m "TFM Cobros PYMES - Sistema completo de IA para priorizacion de cobros"

echo [2/4] Creando rama main...
git branch -M main

echo [3/4] Subiendo a GitHub...
git push -u origin main

echo [4/4] Verificando...
echo.
echo ✅ ¡Proyecto subido exitosamente!
echo.
echo Verifica en: https://github.com/Fran115z/tfm-cobros-pymes
echo.
pause