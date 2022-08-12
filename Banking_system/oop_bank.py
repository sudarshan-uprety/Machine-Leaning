import csv
import pandas as pd

class Bank:

    def __init__(self):
        self.choose_user()

    def choose_user(self):
        print("1. New User.")
        print("2. Already User.")
        print("")
        cu=int(input("Please choose the option: "))
        print("")
        if cu==1:
            self.create_account()
        elif cu==2:
            self.login_account()
        else:
            print("Sorry wrong input")
            print("..........Redirecting to previous part..........")


    def create_account(self):
        name=input("Please enter your name: ")
        p1=int(input(f"{name} please choose the pin: "))
        p2=int(input(f"{name} please confirm your pin: "))
        if(p1==p2):
            print(f"Congratulation {name} you have successfully created bank account")
            balance=0
            with open("database.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, p2,balance])
            file.close()
            print("..........We are redirecting you to login page..........")
            self.login_account()
        else:
            print("Pin did not matched.")
            self.create_account()
            return


    def login_account(self):
        self.uname = input("Please ennter your name: ")
        csv_file = csv.reader(open("database.csv", "r"))
        for row in csv_file:
            if self.uname in row[0]:
                p = row[1]
                self.balance=int(row[2])
                self.p=int(p)
                for i in range(1, 4):
                    print("")
                    pin = int(input(f"Please enter your pin. You have {4 - i} chance: "))
                    if pin==self.p:
                        print("..........Logged In..........")
                        self.choose_process()

                        break
                    else:
                        print("Sorry wrong pin")
                    while i == 3:
                        print("Sorry your account has been temporarily banned.")
                        break
                if(self.uname not in row[0]):
                    print("Sorry you do have account in our bank.")
                    break




    def choose_process(self):
        print(f"..........Welcome {self.uname}..........")
        print("")
        print("")
        print(".....Please Select The Option Below.....")
        print("")
        print("1. Check the balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Change your pin")
        print("5. Exit")
        print("")
        print("")
        op = int(input("Please enter your option: "))
        print("")
        if (op == 1):
            self.check_balance()
        if (op == 2):
            self.deposite_money()
        if (op == 3):
            self.withdraw_money()
        if (op == 4):
            self.change_pin()
        if (op==5):
            self.exit_account()

    def other_services(self):
        lo = input("Do you want to use other service as well (yes or no) ?: ")
        if lo == 'yes':
            self.choose_process()
        if lo == 'no':
            self.exit_account()


    def check_balance(self):
        print("")
        print(f"{self.uname} your total balance is {self.balance}")
        print("")
        print("")
        self.other_services()




    def withdraw_money(self):
        print("")
        wb=int(input("Please enter the balance you want to withdraw: "))
        if wb<=self.balance:
            nb=self.balance-wb
            print("")
            print(f"..........Please collect you cash {wb} in the counter...........")
            df = pd.read_csv('database.csv', index_col='name')
            # Set cell value at row 'c' and column 'Age'
            df.loc[self.uname, 'balance'] =nb
            # Write DataFrame to CSV file
            df.to_csv('database.csv')

        else:
            print(f"..........Sorry {self.uname} you do not have enough balance to withdraw..........")
            print("")
        print("")
        self.other_services()



    def deposite_money(self):
        print("")
        da=int(input("Please enter the amount you want to deposit: "))
        print("")
        nb=self.balance+da
        df = pd.read_csv('database.csv', index_col='name')
        # Set cell value at row 'c' and column 'Age'
        df.loc[self.uname, 'balance'] = nb
        # Write DataFrame to CSV file
        df.to_csv('database.csv')
        print(f"..........Hey {self.uname} you have deposited {da} to your account..........")
        print("")
        self.other_services()

    def change_pin(self):
        print("")
        pc=int(input("Please enter your previous pin: "))
        if pc==self.p:
            p1=int(input("Please enter the new pin: "))
            p2=int(input("Please confirm your new pin: "))
            if p1==p2:
                df = pd.read_csv('database.csv', index_col='name')
                # Set cell value at row 'c' and column 'Age'
                df.loc[self.uname, 'pin'] = p2
                # Write DataFrame to CSV file
                df.to_csv('database.csv')
                print(".....Your pin has been changed successfully.....")
        else:
            print("WRONG PIN")
            self.choose_process()



    def exit_account(self):
        print("..........logging out..........")
        return



while True:
    user=Bank()
