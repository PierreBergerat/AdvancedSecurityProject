# Advanced Security Project : MacOS Excel Ransomware
## Description
When run, this script will ask for user password then proceed to create a new encrypted Volume called "OhNoItsLocked" with a key of 504 bits (maximum key length allowed by MacOS for a drive password). Using Rsync, all files contained in ~/ (User home directory) will be moved to this new drive before it is unmounted. Files containing an encrypted password and a tutorial to send the ransom will then be generated on the Desktop.
## Detailed explanations
1. Creation of a temporary drive that will contain the Excel icon
2. Creation of said icon from Base64 decode. This way, the program won't rely on the default installation path of Excel to query the icon
3. Creation of local variables containing informations about the user (name and id)
4. Display of an Excel looking dialog asking for the user's password
   * Verification of the password and loop to point 4 if wrong
5. Generation of a 63 bytes long password that will be used to encrypt the drive
6. Creation of the encrypted drive with the password generated in the previous point
7. Migration of all the files contained in ~/ onto the new drive
8. As the migration is used with sudo privileges, the property of the files needs to be given back to the regular user (instead of root)
9. Unmounting of the encrypted drive
10. Creation of the attacker public key from Base64
11. Encryption of the password of the drive with the public key and storage of the encrypted password on the Desktop
12. Creation of a shortcut to "Disk Utility.app" on the desktop (in order to allow unexperienced users to access it easily)
13. Creation of the ransom message on the Desktop
14. Destruction of the temporary files