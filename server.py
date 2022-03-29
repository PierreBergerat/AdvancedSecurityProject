import socket

HOST = "0.0.0.0"
PORT = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    client_socket, addr = s.accept()
    client_socket.settimeout(2)
    with client_socket:
        while True:
            command = input("~$: ")
            client_socket.send((command +"\n").encode())
            if command.lower() == "exit":
                break
            while True:
                try:
                    results = client_socket.recv(2048*1024).decode()
                    print(results)
                    print("bash" in results)
                except:
                    break
        client_socket.close()
        s.close()
