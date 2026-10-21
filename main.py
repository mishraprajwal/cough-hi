from fastapi import FastAPI

app = FastAPI(title="Coffee Shop API")

MENU = [
    {"id": 1, "name": "Latte", "price": 4.50},
    {"id": 2, "name": "Cappuccino", "price": 4.25},
    {"id": 3, "name": "Cold Brew", "price": 3.95},
    {"id": 4, "name": "Americano", "price": 3.25},
]


@app.get("/menu")
def get_menu():
    return MENU