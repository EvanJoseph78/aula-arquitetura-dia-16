from flask import Flask, request, jsonify
from flask_cors import CORS  # Importando o CORS

app = Flask(__name__)

# Habilitando o CORS para a aplicação inteira
CORS(app)

# Lista para armazenar os dados dos clientes em memória (não persiste entre reinicializações)
clientes = [
    {"id": 1, "nome": "João Silva", "email": "joao@email.com", "idade": 30},
    {"id": 2, "nome": "Maria Oliveira", "email": "maria@email.com", "idade": 25}
]

# Rota para criar um novo cliente (Create)


@app.route('/clientes', methods=['POST'])
def criar_cliente():
    data = request.get_json()
    if not data or not data.get('nome') or not data.get('email') or not data.get('idade'):
        return jsonify({'error': 'Faltando informações obrigatórias'}), 400
    novo_id = max([cliente['id'] for cliente in clientes], default=0) + 1
    cliente = {"id": novo_id, "nome": data['nome'],
               "email": data['email'], "idade": data['idade']}
    clientes.append(cliente)
    return jsonify(cliente), 201

# Rota para obter todos os clientes (Read)


@app.route('/clientes', methods=['GET'])
def listar_clientes():
    return jsonify(clientes)

# Rota para obter um cliente específico (Read)


@app.route('/clientes/<int:id>', methods=['GET'])
def obter_cliente(id):
    cliente = next((c for c in clientes if c['id'] == id), None)
    if cliente is None:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    return jsonify(cliente)

# Rota para atualizar um cliente (Update)


@app.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    cliente = next((c for c in clientes if c['id'] == id), None)
    if cliente is None:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    data = request.get_json()
    cliente['nome'] = data.get('nome', cliente['nome'])
    cliente['email'] = data.get('email', cliente['email'])
    cliente['idade'] = data.get('idade', cliente['idade'])
    return jsonify(cliente)

# Rota para deletar um cliente (Delete)


@app.route('/clientes/<int:id>', methods=['DELETE'])
def deletar_cliente(id):
    global clientes
    cliente = next((c for c in clientes if c['id'] == id), None)
    if cliente is None:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    clientes = [c for c in clientes if c['id'] != id]
    return jsonify({'message': 'Cliente deletado com sucesso'}), 200


# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
