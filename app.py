from flask import Flask, request, jsonify

app = Flask(__name__)
usuarios = []

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios', methods=['POST'])
def adicionar_usuario():
    data = request.get_json()
    if not data.get('nome') or not data.get('email'):
        return jsonify({'erro': 'Nome e email são obrigatórios!'}), 400
    usuarios.append(data)
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)
