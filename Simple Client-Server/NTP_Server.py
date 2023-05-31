import ntplib
from time import ctime
from socketserver import ThreadingUDPServer, BaseRequestHandler


class NTPServerHandler(BaseRequestHandler):
    def handle(self):
        # Get the client's address and socket
        addr = self.client_address[0]
        sock = self.request[1]

        # Create an NTP client object
        client = ntplib.NTPClient()

        # Get the current time from the NTP server
        response = client.request('pool.ntp.org')

        # Get the current time and format it
        current_time = ctime(response.tx_time)

        # Send the current time to the client
        sock.sendto(current_time.encode(), self.client_address)


if __name__ == '__main__':
    # Set the IP address and port for the server
    server_address = ('localhost', 12345)

    # Create a UDP server with threading support
    server = ThreadingUDPServer(server_address, NTPServerHandler)

    # Start the server
    print('NTP server is running...')
    server.serve_forever()
