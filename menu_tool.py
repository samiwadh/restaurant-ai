menu = [    {"name": "Margherita", "price": 8.5, "category": "Pizza", "allergens": ["gluten", 
"milk"]},
{"name": "Carbonara",  "price": 12.0, "category": "Pasta", "allergens": ["gluten", 
"egg", "milk"]},
{"name": "Insalata",   "price": 7.0, "category": "Salad", "allergens": []},
{"name": "Chicken",   "price": 7.0, "category": "Salad", "allergens": []},
{"name": "Fish soup",   "price": 7.0, "category": "Salad", "allergens": []},
{"name": "Meat",   "price": 7.0, "category": "Salad", "allergens": []},
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




import json, logging
from pathlib import Path
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger(__name__)

class Dish(BaseModel):
    name: str = Field(min_length=2)
    price: float = Field(gt=0)
    category: str
    allergens: list[str] = []
def load_menu(path: str = "menu.json") -> list[Dish]:
    rows = json.loads(Path(path).read_text())
    dishes = [Dish(**r) for r in rows]
    log.info("Loaded %d dishes", len(dishes))
    return dishes

def dishes_without(dishes: list[Dish], allergen: str) -> list[str]:
    return [d.name for d in dishes if allergen.lower() not in d.allergens]
def average_price_by_category(dishes: list[Dish]) -> dict[str, float]:
    totals: dict[str, list[float]] = {}
    for d in dishes:
        totals.setdefault(d.category, []).append(d.price)
    return {c: round(sum(p) / len(p), 2) for c, p in totals.items()}
if __name__ == "__main__":
    menu = load_menu()
print("No gluten:", dishes_without(menu, "gluten"))
print("Avg price:", average_price_by_category(menu))