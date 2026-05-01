#!/usr/bin/env python3
import base64
import sys
import os

def main():
    if len(sys.argv) < 3:
        print("Uso: python3 add_banner.py <ruta_de_imagen> <nombre_de_clase_css>")
        print("Ejemplo: python3 add_banner.py images/ejemplo.jpg banner-amenazas")
        sys.exit(1)
    
    image_path = sys.argv[1]
    class_name = sys.argv[2]
    
    if not os.path.exists(image_path):
        print(f"Error: No se encontro la imagen '{image_path}'.")
        sys.exit(1)
        
    ext = os.path.splitext(image_path)[1].lower().replace('.', '')
    if ext == 'jpg':
        ext = 'jpeg'
        
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    except Exception as e:
        print(f"Error al leer la imagen: {e}")
        sys.exit(1)
        
    css_content = f"""
/* --- Banner Autogenerado: {class_name} --- */
.{class_name} {{
  background-image: url('data:image/{ext};base64,{encoded_string}') !important;
  background-size: cover !important;
  background-repeat: no-repeat !important;
  background-position: center center !important;
  color: white !important;
  position: relative !important;
  z-index: 1 !important;
  margin-top: 2rem !important;
  border-radius: 12px !important;
  padding: 1.5rem !important;
  overflow: hidden !important;
}}
.{class_name}::before {{
  content: "" !important;
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  background-color: rgba(0, 0, 0, 0.4) !important;
  z-index: -1 !important;
  border-radius: 12px !important;
}}
"""
    
    css_file_path = "_static/custom.css"
    if not os.path.exists(css_file_path):
        css_file_path = "../_static/custom.css"
        
    try:
        with open(css_file_path, "r") as f:
            original_css = f.read()
            
        with open(css_file_path, "w") as f:
            f.write(css_content + "\n" + original_css)
            
        print(f"¡Exito! La clase CSS '.{class_name}' ha sido agregada a {css_file_path}")
        print(f"Ahora puedes usarla en MyST Markdown de esta manera:")
        print(f"::::{{div}} {class_name}")
        print(f"# Tu Titulo Aqui")
        print(f"Texto sobre el banner oscuro")
        print(f"::::")
    except Exception as e:
        print(f"Error al actualizar el archivo CSS: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
