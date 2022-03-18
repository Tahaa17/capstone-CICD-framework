import sys
import unittest

sys.path.insert(1,'C:\\Users\\RTEMSOFT\\Desktop\\carla-capstone\\python\\client')

import client_MODIFIED as client
class TestSteeringWheelKit(unittest.TestCase):
    def test_acceleration_input(self):
        client.main(1)
        print(client.get_speed())
        self.assertGreater(client.get_speed(),1)
if __name__ == '__main__':
    unittest.main()


