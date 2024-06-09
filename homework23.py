class Vehicle:
    vehicle_type = 'none'


class Car:
    price = 1000000

    def horse_powers(self):
        return '150 HP'


class Nissan(Vehicle, Car):
    price = 1500000
    vehicle_type = 'Medium-sized cars'

    def horse_powers(self):
        return '175 HP'


nissan = Nissan()
print(f'Класс автомобиля: {nissan.vehicle_type}\n'
      f'Цена: {nissan.price}')
