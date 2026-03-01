# Configuración de Claude Desktop para TFM Cobros PYMES

## Pasos de instalación

1. **Instalar Claude Desktop**
   - Descargar desde https://claude.ai/desktop
   - Instalar y crear cuenta

2. **Configurar MCP (Model Context Protocol)**
   - Copiar el archivo `mcp-cobros.json` a la carpeta de configuración de Claude:
     - Windows: `%APPDATA%\Claude\`
     - macOS: `~/Library/Application Support/Claude/`
     - Linux: `~/.config/Claude/`

3. **Conceder permisos de carpeta**
   - Claude necesita acceso a las carpetas:
     - `C:\Users\frana\Documents\tfm_cobros_pymes\outputs`
     - `C:\Users\frana\Documents\tfm_cobros_pymes\plantillas`

4. **Verificar configuración**
   - Abrir Claude Desktop
   - Escribir: "¿Qué facturas tengo críticas hoy?"
   - Debería poder leer los archivos CSV de outputs

## Notas de seguridad
- Los datos permanecen localmente en tu máquina
- Claude solo accede a las carpetas especificadas en el MCP
- No se envían datos a servidores externos

## Solución de problemas
- Si Claude no puede leer los archivos, verificar los permisos de carpeta
- Asegurarse de que los archivos CSV estén en la carpeta outputs
- Reiniciar Claude Desktop después de cambiar la configuración