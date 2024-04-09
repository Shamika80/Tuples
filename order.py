def process_orders(orders):
 
  for customer_name, product, quantity in orders:
    print(f"{customer_name} ordered {quantity} {product}(s).")

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Phone", 3),
]

process_orders(orders)