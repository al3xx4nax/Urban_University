class House:
    def __init__(self, numberOfFloors):
        self.floors = None
        self.numberOfFloors = numberOfFloors

    def setNewNumberOfFloors(self, floors):
        self.floors = floors
        self.numberOfFloors = self.floors
        print(self.numberOfFloors)


house = House(0)
house.setNewNumberOfFloors(10)
