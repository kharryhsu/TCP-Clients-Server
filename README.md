# TCP-Clients-Server

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
- Listens for incoming TCP connections.
- Uses multithreading to handle multiple clients concurrently.
- Allows message exchange with clients.
- Supports address and port configuration via command-line arguments or interactive input.
- Provides error handling and graceful shutdown.
- Tracks and logs connected clients.

### Client
- Connects to the server using a specified address and port.
- Supports bidirectional communication with the server.
- Configurable via command-line arguments or interactive input.
- Handles errors and unexpected disconnections.

---

## Requirements
- Python 3.x

---

## Deployment

1. **Clone the Repository**
   
   Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/your-username/TCP-Clients-Server.git
   ```
2. **Navigate to the Project Directory**

   Change to the project directory:
   ```bash
   cd TCP-Clients-Server
   ```
3. **Run the Server**

   Start the server script:
   ```bash
   python3 server.py --addr <server_address> --port <server_port>
   ```
   Example:
   ```bash
   python3 server.py --addr 127.0.0.1 --port 12345
   ```
4. **Run the Client**

   Start the client script:
   ```bash
   python3 client.py --addr <server_address> --port <server_port>
   ```
   Example:
   ```bash
   python3 client.py --addr 127.0.0.1 --port 12345
   ```
5. **Interactive Input (Optional)**

   If no arguments are provided, the script will prompt for input. 
   Example:
   ```bash
   python3 server.py
   ```
   Prompted input example:
   ```bash
   Enter server address (default 'localhost'): 127.0.0.1
   Enter server port (default 12345): 12345
   ```

---

## Future Improvements

- Packet Header Implementation: Add packet headers for better data parsing and protocol handling.

- GUI Interface: Create a graphical user interface for improved usability and visualization.

---

## Notes

- Ensure the server is running before starting the client.

- Use `localhost` or `127.0.0.1` for communication on the same machine.

- For communication across different machines, ensure the server's IP address is accessible and firewall settings allow connections.
  
- The server logs the connection status of clients and uses multithreading to handle multiple clients simultaneously.

---

## Contributions

Thank you for your interest in this project! 🙌  
At the moment, we are not accepting contributions as the project is still under active development.  

Stay tuned for updates!
