import socket

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
    except ConnectionRefusedError:
        print(f"Connection failed. Is the server running at {addr}:{port}?")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()
        print("Client connection closed.")
    
if __name__ == "__main__":
    start_client()