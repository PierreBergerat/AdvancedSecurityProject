from CoreFoundation import kCFURLPOSIXPathStyle
from CoreFoundation import CFURLCreateWithFileSystemPath
from CoreFoundation import kCFAllocatorDefault
from Foundation import NSBundle
from objc import loadBundleFunctions
from objc import loadBundleFunctions
from Foundation import NSBundle
from LaunchServices import kLSSharedFileListSessionLoginItems

# File or app to be added in the login items list
PATH = "/System/Applications/Utilities/Terminal.app"

shared_file_list = NSBundle.bundleWithIdentifier_(
    'com.apple.coreservices.SharedFileList')
f = [
    ('LSSharedFileListCreate',
     b'^{OpaqueLSSharedFileListRef=}^{__CFAllocator=}^{__CFString=}@'),
    ('LSSharedFileListCopySnapshot',
     b'^{__CFArray=}^{OpaqueLSSharedFileListRef=}o^I'),
    ('LSSharedFileListInsertItemURL',
     b'^{OpaqueLSSharedFileListItemRef=}^{OpaqueLSSharedFileListRef=}^{OpaqueLSSharedFileListItemRef=}^{__CFString=}^{OpaqueIconRef=}^{__CFURL=}^{__CFDictionary=}^{__CFArray=}'),
    ('kLSSharedFileListItemBeforeFirst', b'^{OpaqueLSSharedFileListItemRef=}')
]
loadBundleFunctions(shared_file_list, globals(), f)
appURL = CFURLCreateWithFileSystemPath(None, PATH, kCFURLPOSIXPathStyle, False)
items = LSSharedFileListCreate(kCFAllocatorDefault, kLSSharedFileListSessionLoginItems, None)
LSSharedFileListInsertItemURL(items, kLSSharedFileListItemBeforeFirst, None, None, appURL, None, None)
