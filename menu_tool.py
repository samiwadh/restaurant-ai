import json
import logging
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


def most_expensive(dishes: list[Dish], n: int = 3) -> list[Dish]:
    """Return the n most expensive dishes, highest price first."""
    return sorted(dishes, key=lambda d: d.price, reverse=True)[:n]


if __name__ == "__main__":
    menu = load_menu()
    print("No gluten:", dishes_without(menu, "gluten"))
    print("Avg price:", average_price_by_category(menu))
    print("Top 3:", [(d.name, d.price) for d in most_expensive(menu)])