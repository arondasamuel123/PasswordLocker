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

    def test_delete_client(self):
        '''
        Test carried to check if client has been deleted 
        '''
        self.new_client.save_client()
        test_client = Client("Sydney", "Domingo", "sydx10@gmail.com", "12345")
        test_client.save_client()
        test_client.del_client()
        self.assertEqual(len(Client.u_list), 1)



if __name__=='__main__':
    unittest.main()