from flask import Flask, jsonify
import requests

app = Flask(__name__)

# URL da API externa
API_URL = "http://localhost:5000/clientes/"


@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # Fazendo uma solicitação GET para a API externa
        response = requests.get(API_URL)

        # Verificando o status da resposta
        if response.status_code == 200:
            data = response.json()  # Convertendo para JSON
            print("Dados recebidos da API:")
            for item in data[:5]:  # Exibir os 5 primeiros registros
                print(f"ID: {item['id']}, Título: {item['title']}")

            return jsonify({"message": "Dados exibidos no terminal com sucesso."}), 200
        else:
            print(f"Erro ao acessar API. Status: {response.status_code}")
            return jsonify({"error": f"Erro ao acessar API. Status: {response.status_code}"}), 500
    except Exception as e:
        print(f"Erro: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=5001)
