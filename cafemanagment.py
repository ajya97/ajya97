def show_menu(menu):
    print("\n**** MENU ****")
    for item, price in menu.items():
        print(item, "->", price, "rs")

def order(menu):
    total_order = 0
    while True:
        order_item = input("Enter the Name of item you want to order = ").title()
        if order_item in menu:
            total_order += menu[order_item]
            print(f"Your item {order_item} has been added to your order")
        else:
            print(f"Ordered item {order_item} is not available yet!")
            show_menu(menu)

        another_item = input("Do you want to add another item? (Yes/No): ").lower()
        if another_item != "yes":
            break
    return total_order

def add_item(menu, item, price):
    menu[item] = price

def remove_item(menu, item):
    if item in menu:
        del menu[item]
    else:
        print("Item not found in menu")

def update_item(menu, item, price):
    if item in menu:
        menu[item] = price
    else:
        print("Item not found in menu")

def update_menu(menu):
    password = input("Enter the password to update the menu = ")
    if password == "password":
        while True:
            print("Add item in Menu -> 1")
            print("Remove item in Menu -> 2")
            print("Update item in Menu -> 3")
            print("Show Menu -> 4")
            print("Exit to the update menu -> 5")
            choice = int(input("Enter your choice = "))
            match choice:
                case 1:
                    item = input("Enter the name of item = ")
                    price = int(input("Enter the price of item = "))
                    add_item(menu, item, price)
                case 2:
                    item = input("Enter the name of item = ")
                    remove_item(menu, item)
                case 3:
                    item = input("Enter the name of item = ")
                    price = int(input("Enter the price of item = "))
                    update_item(menu, item, price)
                case 4:
                    show_menu(menu)
                case 5:
                    break
                case _:
                    print("Invalid Choice")
    else:
        print("Invalid Password")

def main():
    menu = {"Hot Coffee": 59, "Black Coffee": 69, "Cold Cream Coffee": 79, "Special Coffee": 89, "Chocolate Coffee": 99}
    while True:
        print("Welcome to the Cafe")
        print("Order -> 1")
        print("Update Menu -> 2")
        choice = int(input("Enter your choice = "))
        match choice:
            case 1:
                print("\n\n\n")
                show_menu(menu)
                total_order = order(menu)
                print(f"Total Amount of your order is {total_order} rs")
                print("Thank You for Ordering\n\n")
            case 2:
                update_menu(menu)

if __name__ == "__main__":
    main()
