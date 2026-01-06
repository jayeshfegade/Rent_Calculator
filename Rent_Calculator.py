print("===== Rent Calculator =====")

try:
    # Inputs
    rent = int(input("Enter your flat rent :- "))
    grocery = int(input("Enter the amount of grocery ordered :- "))
    electricity_bill = int(input("Enter the total of electricity bill :- "))
    people = int(input("Enter the number of people living in hostel or room :- "))

    # Validation
    if people <= 0:
        print("❌ Error: Number of people must be greater than 0")
    else:
        # Calculations
        total_expense = rent + grocery + electricity_bill
        per_person = total_expense / people

        # Output
        print("\n____________ Expense Summary ___________")
        print("Total Rent:           ₹", rent)
        print("Grocery:              ₹", grocery)
        print("Electricity Bill:     ₹", electricity_bill)
        print("----------------------------------------")
        print("Total Expense:        ₹", total_expense)
        print("Each person will pay: ₹", round(per_person, 2))
        print("________________________________________")
        print("Thank you! Split expenses easily 😊")

except ValueError:
    print("❌ Error: Please enter numbers only (no letters or symbols)")
