# Dictionary to store expenses categorized by type
categories = {
    1: 'Food',
    2: 'Transportation',
    3: 'Entertainment',
    4: 'Utilities',
    5: 'Other'
}

expenses = {category: [] for category in categories.values()}

# Dictionary to store money transactions
balance = {}

# Function to add an expense
def add_expense():
    print("Expense Categories:")
    for num, category in categories.items():
        print(f"{num}. {category}")

    category_num = int(input("Enter expense category number: "))
    if category_num in categories:
        category = categories[category_num]
        amount = float(input("Enter expense amount: "))
        expenses[category].append(amount)
        print(f"\nExpense of ₹{amount} added to {category}!")
    else:
        print("\nInvalid category number!")

# Function to add money lending or receiving
def money_transaction():
    person = input("Enter person's name: ")
    if person not in balance:
        balance[person] = 0

    transaction_type = input("Enter 'lend' or 'receive': ")
    if transaction_type == 'lend':
        amount = float(input("Enter amount to lend: "))
        balance[person] -= amount
        print(f"\nYou lent ₹{amount} to {person}.")
    elif transaction_type == 'receive':
        amount = float(input("Enter amount to receive: "))
        balance[person] += amount
        print(f"\nYou received ₹{amount} from {person}.")
    else:
        print("\nInvalid transaction type!")

# Function to calculate total expenses and display all expenditures
def calculate_total_expenses():
    total = 0
    print("\nExpenditures by Category:")
    for category, expense_list in expenses.items():
        category_total = sum(expense_list)
        print(f"{category}: ₹{category_total:.2f}")
        total += category_total
    print(f"\nTotal Expenses: ₹{total:.2f}")
    return total

# Function to display lending and receiving transactions and its total
def display_balance():
    print("\nBalance:")
    total_balance = 0
    for person, amount in balance.items():
        print(f"{person}: ₹{amount:.2f}")
        total_balance += amount
    print(f"Total Balance: ₹{total_balance:.2f}")

# Main loop for the expense tracker and money flow transactions
while True:
    print("\n===== Expense & Money Flow Manager =====")
    print("1. Expense Input")                           #Add Expense
    print("2. Expense Summary")                         #View Total Expenses
    print("3. Credit & Debit Hub")                      #Add Money (Lender/Receiver)
    print("4. Credit & Debt Summary")                   #View Balance (Lender/Receiver)
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        calculate_total_expenses()
    elif choice == '3':
         money_transaction()
    elif choice == '4':
        display_balance()
    elif choice == '5':
        print("\nExiting...")
        break
    else:
        print("\nInvalid choice. Please enter a number from 1 to 5.")
