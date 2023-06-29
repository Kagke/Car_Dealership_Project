class Car:
    def __init__(self, make, model, stock_quantity, buying_cost, selling_price, manufacturer, id = None):
        self.make = make
        self.model = model
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.manufacturer = manufacturer
        self.id = id
        
    
    def get_profit(self):
        return self.selling_price - self.buying_cost
