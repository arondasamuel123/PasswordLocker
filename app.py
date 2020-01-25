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

def find_client(password):
    """
    Function to login in user to the application
    """
    return Client.find_client(password)


def main():
    while True:
    print("Hello, I am your personal Password Vault. What would like to do?")
    print("1.Register   2.Login")
    option = int(input())

    if option == 1:
        print("Alright lets get started!!")
        print("Enter your first name")
        print("."*20)
        first_n = input()

        print("Enter your last name")
        print("."*20)
        last_n = input()

        print("Enter your email")
        print("."*20)
        email = input()

        print("Enter your password you like to use")
        print("."*20)
        password = input()

        save_client(create_client(first_n, last_n, email, password))

        print(f"Thank you for signing up {first_n} {last_n}. You can now Login")

if __name__ == '__main__':

    main()