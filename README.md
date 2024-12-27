# Simple-TCP-Client-Server

This project demonstrates a simple TCP server and client implementation in Python. The server listens for incoming connections and allows communication with a client. Both server and client support user-configurable address and port settings via command-line arguments or interactive input.

---

## Features

### Server
- Listens for incoming TCP packets from client.
- Allows message exchange with clients.
- Supports command-line argument configuration or interactive input.
- Graceful shutdown with error handling.

### Client
- Connects to the server using a specified address and port.
- Allows bidirectional communication with the server.
- Supports command-line argument configuration or interactive input.
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
   python server.py --addr <server_address> --port <server_port>
   ```
   Example:
   ```bash
   python server.py --addr 192.168.1.50 --port 12345
   ```
3. If no arguments are provided, the script will prompt for input:
   ```bash
   python server.py
   ```
### Client
1. Navigate to the project directory.
2. Run the server script:
   ```bash
   python client.py --addr <server_address> --port <server_port>
   ```
   Example:
   ```bash
   python client.py --addr 127.0.0.1 --port 12345
   ```
3. If no arguments are provided, the script will prompt for input:
   ```bash
   python client.py
   ```

---

## Notes

- Ensure the server is running before starting the client.

- For communication on the same machine, you can use `localhost` or `127.0.0.1` as the server address.

- If running on different machines, ensure the server's IP address is accessible from the client machine.
