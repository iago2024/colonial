from flask import Flask, render_template

app = Flask(__name__)

# A ROTA "/pousada" FOI REMOVIDA
# Esta é a única rota que precisamos agora
@app.route("/")
def home():
    """Renderiza a página inicial do site."""
    return render_template('index.html')

if __name__ == '__main__':
    print("🚀 Servidor do site moderno rodando em http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)