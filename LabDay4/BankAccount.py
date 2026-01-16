class BankAccount:

    # 1. Parameterized constructor
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print("Account created successfully")

    # 2. Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}")
            print("Current Balance:", self.balance)
        else:
            print("Invalid deposit amount")

    # 3. Withdraw method with validation
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")
            print("Current Balance:", self.balance)

    # 4. Destructor
    def __del__(self):
        print("BankAccount object is deleted")



acc1 = BankAccount(101,5000)
acc1.deposit(200)
acc1.withdraw(200)
acc1.deposit(200)
acc1.withdraw(10000)

