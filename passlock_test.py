import unittest
from client import Client

class TestPassLock(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test casescont
        '''
        self.new_client = Client("Samuel", "Aronda", "arondasamuel123@gmail.com", "darko@420")

    
    def test__init__(self):
        '''
        Test if the object has been instantiated 
        '''
        self.assertEqual(self.new_client.fn,"Samuel")
        self.assertEqual(self.new_client.ln,"Aronda")
        self.assertEqual(self.new_client.email, "arondasamuel123@gmail.com")
        self.assertEqual(self.new_client.password, "darko@420")


if __name__=='__main__':
    unittest.main()