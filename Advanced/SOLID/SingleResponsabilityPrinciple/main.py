class Item:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        
class Order:
    def __init__(self, order_id, items) -> None:
        self.order_id = order_id
        self.items = items
        
    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total
    
class OrderManager:
    def place_order(self, order):
        total = order.calculate_total()
        print(f'total is: {total}')


def main():
    order_items = [
        Item("p1", 1000),
        Item("p2", 2000),
        Item("p3", 3000)
    ]
    
    order = Order(123, order_items)
    order_manager = OrderManager()
    order_manager.place_order(order)
    
main()