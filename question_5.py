'''
Question5: Create a "Customer" class and an "Account" class. Let the "Account" class inherit from the "Customer" class and represent a customer's bank account information.

##### Customer Class Features:
- "name" (customer name)
- "surname" (customer surname)
- "tc_identification" (customer TR ID number)
- "phone" (customer phone number)

##### Account Class Properties:
- "customer" (a Customer object)
- "account_number" (account number)
- "balance" (account balance)

##### Customer Class Method:
- "display_information()": Displays the customer's name, surname, TR ID number and telephone number.

##### Account Class Methods:
- "deposit(self, amount)": A method that deposits a certain amount of money into the account.
- "money_check(self, amount)": A method that withdraws a certain amount of money from the account. However, 
if there is not enough balance in the account, the transaction should not occur and a message should be displayed.
- "display_balance()": A method that displays the account balance.

Create these two classes, then create a Customer object and an Account object, add the customer information to the Account object, and perform account operations and view the results.
'''


class Customer:
    def __init__(self,name, surname, tc_identification, phone):
        self.name=name
        self.surname=surname
        self.tc_identification=tc_identification
        self.phone=phone
    def display_information(self):
        return f"{self.name} {self.surname} ismindeki musterinin TC kimlik numarasi '{self.tc_identification}', telefon numarasi ise '{self.phone}'dir."
    
class Account(Customer):
    def __init__(self, customer, account_number, balance):
        self.customer=customer
        self.account_number=account_number
        self.balance=balance
    
    def money_check(self, amount):
        if amount>self.balance:
            print(f"Islem Basarisiz. Yetersiz bakiye!")
            print()
        else:
            self.balance-=amount
            print(f"{amount} Euro para cekildi.")
            print()
    
    def deposit(self, amount):
        self.balance+=amount
        print(f"Hesaba {amount} Euro para yatirildi.")
        print()
    
    def display_balance(self):
        print(f"{self.customer.name} {self.customer.surname} isimli musterinin guncel hesap bakiyesi {self.balance} Euro'dur.")
        print()    

customer1=Customer('ilkay', 'Arslanoglu', '33868478962', '0687269464')
account1=Account(customer1, 'SNSB234109783876', 0)

account1.deposit(250)
account1.money_check(290)
account1.display_balance()
account1.deposit(50)
account1.money_check(290)
account1.display_balance()
print(account1.balance)
