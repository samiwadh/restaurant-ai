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

# List
menu = ["Margherita", "Carbonara", "Bolognese"]
print(menu)
print(menu[0])
print(menu[-1])
print(len(menu))

##dictionary in to list ##
"/n "
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


for dish in menu:
    if dish["price"] > 10:
        label = "premium"
    elif dish["price"] > 7:
        label = "standard"  
    else:
        label = "economical"
    print(f"{dish['name']:<12} {label}")
    
    
def dishes_without(menu: list[dict], allergen: str) -> list[str]:
    """Return the names of dishes that do NOT contain the allergen."""
    return [d["name"] for d in menu if allergen not in d["allergens"]]

def price_with_vat(price: float, vat: float = 0.10) -> float:
    return round(price * (1 + vat), 2)

print(dishes_without(menu, "gluten"))
print(price_with_vat(8.5))            
# default VAT 10%
print(price_with_vat(8.5, vat=0.22))  # keyword argument

"1.6 Comprehensions, sorting, enumerate ,zip"
cheap = [d["name"] for d in menu if d["price"] < 10]
price_by_name = {d["name"]: d["price"] for d in menu}
print(cheap)
print(price_by_name)

by_price = sorted(menu, key=lambda d: d["price"], reverse=True)
for i, d in enumerate(by_price, start=1):
    print(i, d["name"], d["price"])

names = ["A", "B"]; prices = [5, 7]
print(list(zip(names, prices)))



#Backend code must never crash on bad input. It catches the error and returns a clear message.
def get_price(menu: list[dict], name: str) -> float:
    for d in menu:
        if d["name"].lower() == name.lower():
            return d["price"]
    raise ValueError(f"Dish '{name}' not found")
try:
    print(get_price(menu, "carbonara")) 
    print(get_price(menu, "sushi"))
except ValueError as e:
    print("Error:", e)
finally:
    print("done")
    
    
    
# import json file 
import json
from pathlib import Path
path = Path("menu.json")
path.write_text(json.dumps(menu, indent=2))      
# save
loaded = json.loads(path.read_text())            
# load
print(type(loaded), len(loaded), loaded[1]["name"])
print(json.dumps(loaded[0]))



from dataclasses import dataclass, field

@dataclass
class Dish:
    name: str
    price: float
    category: str
    allergens: list[str] = field(default_factory=list)
    
    def contains(self, allergen: str) -> bool:
        return allergen in self.allergens
    def discounted(self, pct: float) -> float:
        return round(self.price * (1 - pct), 2)
    
d = Dish("Margherita", 8.5, "Pizza", ["gluten", "milk"])
print(d)
print(d.contains("milk"), d.discounted(0.2))
dishes = [Dish(**row) for row in menu] # dicts -> objects      
print(dishes[1].name, dishes[1].price)



from pydantic import BaseModel, Field, ValidationError
class DishIn(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: float = Field(gt=0, le=200)
    category: str
    allergens: list[str] = []
ok = DishIn(name="Lasagna", price="11.5", category="Pasta")   # "11.5" converted to float
print(ok)
print(ok.model_dump())          
# -> dict
print(ok.model_dump_json())     
# -> JSON text
try:
    DishIn(name="X", price=-3, category="Pasta")
except ValidationError as e:
    for err in e.errors():
        print(err["loc"], err["msg"])
        
        
        
        
        
        
        

import time
from functools import wraps
def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper
@timed
def slow_sum(n: int) -> int:
    return sum(range(n))
print(slow_sum(1_000_000))

# a "registering" decorator, like FastAPI's router

ROUTES = {}

def route(path):
    def register(func):
        ROUTES[path] = func
    return register
@route("/hello")
def hello():
    return {"msg": "hi"}
print(ROUTES["/hello"]())


from contextlib import contextmanager
@contextmanager
def fake_db_session():
    print("open session")
    try:
        yield {"connected": True}
    finally:
        print("close session")
with fake_db_session() as s:
    print("using", s)
def batches(items, size):
    for i in range(0, len(items), size):
        yield items[i:i + size]
for b in batches(list(range(7)), 3):
    print(b)