# ----- Inventory Management System -----

# Modules
import os
import json

# Classes
class Product:
    # Properties
    Product_ID = None
    Product_Name = None
    Product_Price = None
    Product_Quantity = None
    Product_Supplier = None

    # Constructor
    def __init__(self, p_id, p_name, p_price, p_quantity, p_supplier):
        self.Product_ID = p_id
        self.Product_Name = p_name
        self.Product_Price = p_price
        self.Product_Quantity = p_quantity
        self.Product_Supplier = p_supplier

class Inventory:
    # Properties
    Products = {}
    Low_Stock = 5

    # Methods
    def save_inventory(self, filename="inventory.json"):
        with open(filename, "w") as f:
            data = {pid: vars(pro_details) for pid, pro_details in self.Products.items()}
            json.dump(data, f, indent=4)
        print("\n✅ Inventory saved to file.")

    def load_inventory(self, filename="inventory.json"):
        if not os.path.isfile(filename):
            return
        with open(filename, "r") as f:
            data = json.load(f)
            for pid, data in data.items():
                obj_product = Product(data["Product_ID"], data["Product_Name"], data["Product_Price"], data["Product_Quantity"], data["Product_Supplier"])
                self.Products[pid] = obj_product

    def add_product(self, new_product):
            product_id = new_product.Product_ID

            if product_id in self.Products:
                print("\nProduct ID is already in inventory.")
                return

            self.Products[product_id] = new_product
            print(f"\nProduct '{new_product.Product_Name}' is added to inventory.")

    def update_product(self):
        if not self.Products:
            print("\nInventory is empty.")
            return

        print("\nInventory.")
        for product_details in self.Products.values():
            print(f"ID: {product_details.Product_ID} | Name: {product_details.Product_Name}")

        enter_id = input("\nEnter the ID of product you want to update: ")
        if enter_id in self.Products:
            existing_product = self.Products[enter_id]
            new_id = input("Enter the new product ID: ")
            new_name = input("Enter the new product name: ")
            new_price = input("Enter the new product price: ")
            new_quantity = input("Enter the new product quantity: ")
            new_supplier = input("Enter the new product supplier: ")
            updated_product = Product(new_id, new_name, new_price, new_quantity, new_supplier)
            if not new_id or not new_name or not new_price or not new_quantity or not new_supplier:
                print("\nInvalid Input! All Fields Required.")
                return

            if new_id != enter_id:
                del self.Products[enter_id]

            self.Products[new_id] = updated_product
            print(f"\nProduct '{new_name}' updated successfully!")

        else:
            print("\nProduct ID is not in inventory.")

    def remove_product(self):
        if not self.Products:
            print("\nInventory is empty.")
            return

        print("\nInventory.")
        for product_details in self.Products.values():
            print(f"ID: {product_details.Product_ID} | Name: {product_details.Product_Name}")

        enter_id = input("\nEnter the ID of product you want to remove: ")
        if enter_id in self.Products:
             del self.Products[enter_id]
             print(f"\nProduct '{enter_id}' removed successfully!")

        else:
            print("\nProduct ID is not in inventory.")

    def view_inventory(self):
        if not self.Products:
            print("\nInventory is empty.")
            return

        print("\nInventory:")
        for display_product in self.Products.values():
            print(f"\nProduct ID: {display_product.Product_ID}")
            print(f"Product Name: {display_product.Product_Name}")
            print(f"Product Price: {display_product.Product_Price}")
            print(f"Product Quantity: {display_product.Product_Quantity}")
            print(f"Product Supplier: {display_product.Product_Supplier}")
            print("------------------------------")

    def check_low_stock(self):
        if not self.Products:
            print("\nInventory is empty.")
            return

        found = False
        for product_details in self.Products.values():
            if int(product_details.Product_Quantity) < self.Low_Stock:
                if not found:
                    print("\nLow Stock Products:")
                print(f"Product ID: {product_details.Product_ID} | Name: {product_details.Product_Name} | Quantity: {product_details.Product_Quantity}")
                found = True

        if not found:
               print(f"\nAll products have sufficient stock.")

inventory = Inventory()
inventory.load_inventory()

try:
    while True:
        print("\n----- Welcome to Inventory Management System -----")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. View Inventory")
        print("5. Check Low Stock")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            p_id = input("\nEnter Product ID: ")
            p_name = input("Enter Product Name: ")
            p_price = input("Enter Product Price: ")
            p_quantity = input("Enter Product Quantity: ")
            p_supplier = input("Enter Product Supplier: ")
            if not p_id or not p_name or not p_price or not p_quantity or not p_supplier:
              print("\nInvalid Input! All Fields Required.")
              continue

            product = Product(p_id, p_name, p_price, p_quantity, p_supplier)
            inventory.add_product(product)
        elif choice == "2":
           inventory.update_product()
        elif choice == "3":
           inventory.remove_product()
        elif choice == "4":
           inventory.view_inventory()
        elif choice == "5":
           inventory.check_low_stock()
        elif choice == "0":
            print("\nSaving inventory before exit...")
            inventory.save_inventory()
            print("\nThank you for using Inventory Management System")
            exit()

        else:
           print("\nInvalid Choice. Please choose between 1-6")

except KeyboardInterrupt:
    print("\nSaving inventory before exit...")
    inventory.save_inventory()
    print("\n\nThank you for using Inventory Management System! Bye....")

