#HackerRank - Vending Machine

class VendingMachine:
        
    def __init__ (self, num_items, items_price):
        self.items = num_items
        self.price = items_price
    
    def buy(self, req_items, money):
        
        self.req_items = req_items
        self.money = money
        
        total_cost = req_items * self.price
        
        
        if req_items > self.items:
            message = 'Not enough items in the machine'
            return message
        elif total_cost > money:
            message = 'Not enough coins'
            return message
        elif money > total_cost:
            items_buyed = money - (req_items * self.price)
            return items_buyed
            
maquina = VendingMachine(10, 2)

print(maquina.buy(10, 100))

print(maquina.buy(9, 15))

print(maquina.buy(5, 20))

print(maquina.buy(15, 100))