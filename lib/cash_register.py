#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")

    def add_item(self, title, price, quantity=1):
        item_total = price * quantity
        self.total += item_total
        for _ in range(quantity):
            self.items.append(title)
            
        self.previous_transactions.append({
            "item": title,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount:
            self.total -= self.total * (self.discount / 100)

            display_total = int(self.total) if self.total == int(self.total) else self.total
            print(f"After the discount, the total comes to ${display_total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.previous_transactions:
            last_transaction = self.previous_transactions.pop()
            item_total = last_transaction["price"] * last_transaction["quantity"]

            self.total -= item_total

            for _ in range(last_transaction["quantity"]):
                self.items.remove(last_transaction["item"])
        else:
            print("There is no transaction to void.")