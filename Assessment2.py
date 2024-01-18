#  Here the Vending machine items and prices are mentioned
chips:['Oman chips(1):1.25','Sohar Chips(2):1.50','Lays Max(3)1.50']
Drinks:['Pepsi(4):1.50','Cola(5):1.50','Dew(6):1.50']
Choclates:['kinder Bruno(7):1.50','Flake(8):1.50','KitKat(9):2.00','Snickers(10):1.00']

def vending_machine():
    items = {
        '1': {'Name': 'Oman Chips', 'price': 1.25},
        '2': {'Name': 'Sohar Chips', 'price': 1.50},
        '3': {'Name': 'Lays Max', 'price': 1.50},
        '4': {'Name': 'Pepsi', 'price': 1.50},
        '5': {'Name': 'Cola', 'price': 1.50},
        '6': {'Name': 'Dew', 'price': 1.50},
        '7': {'Name': 'Kinder Bruno', 'price': 1.50},
        '8': {'Name': 'Flake', 'price': 1.50},
        '9': {'Name': 'KitKat', 'price': 2.00},
        '10': {'Name': 'Snickers', 'price': 1.00}
    }

# Display available items and prices And Welcome

    print()
    print("Welcome to icryp's Vending Machine!")
    print()
    print("Please select an item:")

    for Id, item in items.items():
        print(f"{Id}. {item['Name']} - {item['price']} AED")

# Ask the user for input

    select = input("Enter the item number you wish to purchase: ")

# Check if the selected item is valid

    print()
    if select in items:
        selected_item = items[select]
        print(f"You have selected {selected_item['Name']}.")
        total_amount = selected_item['price']
        print()

    # Ask The user to insert money

        while total_amount > 0:
            try:
                payment = float(input(f"Please insert {total_amount:.2f} AED: "))
                if payment >= total_amount:
                    change = payment - total_amount
                    print()
                    print(f"Thank you for your purchase. Your item is being dispensed, Your change is {change:.1f} AED.")
                    break
                else:
                    print("Insufficient Amount. Please insert more money.")
                    total_amount -= payment
            except ValueError:
                print("Unapproved payment amount. Please enter a valid number.")
    else:
        print("Invalid Choice. Please try again.")


# Call the function to make a purchase

vending_machine()

# Ask the user if they want to make another purchase

while True:
    try_again = input("Do you want to Buy another purchase? (yes/no): ").lower()
    if try_again == 'yes':
        vending_machine()
    elif try_again == 'no':
        print("Thank you for using icryp's Vending Machine. Goodbye!!")
        break
    else:
        print("Invalid input. Please enter")