import json
import os

from typing import Any
from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    full_path = os.path.abspath(path)
    with open(full_path, encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: dict) -> list:
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    raw_data = read_json("..\\data\\products.json")
    categories_data = create_objects_from_json(raw_data)
    print(categories_data)

    print(categories_data[0].name)
    print(categories_data[0].description)
    print(categories_data[0].products)
