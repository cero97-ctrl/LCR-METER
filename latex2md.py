#!/usr/bin/env python3
import sys
import re
import os

def convert_tex_to_md(tex_file):
    if not os.path.exists(tex_file):
        print(f"Error: El archivo '{tex_file}' no existe.")
        sys.exit(1)

    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- 1. Limpieza de estructura LaTeX ---
    
    # Eliminar comentarios (todo lo que sigue a % si no está escapado)
    content = re.sub(r'(?<!\\)%.*', '', content)

    # Extraer solo el contenido dentro de document (si existe)
    if "\\begin{document}" in content:
        content = content.split("\\begin{document}")[1]
    if "\\end{document}" in content:
        content = content.split("\\end{document}")[0]

    # Eliminar comandos de metadatos comunes en el cuerpo
    content = re.sub(r'\\maketitle', '', content)

    # --- 2. Encabezados ---
    content = re.sub(r'\\section\*?\{(.*?)\}', r'# \1', content)
    content = re.sub(r'\\subsection\*?\{(.*?)\}', r'## \1', content)
    content = re.sub(r'\\subsubsection\*?\{(.*?)\}', r'### \1', content)

    # --- 3. Formato de texto ---
    content = re.sub(r'\\textbf\{(.*?)\}', r'**\1**', content)
    content = re.sub(r'\\textit\{(.*?)\}', r'*\1*', content)
    content = re.sub(r'\\texttt\{(.*?)\}', r'`\1`', content)
    content = re.sub(r'\\emph\{(.*?)\}', r'*\1*', content)
    
    # Enlaces básicos
    content = re.sub(r'\\href\{(.*?)\}\{(.*?)\}', r'\2', content)
    content = re.sub(r'\\url\{(.*?)\}', r'<\1>', content)

    # --- 4. Listas ---
    # Eliminar entornos de lista, dejar items
    content = re.sub(r'\\begin\{itemize\}', '', content)
    content = re.sub(r'\\end\{itemize\}', '', content)
    content = re.sub(r'\\begin\{enumerate\}', '', content)
    content = re.sub(r'\\end\{enumerate\}', '', content)
    
    # Reemplazar items por guiones
    content = re.sub(r'\\item\s+', '- ', content)

    # --- 5. Tablas (Conversión simplificada) ---
    # Eliminar entornos de tabla y tabular
    content = re.sub(r'\\begin\{table\}(\[.*?\])?', '', content)
    content = re.sub(r'\\end\{table\}', '', content)
    content = re.sub(r'\\begin\{tabular\}\{.*?\}', '', content)
    content = re.sub(r'\\end\{tabular\}', '', content)
    
    # Eliminar comandos de formato de tabla
    content = re.sub(r'\\centering', '', content)
    content = re.sub(r'\\toprule', '', content)
    content = re.sub(r'\\midrule', '', content)
    content = re.sub(r'\\bottomrule', '', content)
    content = re.sub(r'\\caption\{.*?\}', '', content)
    content = re.sub(r'\\label\{.*?\}', '', content)

    # Convertir celdas (& -> |) y filas (\\ -> salto de línea)
    content = re.sub(r'(?<!\\)&', ' | ', content)
    content = re.sub(r'\\\\', '  \n', content)

    # --- 6. Limpieza final ---
    # Reducir múltiples líneas en blanco
    content = re.sub(r'\n\s*\n', '\n\n', content)
    
    # Guardar resultado
    base_name = os.path.splitext(tex_file)[0]
    md_file = f"{base_name}.md"
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"¡Éxito! Archivo convertido: {md_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 latex2md.py <archivo.tex>")
        sys.exit(1)
    
    convert_tex_to_md(sys.argv[1])