import unittest
from client import Client

class TestPassLock(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test casescont
        '''
        self.new_client = Client("Samuel", "Aronda", "arondasamuel123@gmail.com", "darko@420")

    def tearDown(self):
        Client.u_list=[]
    
    def test__init__(self):
        '''
        Test if the object has been instantiated 
        '''
        self.assertEqual(self.new_client.fn,"Samuel")
        self.assertEqual(self.new_client.ln,"Aronda")
        self.assertEqual(self.new_client.email, "arondasamuel123@gmail.com")
        self.assertEqual(self.new_client.password, "darko@420")

    def test_save_client(self):
        '''
        Test to save client to list 
        '''

        self.new_client.save_client()
        self.assertEqual(len(Client.u_list), 1)

    def test_find_client(self):
        '''
        Test to find user by  their password 
        '''
        self.new_client.save_client()
        test_client = Client("Sydney", "Domingo", "sydx10@gmail.com", "123456")
        test_client.save_client()
        found_pass = Client.find_client("123456")
        self.assertEqual(test_client.email,found_pass.email)




if __name__=='__main__':
    unittest.main()