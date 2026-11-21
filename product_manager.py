
class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            product.display_info()
            print("--------------------")

    def total_inventory_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total
    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"{product_name} has been removed.")
                return
        print(f"{product_name} not found.")