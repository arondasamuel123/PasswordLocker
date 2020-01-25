import unittest
from details import AccountDetails


class TestAccountDetails(unittest.TestCase):

    def setUp(self):
        self.new_creds = AccountDetails("Sydx10","Snapchat")
    

