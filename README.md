# Advanced Security Project : MacOS Excel Ransomware
- [Advanced Security Project : MacOS Excel Ransomware](#advanced-security-project--macos-excel-ransomware)
  - [Description](#description)
  - [Workflow](#workflow)
  - [Detailed explanations](#detailed-explanations)
    - [1. Http Server](#1-http-server)
    - [2. VBA Macro](#2-vba-macro)
    - [3. Update.zip](#3-updatezip)
    - [4. Socket Server](#4-socket-server)
## Description
This repository aims to demonstrate a security flaw in an office 2019 version as well as a way to use this flaw in order to gain complete access to a compromised system by the use of various techniques specific to MacOS.

## Workflow
The complete workflow works as follows :
1. The victim opens an injected Microsoft Excel file which will fire a macro as soon as it is opened.
2. This macro will request and download two files from the attacker server (which lays in \_\_main__.py). These two files are :
   1. A zip file containing a folder called LaunchAgents which itself contains a plist file allowing for a reverse shell at the restart of the system
   2. A python file which uses MacOS librairies in order to add the zip file as a login item, which will uncompress it when the victim will restart or relog in the system
3. Once the system is reloaded and the reverse shell is initiated, the victim will connect to a socket server (server.py) which will allow the attaquer to input commands into the victim's system.
   1. The "phishing" command will pop a native window asking for a password in order to install a fake update
   2. The "ransom" command will
      1. Create a new disk partition encrypted with a 127 bits password
      2. Move every file from the desktop to this encrypted file
      3. Unmount the encrypted drive
## Detailed explanations
### 1. Http Server
### 2. VBA Macro
### 3. Update.zip
### 4. Socket Server