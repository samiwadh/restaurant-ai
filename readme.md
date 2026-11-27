# Restaurant AI

A small Python learning project built around a restaurant menu. It goes from Python basics to validated data models, and is meant to grow into an AI-powered restaurant backend.

## Project structure

| File | What it does |
|------|--------------|
| `basic.py` | Python fundamentals with menu examples: types, strings, lists, dictionaries, loops, functions, comprehensions, error handling, JSON, dataclasses, Pydantic, decorators, context managers, generators, `asyncio` and logging. |
| `menu_tools.py` | A small menu tool. It loads `menu.json`, validates each dish with Pydantic, filters dishes by allergen, works out the average price per category and finds the most expensive dishes. |
| `menu.json` | Menu data: each dish has a name, price, category and list of allergens. |
| `requirements.txt` | Python dependencies (Pydantic and the packages it needs). |

## Requirements

- Python 3.10 or newer
- The packages in `requirements.txt`

## Setup

```bash
git clone https://github.com/samiwadh/restaurant-ai.git
cd restaurant-ai
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run the menu tool:

```bash
python menu_tools.py
```

Example output:

```
INFO | Loaded 6 dishes
No gluten: ['Insalata', 'Grilled Salmon']
Avg price: {'Pizza': 8.5, 'Pasta': 11.75, 'Salad': 7.0, 'Dessert': 6.0, 'Main': 16.0}
Top 3: [('Grilled Salmon', 16.0), ('Carbonara', 12.0), ('Lasagna', 11.5)]
```

Run the Python basics walkthrough:

```bash
python basic.py
```

> Note: `basic.py` rewrites `menu.json` with its own sample menu when it runs.

Check code style with Ruff:

```bash
ruff check .
```

## Menu data format

Each dish in `menu.json` looks like this:

```json
{
  "name": "Margherita",
  "price": 8.5,
  "category": "Pizza",
  "allergens": ["gluten", "milk"]
}
```

Validation rules (in `menu_tools.py`):

- `name`: at least 2 characters
- `price`: greater than 0
- `category`: required
- `allergens`: optional list, empty by default

## Main functions

- `load_menu(path="menu.json")`: reads the JSON file and returns a list of validated `Dish` objects.
- `dishes_without(dishes, allergen)`: returns the names of dishes that do not contain the given allergen.
- `average_price_by_category(dishes)`: returns the average price for each category, rounded to 2 decimals.
- `most_expensive(dishes, n=3)`: returns the n most expensive dishes, highest price first.

## Roadmap

- REST API (for example with FastAPI) to serve the menu
- Database storage for dishes and orders
- An AI assistant that answers customer questions about the menu and allergens
