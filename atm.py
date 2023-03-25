class atm(object):
    def __init__(self,atmno,pinno):
        self.atmno=atmno
        self.pinno=pinno
    def   cashwithdrawel(self,amount):
        new_amount= 50000 - amount
        print("you have withdrawnedthe amount"+str(amount)+"your remaining balance is"+str(new_amount) )  
    def check_balance(self):
        print("your balance is 50000")

def main():
    Card_number = input("insert your card number:- ")
    pin_number  = input("enter your pin number:- ")

    new_user =  atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()


