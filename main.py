import random
from product import Product
from product_manager import ProductManager
from cart import Cart

# Creating product manager
manager = ProductManager()

# Creating products
product1 = Product("Laptop", 85000, 5)
product2 = Product("Smartphone", 60000, 10)
product3 = Product("Headphones", 8000, 15)
product4 = Product("Keyboard", 4500, 8)

# Adding products to inventory
manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.add_product(product4)

# Displaying all products
print("AVAILABLE PRODUCTS:")
manager.display_products()

# Displaying total inventory value
print("Total inventory value:", manager.total_inventory_value(), "RSD")
# Removing a product
manager.remove_product("Keyboard")

# Displaying updated products
print("UPDATED PRODUCT LIST:")
manager.display_products()
# Creating shopping cart
cart = Cart()

# Randomly selecting three products
selected_products = random.sample(manager.products, 3)

# Adding selected products to cart
for product in selected_products:
    cart.add_to_cart(product)

# Displaying cart contents
print("\nSHOPPING CART:")
cart.display_cart()

# Displaying total cart value
print("Total cart value:", cart.calculate_total(), "RSD")
