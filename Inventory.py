class Product(object):

	def __init__(self, price, id, quantity):
		self.price = price
		self.id = id.capitalize()
		self.quantity = quantity

class Inventory(object):

	def __init__(self, products=[], value=0):
		self.products = products
		self.value = value

	def add_to_inv(self, product):
		self.products.append(product)

	def change_product_quantity(self, name, amount):
		for item in self.products:
			if name.capitalize() == item.id:
				item.quantity = amount

	def show_me(self):
		fmt = 'Name = {}, Price = {}, Quantity = {}'
		for product in self.products:
			print(fmt.format(product.id, product.price, product.quantity))

	def sum_value(self):
		total = 0
		for item in self.products:
			total += (item.price * item.quantity)
		self.value = total

inv = Inventory()

print("Welcome to your Product Inventory!")

while True:
	print("\nWhat would you like to do?\n",
			"\t1. Check current inventory\n",
			"\t2. Add new product to Inventory\n",
			"\t3. Change Quantity of Product\n"
			"\t4. Check current value of inventory\n"
			"\t5. Quit")

	inp = int(input())

	if inp == 1:
		inv.show_me()
	elif inp == 2:
		name = input("Name of Product: ")
		price = float(input("Price of Product: "))
		quantity = int(input("Quantity on hand: "))
		inv.add_to_inv(Product(price, name, quantity))
	elif inp == 3:
		prod = input("What product are we changing? ")
		new_quant = int(input("What is the new quantity? "))
		inv.change_product_quantity(prod, new_quant)
	elif inp == 4:
		inv.sum_value()
		print("Total value = $%0.2f" % inv.value)
	else: 
		break

print("Goodbye")


