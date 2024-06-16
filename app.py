from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ESP32_URL = 'http://10.10.0.2'  # Replace with the actual IP address of your ESP32

@app.route('/send_command', methods=['POST'])
def send_command():
    command = request.json.get('command')
    if command == 'rotate_servo':
        # Send a command to the ESP32
        response = requests.post(f'{ESP32_URL}/servo', json={'action': 'rotate'})
        if response.status_code == 200:
            return jsonify({'status': 'success', 'message': 'Servo rotated'}), 200
        else:
            return jsonify({'status': 'failure', 'message': 'Failed to rotate servo'}), 500
    return jsonify({'status': 'failure', 'message': 'Invalid command'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
