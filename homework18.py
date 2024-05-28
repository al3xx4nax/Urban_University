class House:
    def __init__(self, name, number_of_floors):
            self.name = name
            self.number_of_floors = number_of_floors


def go_to():
    new_floor = int(input())
    if new_floor < 1 or new_floor > house.number_of_floors:
        print("Такого этажа не существует!")
    else:
        for i in range(1, new_floor + 1):
            print(i)


house = House("ЖК Румянцево-парк", 21)

go_to()