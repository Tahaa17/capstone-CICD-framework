import sys
import getopt
import subprocess
import unittest
connection = subprocess.check_output("adb devices").strip()
connectionStripped = str(connection).replace("\\t","+")
class TestADB(unittest.TestCase):

    def test_creation_of_connection(self):
        connectionCreated = False
        if("SGWOOFVOO7NJRO7H+device" in str(connectionStripped)):
            print("Test Passed!")
            connectionCreated = True
        elif("SGWOOFVOO7NJRO7H+offline" in str(connectionStripped)):
            print("Test failed! Device is offline!")
            connectionCreated = False
        else:
            print("Test Failed! Could not create ADB connection!")
            connectionCreated = False
        self.assertTrue(connectionCreated)

if __name__ == '__main__':
    unittest.main()
