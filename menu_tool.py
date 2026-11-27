menu = [    {"name": "Margherita", "price": 8.5, "category": "Pizza", "allergens": ["gluten", 
"milk"]},
{"name": "Carbonara",  "price": 12.0, "category": "Pasta", "allergens": ["gluten", 
"egg", "milk"]},
{"name": "Insalata",   "price": 7.0, "category": "Salad", "allergens": []},
]
print(menu[0]["name"])              
# first dish's name
print(len(menu))                    
# number of dishes
menu.append({"name": "Tiramisu", "price": 6.0, "category": "Dessert",
"allergens": ["egg", "milk", "gluten"]})
print([d["name"] for d in menu])    
# all names
all_allergens = set()
for d in menu:
    all_allergens.update(d["allergens"])
print(sorted(all_allergens))