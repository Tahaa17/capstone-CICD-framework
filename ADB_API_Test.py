import sys
import getopt
import subprocess
import unittest
f=open("C:\\Users\\Shdow\\Desktop\\Capstone\\fileUploaded.txt","r")
packageName = f.read()
print(packageName)
brakeMethod = "Vehicle.brake.press()"
invocation = str(subprocess.check_output("adb logcat | findstr " + packageName))
print (invocation)
class TestAPICall(unittest.TestCase):

    def test_car_api_usage(self):
        if(brakeMethod == invocation):
            print("Brake method has been invoked")
            isUsed=False
        else:
            isUsed=True
        self.assertTrue(isUsed)

if __name__ == '__main__':
    unittest.main()