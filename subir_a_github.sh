#!/bin/bash
# Script para subir el proyecto TFM Cobros PYMES a GitHub

echo "=== Script de subida a GitHub para TFM Cobros PYMES ==="
echo ""

# Verificar si git está instalado
if ! command -v git &> /dev/null; then
    echo "❌ Git no está instalado. Por favor instala Git primero."
    exit 1
fi

# Pedir nombre del repositorio
read -p "¿Cuál es el nombre de tu repositorio de GitHub? (ej: tfm-cobros-pymes): " REPO_NAME
read -p "¿Cuál es tu nombre de usuario de GitHub? " USERNAME

# Crear repositorio en GitHub (requiere autenticación)
echo ""
echo "Para crear el repositorio en GitHub, necesitas tener el CLI de GitHub instalado"
echo "o crearlo manualmente en https://github.com/new"
echo ""
echo "Una vez creado el repositorio, ejecuta estos comandos:"
echo ""
echo "cd C:\Users\frana\Documents\tfm_cobros_pymes"
echo "git init"
echo "git add ."
echo "git commit -m 'Initial commit: TFM Cobros PYMES'"
echo "git branch -M main"
echo "git remote add origin https://github.com/$USERNAME/$REPO_NAME.git"
echo "git push -u origin main"
echo ""
echo "✅ ¡Listo! Tu proyecto estará en GitHub"