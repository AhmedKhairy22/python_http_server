import socket

ip = "127.0.0.1"
port = 8080

# setting up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# initializing the server
server_socket.bind((ip, port))
server_socket.listen(5)

print(f"your server is running on {ip}:{port} ....")

# TODO: Handle multi clients by using multithreading
# TODO: Handel the parsing of the other http methods: POST, PUT, DELETE

while True:
    client_socket, client_addr = server_socket.accept()
    request = client_socket.recv(1024).decode()

    if not request:
        client_socket.close()
        continue
    
    headers = request.split("\n")

    request_line_components = headers[0].split()
    method = request_line_components[0]
    path = request_line_components[1]
    
    if method == 'GET':
        if path == "/":
            with open("index.html") as html_file:
                content = html_file.read()
        else:
            with open("404.html") as html_file:
                content = html_file.read()
                response = 'HTTP/1.1 404 Not Found\r\n\r\n' 

        response = 'HTTP/1.1 200 OK\r\n\r\n' + content + '\r\n'

    else:
        response = 'HTTP/1.1 405 MTHOD NOT ALLOWED\r\n\r\nAllow: GET\r\n'   


    client_socket.sendall(response.encode())
    client_socket.close()