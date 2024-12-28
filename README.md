# Simple-TCP-Client-Server

This project demonstrates a simple TCP server and client implementation in Python. The server listens for incoming connections and allows communication with a client. Both server and client support user-configurable address and port settings via command-line arguments or interactive input.

---

## Screenshots

### Server Output
Here’s an example of the server output when a client connects and sends a message:
#### Server
![Screenshot 2024-12-28 173713](https://github.com/user-attachments/assets/98a7414c-04a1-43ec-b6ad-97f3085bef8a)

### Client Output
Here’s an example of the client output after connecting to the server:
#### Client 1
![Screenshot 2024-12-28 173738](https://github.com/user-attachments/assets/94c7428c-82d1-49b7-a245-d7ed709436b4)

#### Client 2
![Screenshot 2024-12-28 173751](https://github.com/user-attachments/assets/92a71c32-a02f-4425-a889-153ccd70ebad)

---

## Features

### Server
- Listens for incoming TCP connections from clients.
- Uses multithreading to handle multiple clients concurrently.
- Allows message exchange with clients.
- Supports command-line argument configuration or interactive input for the address and port.
- Graceful shutdown with error handling.
- Tracks the number of connected clients.

### Client
- Connects to the server using a specified address and port.
- Allows bidirectional communication with the server.
- Supports command-line argument configuration or interactive input for the address and port.
- Handles errors and unexpected disconnections.

---

## Requirements
- Python 3.x

---

## How to Run

### Server
1. Navigate to the project directory.
2. Run the server script:
   ```bash
   python3 server.py --addr <server_address> --port <server_port>
   ```
   Example:
   ```bash
   python3 server.py --addr 127.0.0.1 --port 12345
   ```
3. If no arguments are provided, the script will prompt for input:
   ```bash
   python3 server.py
   ```
   Example of prompted input:
   ```bash
   Enter server address (default 'localhost'): 127.0.0.1
   Enter server port (default 12345): 12345
   ```
### Client
1. Navigate to the project directory.
2. Run the server script:
   ```bash
   python3 client.py --addr <server_address> --port <server_port>
   ```
   Example:
   ```bash
   python3 client.py --addr 127.0.0.1 --port 12345
   ```
3. If no arguments are provided, the script will prompt for input:
   ```bash
   python3 client.py
   ```
   Example of prompted input:
   ```bash
   Enter server address (default 'localhost'): 127.0.0.1
   Enter server port (default 12345): 12345
   ```

---

## Notes

- Ensure the server is running before starting the client.

- For communication on the same machine, you can use `localhost` or `127.0.0.1` as the server address.

- If running on different machines, ensure the server's IP address is accessible from the client machine (consider firewall settings and network configurations).
  
- The server tracks the number of connected clients and prints updates on the client connection status.
  
- Multithreading is used on the server side to handle multiple clients concurrently, allowing each client to communicate with the server without blocking others.
