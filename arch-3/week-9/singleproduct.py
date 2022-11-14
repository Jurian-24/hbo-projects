if __name__ == '__main':
    print()

class Product():
    def __init__(self, name, amount, price):
        self.productName = name
        self.amount = amount
        self.price = price

    def get_price(self, amount_in_cart):
        total_price = amount_in_cart * self.price

        if amount_in_cart < 10:
            total_price = total_price
        elif 10 <= amount_in_cart < 99:
            total_price = float(total_price) * 0.9
        elif amount_in_cart >= 100:
            total_price = float(total_price) * 0.8
        else:
            print('peielemuis')
        return total_price

    def make_purchase(self, amount_in_cart):
        self.amount -= int(amount_in_cart)
        return
