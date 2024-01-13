import datetime

# Initialize empty dictionary to store expenses
expenses = {}

# Function to add an expense
def add_expense():
    category = input("Enter expense category (e.g., food, transportation, entertainment): ")
    amount = float(input("Enter expense amount: "))
    description = input("Enter a brief description: ")
    
    date = datetime.date.today().strftime("%Y-%m-%d")
    
    if category in expenses:
        expenses[category].append({"date": date, "amount": amount, "description": description})
    else:
        expenses[category] = [{"date": date, "amount": amount, "description": description}]
    
    print("Expense added successfully!")

# Function to display expenses
def display_expenses():
    print("\nExpense Tracker:")
    for category, entries in expenses.items():
        print(f"\nCategory: {category}")
        for entry in entries:
            print(f"Date: {entry['date']}, Amount: ${entry['amount']}, Description: {entry['description']}")

# Function to display monthly summary
def display_monthly_summary():
    month = input("Enter the month (format: MM) to view summary: ")
    
    total_expense = 0
    for category, entries in expenses.items():
        for entry in entries:
            if entry['date'][5:7] == month:
                total_expense += entry['amount']
    
    print(f"\nMonthly Summary for {datetime.date(1900, int(month), 1).strftime('%B %Y')}:")
    print(f"Total Expenses: ${total_expense}")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add Expense")
    print("2. Display Expenses")
    print("3. Monthly Summary")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_expense()

    elif choice == '2':
        display_expenses()

    elif choice == '3':
        display_monthly_summary()

    elif choice == '4':
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")