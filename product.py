class Product:
    def __init__(self, product_id, name, category, unit_price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.unit_price = unit_price
        self.quantity = quantity

    def display_product(self):
        print("\n--- Product Details ---")
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Unit Price: Ksh {self.unit_price:.2f}")
        print(f"Quantity in Stock: {self.quantity}")

        if self.quantity < 5:
            print("WARNING: Low stock! Reorder this product.")

    def calculate_stock_value(self):
        return self.unit_price * self.quantity