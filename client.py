class Client:
    """
    Class that creates  new instances of client
    """
    u_list = []

    def __init__(self, fn, ln, email, password):
        self.fn = fn
        self.ln = ln
        self.email = email
        self.password = password
    
    def save_client(self):
        """
        Function to save client to list 
        """
        Client.u_list.append(self)

    @classmethod
    def find_client(cls, email, password):
        """
        Function that takes in a password and the user 

        Args:
            password ro search for 
        Returns :
            Logins in user to application
        """
        for client in cls.u_list:
            if client.password == password:
                return client

    