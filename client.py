import socket
import argparse

def start_client(addr='localhost', port=12345):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((addr, port))
        
        print(f'Connected to server at {addr}:{port}')
        
        while True:
            msg = input("Client: Enter message to send (or type 'exit' to end connection)\n> ")
            
            if msg.lower() == 'exit':
                print("Closing connection.")
                break
                
            try:
                client_socket.send(msg.encode('utf-8'))
            except Exception as e:
                print(f"Error sending message: {e}")
                break
            
            try:
                data = client_socket.recv(1024).decode('utf-8')
                
                if data:
                    print(f'Received from server: {data}')
                else:
                    print("Server closed the connection.")
                    break
            except Exception as e:
                print(f'Error receiving data: {e}')
    except KeyboardInterrupt:
        print("Exited by user.")
    except ConnectionRefusedError:
        print(f"Connection failed. Is the server running at {addr}:{port}?")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()
        print("Client connection closed.")
    
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
    
    start_client(addr=addr, port=port)