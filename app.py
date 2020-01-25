from client import Client
from account_details import AccountDetails

def create_client(fn, ln, email, password):
    """
    Function to create user
    """
    new_acc = Client(fn,ln, email, password)
    return new_acc
def save_client(client):
    """
    Function to save the user to a list
    """
    client.save_client()

def find_client(password)
    """
    Function to login in user to the application
    """
    return Client.find_client(password)


main()