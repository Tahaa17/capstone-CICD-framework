import sys
import getopt
import subprocess
import unittest
f=open("C:\\Users\\Shdow\\Desktop\\Capstone\\fileUploaded.txt","r")
packageName = f.read()
print(packageName)
installed = str(subprocess.check_output("adb shell am start -n "+packageName+"/"+packageName+".MainActivity"))
print(installed)


class TestAppRunning(unittest.TestCase):
    
    
    def test_CPU_usage(self):
        if(len(packageName)>=15):
            packageNameCut = packageName[0:15]+"+"
        cpuData= str(subprocess.check_output("adb shell top -n 1 | FINDSTR "+packageNameCut, shell=True))
        self.assertNotEqual(cpuData,"")
if __name__ == '__main__':
    unittest.main()