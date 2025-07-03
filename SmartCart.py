catalog = {
    "Vegetables": {
        1: ("Tomato", 20),
        2: ("Potato", 25),
        3: ("Carrot", 30),
        4: ("Onion", 22),
        5: ("Brinjal", 28)
    },
    "Fruits": {
        1: ("Apple", 100),
        2: ("Banana", 40),
        3: ("Grapes", 60),
        4: ("Mango", 120),
        5: ("Orange", 70)
    },
    "Groceries": {
        1: ("Rice", 60),
        2: ("Wheat Flour", 45),
        3: ("Salt", 20),
        4: ("Sugar", 35),
        5: ("Turmeric Powder", 15)
    },
    "Meat & Seafood": {
        1: ("Chicken", 250),
        2: ("Fish", 300),
        3: ("Mutton", 500),
        4: ("Prawns", 400),
        5: ("Crab", 450)
    },
    "Dairy Products": {
        1: ("Milk", 50),
        2: ("Butter", 80),
        3: ("Cheese", 90),
        4: ("Ghee", 120),
        5: ("Curd", 40)
    }
}

cart = []

def display_categories():
    print("\nAvailable Categories:")
    for idx, category in enumerate(catalog.keys(), start=1):
        print(f"{idx}. {category}")
    print(f"{len(catalog) + 1}. Finish Shopping & Show Final Bill")

def display_items(category):
    print(f"\nItems in {category}:")
    for item_no, (item_name, price) in catalog[category].items():
        print(f"{item_no}. {item_name} - ₹{price}")


while True:
    display_categories()
    try:
        choice = int(input("\nSelect a category by number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == len(catalog) + 1:
        break 

    category_list = list(catalog.keys())
    if 1 <= choice <= len(category_list):
        selected_category = category_list[choice - 1]

        while True:  # Stay in same category until user says no
            display_items(selected_category)
            try:
                item_no = int(input("Enter item number to add to cart: "))
                quantity = int(input("Enter quantity: "))
                item_name, price = catalog[selected_category][item_no]
                cart.append((item_name, price, quantity))
                print(f"Added {quantity} x {item_name} to cart.")
            except (ValueError, KeyError):
                print("Invalid item number or quantity.")
                continue

            same_category = input("Want to buy another item from the same category? (yes/no): ").strip().lower()
            if same_category != "yes":
                break  # Exit to category selection
    else:
        print("Invalid choice. Try again!")

# Final Bill Display
print("\nFinal Bill Summary:")
total = 0
for name, price, qty in cart:
    subtotal = price * qty
    print(f"{name} x {qty} = ₹{subtotal}")
    total += subtotal

#  Apply discount
discount = 0
if total > 1000:
    discount = total * 0.10
elif total > 500:
    discount = total * 0.05

final_amount = total - discount

print(f"\nTotal: ₹{total}")
print(f"Discount Applied: ₹{int(discount)}")
print(f"Final Amount to Pay: ₹{int(final_amount)}")
print("\nThank you for shopping with SmartCart!")