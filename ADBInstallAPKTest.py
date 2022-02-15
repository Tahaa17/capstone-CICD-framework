import sys
import getopt
import subprocess
import unittest
f=open("C:\\Users\\Shdow\\Desktop\\Capstone\\fileUploaded.txt","r")
packageName = f.read()
print(packageName)
installed = str(subprocess.check_output("adb shell pm list packages "+packageName))
print (installed)
class TestADB(unittest.TestCase):

    def test_installation(self):
        isInstalled = False
        if(packageName in installed):
            print("APK installed Successfully")
            isInstalled=True
        else:
            isInstalled=False
        self.assertTrue(isInstalled)

if __name__ == '__main__':
    unittest.main()
