def menu():
    welcome="Welcome to SBI"
    print(welcome.center(100))
    print("1) press 1 to create account \n2) press 2 for balance \n3) press 3 to deposit \n4) press 4 to withdraw \n5) press 5 to exit")


def choice():
    choice=int(input("Enter your choice:"))
    return choice                

def deposit(amt):
    return (balance+amt)

def withdraw(bal,amt):
    global balance
    if amt>bal:
        print("Insufficient Balance..")
    else:
        balance=bal-amt

menu()
ch=choice()
while ch in (1,2,3,4,5):
        if ch==1:
            name=input("Enter your name:")
            accno=int(input("Enter account no:"))
            balance=1000        #initial balance loaded with 1000
            menu()
            ch=choice()
        

        elif ch==2:
            print("\t\tCurrent Balance:",balance)
            menu()

            ch=choice()
        
        elif ch==3:
            amount=int(input("Enter the amount you want to deposit?"))
            balance=deposit(amount)
            print("\t\tAmount Deposited.. Your New Balance is:",balance)
            menu()
            
            ch=choice()
        
        elif ch==4:
            amount=int(input("Enter the amount you want to withdraw?"))
            if balance>0:
                withdraw(balance,amount)
                print("\t\tNew Balance:",balance)
            else:
                print("\t\tInsufficient Balance..")
            menu()
            
            ch=choice()
        
        elif ch==5:
            exit()
        
        else:
            print("Invalid Choice..")
