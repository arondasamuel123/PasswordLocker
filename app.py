from client import Client
from account_details import AccountDetails
import strgen

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

def create_acc(acc_username, platform_name, acc_password):
    new_account = AccountDetails(acc_username,platform_name,acc_password)
    return new_account

def save_account(account_details):
    """
    Save an account in the account details list
    """
    account_details.save_acc()

def display_accounts():
    """
        Display all account credentials
    """
    return AccountDetails.display_accs()

def find_creds(acc_username):
    """
    Finding account credentials 
    """
    return AccountDetails.find_creds(acc_username)

def del_creds(account_details):
    """
    Delete credentials function 
    """
    return account_details.delete_acc()

def main():
    while True:
        print("Hello, This will be your personal Password Vault. What would like to do?")
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
            

        elif option == 2:
            print("Enter Email")
            accessemail = input()
            print("Enter Password")
            accesspass = input()
            if find_client(accesspass):
                print(f"Welcome to your Password Vault {accessemail}. What would like to do?")
                print("4.Add credentials 5.View credentials  0.Delete credentials  9.Add existing credentials")
                choice = int(input())

                if choice == 4:
                        print("Enter account username")
                        acc_name = input()
                        print("Enter Platform name")
                        plat_name = input()
                        print("6.Would like a generated password?  7.Would like to create your own password?")
                        choice = int(input())

                        if choice == 6:
                                acc_pass = strgen.StringGenerator("[\d\w]{8}").render()
                                print(f"Password: {acc_pass}")
                        elif choice == 7:
                                print("Enter password")
                                acc_pass = input()
                        else:
                                print("Wrong choice")

                        save_account(create_acc(acc_name,plat_name,acc_pass))
                        print(f"Account Name: {acc_name} Platform Name: {plat_name} Account Password: {acc_pass}" )

                if choice==5:
                    print("Enter Account username")
                    acc_username = input()
                    if find_creds(acc_username):
                        for client in display_accounts():
                            print(f"Account Name:{client.acc_username}, Platform Name:{client.platform_name}, Account Password:{client.acc_password}")
                if choice==0:
                    print("Enter Account username")
                    creds_deleted = input()
                    deleted = find_creds(creds_deleted)
                    del_creds(deleted)
                    print("Your credentials have been deleted")
                
                if choice== 9:
                    print("Enter Account Username")
                    cred_username = input()
                    print("Enter Platform Name")
                    cred_plat_name = input()
                    print("Enter Account Password")
                    cred_password = input()

                    save_account(create_acc(cred_username,cred_plat_name,cred_password))
                    print(f"Account Username: {cred_username} Platform Name: {cred_plat_name} Account Password:{cred_password}")
                


                else:
                    print("Invalid choice")

            else:
                print("Invalid credentials")
        else:
            print("Incorrect choice")

        

if __name__ == '__main__':

    main()