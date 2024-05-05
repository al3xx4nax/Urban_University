class House:
    def __init__(self):
        self.numberOfFloors = 10


house = House()
floor = 0
for i in range(house.numberOfFloors):
    i = floor
    floor += 1
    print('Текущий этаж', floor)
