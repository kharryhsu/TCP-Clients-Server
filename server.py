import socket
import argparse

def start_server(addr='localhost', port=12345):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((addr, port))
        server_socket.listen(5)
        
        print(f'Server is listening on port {addr}:{port}...')
        
        while True:
            client_socket, client_address = server_socket.accept()
            
            print(f'Connection established with {client_address}')
            try:
                while True:
                    data = client_socket.recv(1024).decode('utf-8')
                    
                    if not data:
                        print(f"Client {client_address} disconnected.")
                        break
                    
                    print(f"Received from client: {data}")
                    
                    msg = input("Server: Enter message to send (or type 'exit' to end connection)\n> ")
                    
                    if msg.lower() == 'exit':
                            print("Ending connection with client.")
                            client_socket.send("Connection closed by server.".encode('utf-8'))
                            break

                    try:
                        client_socket.send(msg.encode('utf-8'))
                    except Exception as e:
                        print(f"Error sending message: {e}")
                        break
            except Exception as e:
                print(f'Error handling client {client_address}: {e}')
            finally:
                client_socket.close()
                print(f'Connection with {client_address} closed.')
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

    start_server()