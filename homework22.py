class Car:
    price = 1000000

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)

    def hourse_powers(self):
        return '75 HP'


class Nissan(Car):
    def hourse_powers(self):
        return '175 HP'


class Kia(Car):
    def hourse_powers(self):
        return '125 HP'


my_car = Car('2107')
print(my_car)
print('Цена:', my_car.price, '₽')
print('Мощность (л/с):', my_car.hourse_powers())

kia = Kia(model='K5')
print(kia)
kia.price = 1800000
print('Цена:', kia.price, '₽')
print('Мощность (л/с):', kia.hourse_powers())


nissan = Nissan(model='X-Trail')
print(nissan)
nissan.price = 1550000
print('Цена:', nissan.price, '₽')
print('Мощность (л/с):', nissan.hourse_powers())