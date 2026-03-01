# Guía para subir el proyecto TFM Cobros PYMES a GitHub

## Paso 1: Verificar el repositorio actual
Tu repositorio ya está configurado con:
- URL: https://github.com/Fran115z/tfm-cobros-pymes.git
- Rama: main
- Estado: listo para subir contenido

## Paso 2: Hacer commit de los cambios

Abre PowerShell o Terminal en la carpeta `C:\Users\frana\Documents\tfm_cobros_pymes` y ejecuta:

```bash
# Configurar usuario (solo la primera vez)
git config user.name "Fran115z"
git config user.email "tu-email@ejemplo.com"

# Hacer commit
git commit -m "TFM Cobros PYMES - Sistema completo de IA para priorización de cobros"

# Verificar que se hizo el commit
git log --oneline -5
```

## Paso 3: Subir a GitHub

```bash
# Empujar los cambios a GitHub
git push -u origin main
```

## Paso 4: Verificar la subida
Ve a https://github.com/Fran115z/tfm-cobros-pymes y deberías ver todo el contenido.

## Si hay errores de autenticación:

1. **Opción A - Token de acceso personal:**
   - Ve a GitHub → Settings → Developer settings → Personal access tokens
   - Crea un nuevo token con permisos de repo
   - Usa el token como contraseña cuando git lo pida

2. **Opción B - GitHub CLI:**
   ```bash
   # Instalar GitHub CLI si no lo tienes
   winget install GitHub.cli
   
   # Autenticar
   gh auth login
   
   # Hacer push
   gh repo push
   ```

## Estructura que se subirá
El repositorio contendrá:
- 📁 `datos/`: CSV de ejemplo
- 📁 `scripts/`: Código Python del pipeline
- 📁 `modelos/`: Modelo entrenado
- 📁 `outputs/`: Resultados del modelo
- 📁 `claude_config/`: Configuración para Claude Desktop
- 📁 `documentos/`: Documentación
- 📄 `README.md`, `LICENSE`, `requirements.txt`

## Notas importantes
- Los archivos CSV en `datos/` y `outputs/` están incluidos como ejemplo
- En producción, estos datos serían específicos de cada empresa
- El modelo en `modelos/` está entrenado con datos sintéticos

¡Listo! Tu proyecto TFM estará disponible en GitHub.