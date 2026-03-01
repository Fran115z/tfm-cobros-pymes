@echo off
echo === Script de subida a GitHub para TFM Cobros PYMES ===
echo.

# Verificar si git está instalado
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Git no está instalado. Por favor instala Git primero.
    pause
    exit /b 1
)

# Pedir información
echo.
echo Para subir tu proyecto a GitHub, necesitarás:
echo 1. Tener una cuenta de GitHub
echo 2. Crear un repositorio nuevo en https://github.com/new
echo 3. Tener Git instalado (ya lo tienes)
echo.

set /p REPO_NAME="¿Cuál será el nombre de tu repositorio? (ej: tfm-cobros-pymes): "
set /p USERNAME="¿Cuál es tu nombre de usuario de GitHub? "

echo.
echo === Pasos para subir tu proyecto ===
echo.
echo 1. Crea el repositorio en https://github.com/new
echo 2. No inicialices con README (lo haremos nosotros)
echo 3. Copia la URL del repositorio
echo.
echo Una vez creado, ejecuta estos comandos en PowerShell:
echo.
echo cd C:\Users\frana\Documents\tfm_cobros_pymes
echo git init
echo git add .
echo git commit -m "Initial commit: TFM Cobros PYMES"
echo git branch -M main
echo git remote add origin https://github.com/%USERNAME%/%REPO_NAME%.git
echo git push -u origin main
echo.
echo ✅ ¡Listo! Tu proyecto estará en GitHub
echo.
pause