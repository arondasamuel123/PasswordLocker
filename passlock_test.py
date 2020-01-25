import unittest
from client import Client
from account_details import AccountDetails


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
    
    def test_several_clients(self):
        '''
        Test to save more than one client 
        '''
        self.new_client.save_client()
        test_client = Client("Alvin", "Kyle", "kyle@gmail.com", "abcdef")
        test_client.save_client()

        test_client2 = Client("Monica","Oyugi","oyugi@gmail.com", "123abc")
        test_client2.save_client()

        self.assertEqual(len(Client.u_list), 3)
    

class TestAccountDetails(unittest.TestCase):
    
    def setUp(self):
        """
        Set Up with dummy instance object of Account Details 
        """
        self.new_acc = AccountDetails("Sydx10", "Snapchat", "syd123")

    def test__init__(self):
        """
        Created test to check if the object has actually been instansiated 
        """
        self.assertEqual(self.new_acc.acc_username,"Sydx10")
        self.assertEqual(self.new_acc.platform_name, "Snapchat")
        self.assertEqual(self.new_acc.acc_password, "syd123")
    
    def test_save_acc(self):
        
        self.new_acc.save_acc()
        self.assertEqual(len(AccountDetails.details_list), 1)

    




if __name__=='__main__':
    unittest.main()