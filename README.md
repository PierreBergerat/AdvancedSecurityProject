# Advanced Security project : Ransomware
- [Advanced Security project : Ransomware](#advanced-security-project--ransomware)
  - [1. Description](#1-description)
  - [2. Workflow](#2-workflow)
  - [3. Detailed explanations](#3-detailed-explanations)
    - [3.1. Http Server](#31-http-server)
    - [3.2. VBA Macro](#32-vba-macro)
    - [3.3. Update.zip](#33-updatezip)
    - [3.4. Socket Server](#34-socket-server)
## 1. Description
This repository aims to demonstrate a security flaw in an office 2019 version as well as a way to use this flaw in order to gain complete access to a compromised system by the use of various techniques specific to MacOS.

## 2. Workflow
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
## 3. Detailed explanations
### 3.1. Http Server
### 3.2. VBA Macro
### 3.3. Update.zip
### 3.4. Socket Server