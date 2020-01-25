class AccountDetails:

    """
    Creating an instance of the account details of the user
    """

    details_list = []


    def __init__(self, acc_username, platform_name, acc_password):
        self.acc_username = acc_username
        self.platform_name = platform_name
        self.acc_password = acc_password

    def save_acc(self):
        AccountDetails.details_list.append(self)

    def delete_acc(self):
        AccountDetails.details_list.remove(self)

    @classmethod
    def display_accs(cls):

        return cls.details_list
    
    @classmethod
    def find_creds(cls, acc_username):
        for accountdetails in cls.details_list:
            if accountdetails.acc_username = acc_username
            
            return accountdetails


    