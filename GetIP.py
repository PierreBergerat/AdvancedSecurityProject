import socket


# Retourne l'adresse IP à utiliser dans les payloads
def getLocalIP():
    try: # Tentative de connexion à google pour obtenir l'IP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except: # En cas d'échec, utilisation de gethostbyname (peut retourner de fausses adresses en cas de cartes réseaux virtuelles)
        return socket.gethostbyname(socket.gethostname())
