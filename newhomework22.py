class Car:
    price = 1000000

    def horse_powers(self):
        return '175 HP'


class Nissan(Car):
    price = 1500000

    def horse_powers(self):
        return '249 HP'


class Kia(Car):
    price = 2300000

    def horse_powers(self):
        return '199 HP'


car = Car()
print('..::Car::..')
print(f'Цена: {car.price}')
print(f'Кол-во лошадиных сил: {car.horse_powers()}')

nissan = Nissan()
print('..::Nissan::..')
print(f'Цена: {nissan.price}')
print(f'Кол-во лошадиных сил: {nissan.horse_powers()}' )

kia = Kia()
print('..::KIA::..')
print(f'Цена: {kia.price}')
print(f'Кол-во лошадиных сил: {kia.horse_powers()}')
