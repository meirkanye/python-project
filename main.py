from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

menu = [
    {'id': 1, 'name': 'Espresso', 'price': 2.5},
    {'id': 2, 'name': 'Latte', 'price': 3.0},
    {'id': 3, 'name': 'Cappuccino', 'price': 3.5}
]

orders = []


class Order(BaseModel):
    item_id: int
    quantity: int = 1
    total_price: float = 0

    def calculate_total_price(self):
        for item in menu:
            if item['id'] == self.item_id:
                return item['price'] * self.quantity
        return 0.0


@app.get('/menu', response_model=list)
async def get_menu():
    return menu


@app.get('/order', response_model=list)
async def get_orders():
    return orders


@app.post('/order', response_model=Order)
async def place_order(order: Order):
    item_id = order.item_id
    quantity = order.quantity

    new_order = Order(item_id=item_id, quantity=quantity)
    new_order.total_price = new_order.calculate_total_price()
    orders.append(new_order)

    return new_order



import uvicorn

uvicorn.run(app, host="127.0.0.1", port=8000)
