# Define the inventory dictionary
inventory = {}

# Function to add or update a product
def add_update_product(name, price, quantity):
    inventory[name] = {'price': price, 'quantity': quantity}
    print(f"Product {name} added/updated successfully.")

# Function to remove a product
def remove_product(name):
    if name in inventory:
        del inventory[name]
        print(f"Product {name} removed successfully.")
    else:
        print(f"Product {name} does not exist in the inventory.")

# Function to display the inventory
def display_inventory():
    if inventory:
        print("\nCurrent Inventory:")
        for name, details in inventory.items():
            print(f"Name: {name}, Price: {details['price']}, Quantity: {details['quantity']}")
    else:
        print("Inventory is empty.")

# Main menu
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add/Update Product")
        print("2. Remove Product")
        print("3. Display Inventory")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            add_update_product(name, price, quantity)
        elif choice == '2':
            name = input("Enter product name to remove: ")
            remove_product(name)
        elif choice == '3':
            display_inventory()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main function
if __name__ == "__main__":
    main()
