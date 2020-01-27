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
        found_pass = Client.find_client("sydx10@gmail.com","123456")
        self.assertEqual(found_pass.email,test_client.email)
    
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
    
    def tearDown(self):
        """
        
        """
        AccountDetails.details_list= []

    def test__init__(self):
        """
        Created test to check if the object has actually been instansiated 
        """
        self.assertEqual(self.new_acc.acc_username,"Sydx10")
        self.assertEqual(self.new_acc.platform_name, "Snapchat")
        self.assertEqual(self.new_acc.acc_password, "syd123")
    
    def test_save_acc(self):
        """
        Created test to check if object of Account Details is being added to a list
        """
        self.new_acc.save_acc()
        self.assertEqual(len(AccountDetails.details_list), 1)

    def test_save_multiple_acc(self):
        """
        Created test to save save multiple account to the list in a clasS AccountDetails
        """
        self.new_acc.save_acc()
        test_acc= AccountDetails("samuel123","Facebook", "samuel@123" )
        test_acc.save_acc()

        test_acc2 = AccountDetails("alvin.kyle", "Instagram", "kyle@abc")
        test_acc2.save_acc()
        self.assertEqual(len(AccountDetails.details_list), 3)

    def test_delete_acc(self):
        """
        Created test to delete account credentials 
        """
        self.new_acc.save_acc()
        test_acc3 = AccountDetails("hannes", "Reddit", "yoda")
        test_acc3.save_acc()
        
        test_acc3.delete_acc()
        self.assertEqual(len(AccountDetails.details_list),1)
    
    def test_display_accs(self):
        """
        Created test to display all account credentials for user
        """
        self.assertEqual(AccountDetails.display_accs(), AccountDetails.details_list)

    def test_find_creds(self):
        """
        Created test to find a users credentials
        """
        self.new_acc.save_acc()
        testacc4 = AccountDetails("peter123", "Gmail", "qwert123")
        testacc4.save_acc()
        
        found_creds = AccountDetails.find_creds("peter123")
        self.assertEqual(found_creds.acc_username,testacc4.acc_username)

    
        


    


    




if __name__=='__main__':
    unittest.main()