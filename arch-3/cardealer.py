class Car:
    def __init__(self, brand, color, model, price):
        self.brand = brand
        self.color = color
        self.model = model
        self.price = price
        self.sold = False
        self.sold_to = ''

    def sell(self, Customer):
        self.sold = True

        if Customer:
            self.sold_to = Customer

        return

    def print(self):
        car_info = {
            'Brand': self.brand,
            'Color': self.color,
            'Model': self.model,
            'Price': self.model,
            'Sold': [
                self.sold,
                self.sold_to
            ]
        }

        print(car_info)


class Customer:
    def __init__(self, name, age=0):
        self.firstName = name.split(' ')[0]
        self.lastName = name.split(' ')[1]
        self.age = age

    def print(self):
        customer = {
            'First name': self.firstName,
            'Last name': self.lastName,
            'Age': self.age
        }

        print(customer)


class Motorcycle():
    def __init__(self, brand, color, model, price):
        self.brand = brand
        self.color = color
        self.model = model
        self.price = price
        self.sold = False
        self.sold_to = ''

    def sell(self, Customer):
        self.sold = True

        if Customer:
            self.sold_to = f'{Customer.firstName} {Customer.lastName}'

        return

    def print(self):
        motorcycle_info = {
            'Brand': self.brand,
            'Color': self.color,
            'Model': self.model,
            'Price': self.model,
            'Sold': [
                self.sold,
                self.sold_to
            ]
        }

        print(motorcycle_info)


def startApp():
    return


if __name__ == '__main__':
    startApp()
