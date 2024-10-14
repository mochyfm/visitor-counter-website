from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)
load_dotenv()

host = os.getenv("HOST", "127.0.0.1") # It does not work with "localhost" hostname, since it needs the ip address   
port = int(os.getenv("PORT", 5000))

print(f"Server running on {host}:{port}")

socketio = SocketIO(app, cors_allowed_origins="*")

COUNTER_FILE = os.path.join(os.path.dirname(__file__), 'visitors.txt')
IP_FILE = os.path.join(os.path.dirname(__file__), 'visitor_ips.txt')

def read_counter():
    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, 'w') as visitorsFile:
            visitorsFile.write('0')
    with open(COUNTER_FILE, 'r') as visitorsFile:
        count = int(visitorsFile.read())
    return count

def write_counter(count):
    with open(COUNTER_FILE, 'w') as visitorsFile:
        visitorsFile.write(str(count))

def read_ips():
    """Lee las direcciones IP del archivo y devuelve un conjunto de IPs únicas."""
    if not os.path.exists(IP_FILE):
        return set()
    
    with open(IP_FILE, 'r') as ip_file:
        return set(line.strip() for line in ip_file.readlines())

def write_ip(ip):
    """Escribe una nueva dirección IP en el archivo."""
    try:
        with open(IP_FILE, 'a') as ip_file:
            ip_file.write(ip + '\n')
        print(f"IP {ip} guardada exitosamente.")
    except Exception as e:
        print(f"Error al guardar la IP {ip}: {e}")

@app.route('/api/visits', methods=['GET'])
def get_visits():
    count = read_counter()
    count += 1
    write_counter(count)
    socketio.emit('update_visits', {'visits': count})
    return jsonify({'visits': count})

@socketio.on('newVisitor')
def handle_new_visitor():
    client_ip = request.remote_addr
    
    print(f"Nuevo visitante desde la IP: {client_ip}")
    
    existing_ips = read_ips()
    count = read_counter()  

    if client_ip not in existing_ips:
        write_ip(client_ip) 
        count += 1 
        write_counter(count)

    socketio.emit('update_visits', {'visits': count}) 

@socketio.on('disconnect')
def handle_disconnect():
    print('Client Disconnected')

if __name__ == '__main__':
    socketio.run(app, host=host, port=port)
    