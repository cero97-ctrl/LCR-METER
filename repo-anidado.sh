#!/usr/bin/env bash
set -euo pipefail

# Obtener el directorio donde se encuentra el script para evitar rutas absolutas
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "$SCRIPT_DIR"

# Verificar si se proporcionó un argumento
if [ $# -eq 0 ]; then
    echo "Uso: $0 <carpeta-del-repositorio-anidado>"
    exit 1
fi

TARGET_DIR="${1%/}" # Eliminar barra final si existe

# Validación básica de seguridad
if [[ "$TARGET_DIR" == "." || "$TARGET_DIR" == ".." || "$TARGET_DIR" == "/" ]]; then
    echo "Error: Directorio objetivo inválido."
    exit 1
fi

# 1. Eliminar la carpeta .git oculta dentro del directorio objetivo
# Esto elimina la historia del repositorio original, convirtiéndolo en una carpeta normal
if [ -d "$TARGET_DIR/.git" ]; then
    rm -rf "$TARGET_DIR/.git"
fi

# 2. Eliminar la referencia de "submódulo" que Git guardó en la memoria caché
# Nota: Si este comando da error diciendo que no es un directorio, intenta sin la opción -r
git rm --cached "$TARGET_DIR" || true

# 3. Agregar la carpeta nuevamente (ahora Git verá los archivos dentro)
git add "$TARGET_DIR"

# 4. Confirmar y subir los cambios si existen
if ! git diff --cached --quiet; then
    git commit -m "Arreglar: Integrar repositorio anidado '$TARGET_DIR' como carpeta normal"
    git push
fi
