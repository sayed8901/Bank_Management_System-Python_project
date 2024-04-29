class User:
    def __init__(self, name, password, email, address, account_type) -> None:
        self.name = name
        self.password = password
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = name + '-' + password
        self.balance = 0
        self.transaction_history = []
        self.loan_term = 2
    

    def __repr__(self) -> str:
        return f'User_Account_holder: {self.name}, account_type: {self.account_type}, transactions: {self.transaction_history}'
    

    def user_login(self, bank, account_number, email):
        if account_number not in bank.user_accounts:
            print(f'\nAccount does not exist: {account_number}. Please type carefully !!\n')
        else:
            if email != bank.user_accounts[account_number].email:
                print('Incorrect email address provided !!')
            else:
                print(f'Welcome user: {account_number}. You have logged in successfully.')

    
    def deposit(self, amount):
        self.balance += amount
        print(f'\ntk {amount} deposited successfully.\n')

        self.transaction_history.append(f'tk {amount} deposited')
    

    def withdraw(self, bank, amount):
        if bank.is_bankrupt == True:
            print('This bank is bankrupt. You can not withdraw from this bank anymore !!!')
        else:
            if amount > self.balance:
                print('\nWithdrawal amount exceeded !!\n')
            else:
                self.balance -= amount
                print(f'\ntk {amount} withdrawn successfully.\n')

                self.transaction_history.append(f'tk {amount} withdrawn')
    

    def check_balance(self):
        print(f'\nAvailable balance is : tk {self.balance}\n')
    

    def show_transaction_history(self):
        print('\nYour transaction history : \n')
        for history in self.transaction_history:
            print(history)
    

    def taking_loan(self, bank, amount):
        if bank.is_loan_opportunity == True and bank.is_bankrupt == False and self.loan_term > 0:
            self.loan_term -= 1

            self.balance += amount
            bank.total_loan += amount

            print(f'\ntk {amount} loaned successfully.\n')
            self.transaction_history.append(f'tk {amount} loan taken')

        elif bank.is_loan_opportunity == False:
            print('\nCurrently loan feature is not available in this bank\n')
        elif bank.is_bankrupt == True:
            print('\nThis bank is bankrupt. You can not take no more loan from this bank !!!\n')
        else:
            print('\nYou have already taken loan for the maximum 2 terms\n')
    

    def transfer_amount(self, bank, receivers_account_number, amount):
        if receivers_account_number not in bank.user_accounts:
            print(f'\nAccount does not exist: {receivers_account_number}. Please type carefully !!\n')
        else:
            if bank.is_bankrupt == True:
                print('\nThis bank is bankrupt. You can not send no more money from this bank !!!\n')
            elif amount < self.balance and bank.is_bankrupt == False:
                # deducting money from the senders account balance
                self.balance -= amount

                # adding money to the receivers account balance
                bank.user_accounts[receivers_account_number].balance += amount

                print(f"\nSuccessfully sent tk {amount} to: '{receivers_account_number}'\n")

                # tracking transaction for sender
                self.transaction_history.append(f"tk {amount} sent to: '{receivers_account_number}'")
                # tracking transaction for receiver
                bank.user_accounts[receivers_account_number].transaction_history.append(f"Received tk {amount} from '{self.account_number}'")

            else:
                print('\nYou dont have enough balance !!\n')






class Admin:
    def __init__(self, name, password, email, address) -> None:
        self.name = name
        self.password = password
        self.email = email
        self.address = address
        self.id_number = name + '-' + password
    

    def __repr__(self) -> str:
        return f'Admin_Name: {self.name}, email: {self.email}'
    

    def delete_account(self, bank, account_number):
        if account_number not in bank.user_accounts:
            print(f'\nAccount does not exist: {account_number}. Please type carefully !!\n')
        else:
            del bank.user_accounts[account_number]
            print(f'\nAccount successfully deleted for : {account_number}\n')
    

    def view_all_users_account(self, bank):
        print('\naccount_number\tname\tpassword\temail\taddress\taccount_type\ttransaction_history')
        for account_number, details in bank.user_accounts.items():
            print(f'{account_number}\t{details.name}\t{details.password}\t{details.email}\t{details.address}\t{details.account_type}\t{details.transaction_history}\t')
        print()

    
    def total_available_balance(self, bank):
        total_balance = 0
        for customer_details in bank.user_accounts.values():
            total_balance += customer_details.balance
        print(f'\nTotal available balance in {bank.name} is: {total_balance}\n')
    

    def total_loan_amount(self, bank):
        print(f'\nTotal loan in {bank.name} is: tk {bank.total_loan}\n')
    

    def loan_feature_on(self, bank):
        if bank.is_loan_opportunity == False:
            bank.is_loan_opportunity = True
            print("\nLoan feature is 'available' now for this bank")
        else:
            print("\nLoan feature is already 'available' for this bank !!")


    def loan_feature_off(self, bank):
        if bank.is_loan_opportunity == True:
            bank.is_loan_opportunity = False
            print("\nLoan feature is 'not available' now for this bank")
        else:
            print("\nLoan feature is already 'not available' for this bank !!")


    def bankrupt_on(self, bank):
        if bank.is_bankrupt == False:
            bank.is_bankrupt = True
            print("\nThis bank is bankrupt now. No loan or withdrawal available from this bank anymore !!!")
        else:
            print("\nThis bank is already declared as bankrupt !!")






class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.total_loan = 0
        self.is_loan_opportunity = True
        self.is_bankrupt = False

        self.user_accounts = {}
        self.admin_lists = {}

    def add_user(self, user):
        self.user_accounts[user.account_number] = user
        print(f'\nUser added successfully.\n')
    
    def add_admin(self, admin):
        self.admin_lists[admin.id_number] = admin
        print(f'\nAdmin added successfully.\n')






# Create a Bank instance
DBBL = Bank('DBBL')

# Create Admin instances
admin = Admin('Sohel', '8901', 'sohel@gmail.com', 'Dhaka')

# Add admin to the bank
DBBL.add_admin(admin)








# replica system

while True:
    print(f'Welcome to {DBBL.name}.\n')

    print('1. User portal')
    print('2. Admin portal')
    print('3. Exit\n')

    option = int(input('Enter your choice : '))


    while option == 1:
        print(f"\nWelcome to the 'user portal' of {DBBL.name}\n")

        print('1.1 Create user account')
        print('1.2 User login')
        print('1.3 Deposit')
        print('1.4 Withdraw')
        print('1.5 Check balance')
        print('1.6 Take loan')
        print('1.7 Money transfer')
        print('1.8 Check transaction history')
        print('1.9 Back to main menu\n')

        choice = float(input('Enter your Choice : '))


        if choice == 1.1:
            name = input('Enter your name : ')
            password = input('Enter your password : ')
            email = input('Enter your email : ')
            address = input('Enter your address : ')
            account_type = input("Enter your account type: 'current / savings' : ")

            new_user = User(name, password, email, address, account_type)
            DBBL.add_user(new_user)
        

        if choice == 1.2:
            account_no = input('Enter your acount number : ')
            email = input('Enter your email address : ')
            new_user.user_login(DBBL, account_no, email)


        if choice == 1.3:
            deposit_amount = int(input('Enter the amount you want to deposit : '))
            new_user.deposit(deposit_amount)
        

        if choice == 1.4:
            withdraw_amount = int(input('Enter the amount you want to withdraw : '))
            new_user.withdraw(DBBL, withdraw_amount)
        
        
        if choice == 1.5:
            new_user.check_balance()
        

        if choice == 1.6:
            loan_amount = int(input('Enter the amount you want to take loan : '))
            new_user.taking_loan(DBBL, loan_amount)
        

        if choice == 1.7:
            receiver_account_no = input('Enter the receivers account number : ')
            transfer_amount = int(input('Enter the amount you want to transfer : '))
            new_user.transfer_amount(DBBL, receiver_account_no, transfer_amount)
        

        if choice == 1.8:
            new_user.show_transaction_history()
            
        
        if choice == 1.9:
            break

    


    while option == 2:
        print(f"\nWelcome to the 'admin portal' of {DBBL.name}\n")

        print('2.1 Create user account')
        print('2.2 Create admin account')
        print('2.3 Delete any user account')
        print('2.4 View all user account list')
        print('2.5 Check total available balance of the bank')
        print('2.6 Check total loan amount of the bank')
        print('2.7 Open / Close the loan feature of the bank')
        print("2.8 Declare the bank as 'bankrupt'")
        print('2.9 Back to main menu\n')

        choice = float(input('Enter your Choice : '))


        if choice == 2.1:
            name = input('Enter your name : ')
            password = input('Enter your password : ')
            email = input('Enter your email : ')
            address = input('Enter your address : ')
            account_type = input("Enter your account type: 'current / savings' : ")

            new_user = User(name, password, email, address, account_type)
            DBBL.add_user(new_user)
        

        if choice == 2.2:
            name = input('Enter your name : ')
            password = input('Enter your password : ')
            email = input('Enter your email : ')
            address = input('Enter your address : ')

            new_admin = User(name, password, email, address)
            DBBL.add_admin(new_admin)


        if choice == 2.3:
            account_number = input('Enter the account number : ')
            admin.delete_account(DBBL, account_number)
        

        if choice == 2.4:
            admin.view_all_users_account(DBBL)


        if choice == 2.5:
            admin.total_available_balance(DBBL)
        

        if choice == 2.6:
            admin.total_loan_amount(DBBL)

        
        if choice == 2.7:
            if DBBL.is_loan_opportunity == False:
                admin.loan_feature_on(DBBL)
            elif DBBL.is_loan_opportunity == True:
                admin.loan_feature_off(DBBL)


        if choice == 2.8:
            admin.bankrupt_on(DBBL)


        if choice == 2.9:
            break




    if option == 3:
        break


