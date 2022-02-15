from git import Repo
import subprocess
from pathlib import Path
import os
print (Path('C:\\Users\\Shdow\\Desktop\\Capstone\\Build1').is_dir())
if(not Path('C:\\Users\\Shdow\\Desktop\\Capstone\\Build1').is_dir()):
    Repo.clone_from('https://github.com/Tahaa17/capstone-app', "C:\\Users\\Shdow\\Desktop\\Capstone\\Build1")
else:
    repo = Repo('C:\\Users\\Shdow\\Desktop\\Capstone\\Build1')
    repo.remotes.origin.pull()
os.chdir('C:\\Users\\Shdow\\Desktop\\Capstone\\Build1\\MusicPlayer')
subprocess.call('gradlew assembleDebug',shell=True)
f="C:\\Users\\Shdow\\Desktop\\Capstone\\Build1\\MusicPlayer\\app\\build\\outputs\\apk\\debug\\app-debug.apk"
subprocess.call("adb install -r "+f,shell=True)
file = open("C:\\Users\\Shdow\\Desktop\\Capstone\\fileUploaded.txt", "w")
toWrite = str(subprocess.check_output("aapt dump badging "+f+" | findstr -n \"package: name\" | findstr \"1:\""))
toWrite.strip()
toWriteArray = toWrite.split("\'")
file.write(toWriteArray[1])
file.close()
