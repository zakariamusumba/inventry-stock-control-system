from product import Product
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self):
        product_id = input("Enter product ID: ").strip()

        if not product_id:
            print("Product ID cannot be blank.")
            return

        if product_id in self.products:
            print("Error: Product ID already exists.")
            return

        name = input("Enter product name: ").strip()

        if not name:
            print("Product name cannot be blank.")
            return

        category = input("Enter product category: ").strip()

        if not category:
            print("Category cannot be blank.")
            return

        try:
            unit_price = float(input("Enter unit price: "))
            quantity = int(input("Enter quantity: "))

            if unit_price < 0:
                print("Price cannot be negative.")
                return

            if quantity < 0:
                print("Quantity cannot be negative.")
                return

            product = Product(
                product_id, name, category, unit_price, quantity
            )

            self.products[product_id] = product

            print("Product added successfully!")

        except ValueError:
            print("Invalid input. Enter a valid price and quantity.")

    def view_products(self):
        if not self.products:
            print("No products available.")
            return

        print("\n========== ALL PRODUCTS ==========")

        for product in self.products.values():
            product.display_product()

        self.total_stock_value()

    def search_product(self):
        product_id = input("Enter product ID to search: ").strip()

        product = self.products.get(product_id)

        if product:
            product.display_product()
        else:
            print("Product not found.")

    def update_quantity(self):
        product_id = input("Enter product ID: ").strip()

        product = self.products.get(product_id)

        if not product:
            print("Product not found.")
            return

        try:
            quantity = int(input("Enter new quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative.")
                return

            product.quantity = quantity

            print("Product quantity updated successfully!")

            if product.quantity < 5:
                print("WARNING: Low stock! Reorder this product.")

        except ValueError:
            print("Invalid quantity. Enter a whole number.")

    def record_sale(self):
        product_id = input("Enter product ID: ").strip()

        product = self.products.get(product_id)

        if not product:
            print("Product not found.")
            return

        try:
            quantity_sold = int(input("Enter quantity sold: "))

            if quantity_sold <= 0:
                print("Sale quantity must be greater than zero.")
                return

            if quantity_sold > product.quantity:
                print("Insufficient stock!")
                print(f"Available stock: {product.quantity}")
                return

            total = quantity_sold * product.unit_price

            product.quantity -= quantity_sold

            print("\n========== SALES RECEIPT ==========")
            print(f"Product: {product.name}")
            print(f"Quantity Sold: {quantity_sold}")
            print(f"Unit Price: Ksh {product.unit_price:.2f}")
            print(f"Total Sale: Ksh {total:.2f}")
            print(f"Remaining Stock: {product.quantity}")

            if product.quantity < 5:
                print("WARNING: Low stock! Reorder this product.")

        except ValueError:
            print("Invalid input. Enter a valid whole number.")

    def total_stock_value(self):
        total_value = sum(
            product.calculate_stock_value()
            for product in self.products.values()
        )

        print("\n========== STOCK VALUE ==========")
        print(f"Total Stock Value: Ksh {total_value:.2f}")

    def menu(self):
        while True:
            print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")
            print("1. Add Product")
            print("2. View All Products")
            print("3. Search Product")
            print("4. Update Product Quantity")
            print("5. Record Sale")
            print("6. Calculate Total Stock Value")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ").strip()

            if choice == "1":
                self.add_product()

            elif choice == "2":
                self.view_products()

            elif choice == "3":
                self.search_product()

            elif choice == "4":
                self.update_quantity()

            elif choice == "5":
                self.record_sale()

            elif choice == "6":
                self.total_stock_value()

            elif choice == "7":
                print("Thank you for using the Inventory Management System!")
                break

            else:
                print("Invalid choice. Please select between 1 and 7.")	