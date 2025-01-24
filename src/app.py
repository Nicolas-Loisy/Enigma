from flask import Flask, request, jsonify
from enigma.enigma import Enigma

app = Flask(__name__)

def process_message(data, encode=True):
    initial_positions = data.get('initial_positions', [1, 1, 1])
    board_connections = data.get('board_connections', ["AY", "CD", "EF"])
    message = data.get('message', '') if encode else data.get('encoded_message', '')

    enigma = Enigma(initial_positions, board_connections)
    return enigma.run(message)

@app.route('/encode', methods=['POST'])
def encode():
    data = request.get_json()
    encoded_message = process_message(data, encode=True)
    return jsonify({'encoded_message': encoded_message})

@app.route('/decode', methods=['POST'])
def decode():
    data = request.get_json()
    decoded_message = process_message(data, encode=False)
    return jsonify({'decoded_message': decoded_message})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)