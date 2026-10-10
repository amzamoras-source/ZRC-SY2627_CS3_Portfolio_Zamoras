
# Create a BankAccount class with attributes that can be accessed and updated through
# methods.

# Goal: Apply the concept of Encapsulation by designing a BankAccount class that protects its
# data and controls access and modification.
# Role: You are a junior software developer hired by a bank to create a secure bank account
# system. Your task is to make sure sensitive information is properly protected.
# Audience: Your work will be reviewed by your teacher (as the lead developer)
# Situation: A bank wants to digitize its account management system. However, they are
# concerned about security and data integrity.
# They need a BankAccount class that:
# Protects the account number:
# Prevents negative balances
# Allows controlled access through methods
# You must design the class in accordance with proper encapsulation principles.


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_balance(self, balance):
        if balance < 0:
            print("The balance must not be a negative number.")
        else:
            self.__balance = balance

    @property
    def get_account_number(self):
        return self.__account_number

    @property
    def get_balance(self):
        return self.__balance


a1 = BankAccount(12345, 1000)

print("Account 1")
print("Account Number:", a1.get_account_number)
print(f"Balance: {a1.get_balance:.2f}")

print("\nUpdate balance to -100")
a1.set_balance(-100)

print("Account Number:", a1.get_account_number)
print(f"Balance: {a1.get_balance:.2f}")
