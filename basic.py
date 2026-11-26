name = "Margherita"        
price = 8.5                
quantity = 2               
# str
# float
# int
vegetarian = True          
# bool
note = None                
# "no value"
print(type(name), type(price), type(quantity), type(vegetarian), type(note))
print(price * quantity)



dish = "carbonara" 
price = 12
print(f"{dish.title()} costs EUR {price:.2f}")
print(dish.upper(), len(dish), dish.replace("a", "@"))
print("gluten,milk".split(","))
print(", ".join(["gluten", "milk"]))
print("  extra spaces  ".strip())
print("  extra spaces  ".lstrip())
print("  extra spaces  ".rstrip())
print("  extra spaces  ".strip().upper())
print("  extra spaces  ".strip().replace(" ", "_"))