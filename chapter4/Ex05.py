class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print("Giá phải > 0")

    def __str__(self):
        return f"Price: {self._price}"

# test
p = Product(100)
print(p)

p.set_price(200)
print(p)