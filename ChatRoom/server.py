import socket
import threading
import tkinter as tk

class Server:
    def __init__(self, master, port):
        self.master = master
        self.port = port
        self.socket = None
        self.clients = {}

        self.status_label = tk.Label(master, text="Server is running on port {}".format(port))
        self.status_label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_server)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_server, state=tk.DISABLED)
        self.stop_button.pack()

    def start_server(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("localhost", self.port))
        self.socket.listen(5)

        self.status_label.config(text="Server is running on port {}".format(self.port))
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        threading.Thread(target=self.accept_clients).start()

    def accept_clients(self):
        while True:
            client_socket, address = self.socket.accept()

            username = "User{}".format(len(self.clients) + 1)
            client_socket.sendall(username.encode())

            client = {"username": username, "socket": client_socket}
            self.clients[username] = client

            self.broadcast_message("{} has joined the chat.".format(username))

            threading.Thread(target=self.handle_client, args=(client,)).start()

    def handle_client(self, client):
        username = client["username"]
        socket = client["socket"]

        while True:
            try:
                message = socket.recv(1024).decode()
                if not message:
                    break

                self.broadcast_message("{}: {}".format(username, message))
            except ConnectionResetError:
                break

        self.remove_client(username)

    def remove_client(self, username):
        client = self.clients.pop(username)
        client["socket"].close()

        self.broadcast_message("{} has left the chat.".format(username))

    def broadcast_message(self, message):
        for client in self.clients.values():
            client["socket"].sendall(message.encode())

    def stop_server(self):
        for client in self.clients.values():
            client["socket"].close()

        self.socket.close()
        self.socket = None

        self.status_label.config(text="Server stopped.")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chat Room Server")

    server = Server(root, 8000)

    root.mainloop()
