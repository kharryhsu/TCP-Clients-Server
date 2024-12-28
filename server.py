import socket
import argparse
import threading

num_clients = 0
client_lock = threading.Lock()

def handle_client(client_socket, client_address):
    global num_clients
    
    try:
        with client_lock:
            num_clients += 1
        
        print(f"Number of connected clients: {num_clients}\n")
        
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            
            if not data:
                print(f"Client {client_address} disconnected.")
                break
            
            print(f"Received from client {client_address}: {data}\n")
            
            msg = f"Hey, Client {client_address[0]}"
            
            if msg.lower() == 'exit':
                print(f"Ending connection with client {client_address}.")
                client_socket.send("Connection closed by server.".encode('utf-8'))
                break

            try:
                client_socket.send(msg.encode('utf-8'))
            except Exception as e:
                print(f"Error sending message to {client_address}: {e}")
                break
    except Exception as e:
        print(f'Error handling client {client_address}: {e}')
    finally:
        with client_lock:
            num_clients -= 1
        
        client_socket.close()
        
        print(f'Connection with {client_address} closed.')   
        print(f"Number of connected clients: {num_clients}\n")
        
        if num_clients < 1:
            print("Waiting for connection...\n")

def start_server(addr='localhost', port=12345):
    global num_clients
    
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((addr, port))
        server_socket.listen(5)
        
        print(f'Server is listening on port {addr}:{port}...')
        print("\nWaiting for connection...\n")
        
        while True:
            client_socket, client_address = server_socket.accept()
            
            print(f'Connection established with {client_address}')
            
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
    except Exception as e:
        print(f'Server error: {e}')
    finally:
        server_socket.close()
        print("Server shutdown.")
        
def parse_arguments():
    parser = argparse.ArgumentParser(description="TCP Client")
    parser.add_argument('--addr', type=str, default='localhost', help="Server address (default: localhost)")
    parser.add_argument('--port', type=int, default=12345, help="Server port (default: 12345)")
    
    return parser.parse_args()

def configure_with_input():
    addr = input("Enter server address (default 'localhost'): ") or 'localhost'
    port = input("Enter server port (default 12345): ")
    port = int(port) if port else 12345
    
    return addr, port

if __name__ == "__main__":
    args = parse_arguments()
    
    if args.addr == 'localhost' and args.port == 12345:
        addr, port = configure_with_input()
    else:
        addr, port = args.addr, args.port

    start_server(addr=addr, port=port)