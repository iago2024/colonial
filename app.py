import os
from flask import Flask, render_template

app = Flask(__name__)

# Esta é a única rota que precisamos
@app.route("/")
def home():
    """Renderiza a página inicial do site."""
    
    # --- LÓGICA DA GALERIA DINÂMICA ---
    # 1. Define o caminho para a pasta da galeria
    gallery_path = os.path.join(app.static_folder, 'images', 'gallery')
    
    gallery_images = []
    
    # 2. Verifica se a pasta existe
    if os.path.exists(gallery_path):
        # 3. Lista todos os arquivos na pasta
        valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')
        for filename in os.listdir(gallery_path):
            # 4. Adiciona apenas se for uma imagem válida
            if filename.lower().endswith(valid_extensions):
                gallery_images.append(filename)
                
    # 5. Passa a lista de nomes de arquivos para o template
    return render_template('index.html', gallery_images=gallery_images)

if __name__ == '__main__':
    print("🚀 Servidor do site moderno rodando em http://127.0.0.1:5000")
    print(f"   Carregando galeria da pasta: static/images/gallery/")
    app.run(host="0.0.0.0", port=5000, debug=True)
