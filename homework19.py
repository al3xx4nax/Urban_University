class Building:

    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.buildingType == other.buildingType and self.numberOfFloors == other.numberOfFloors


ostankino_tower = Building(120, "Television and radio building")
evolution_tower = Building(55, "Bussiness Building")

print(ostankino_tower == evolution_tower)

ostankino_tower.numberOfFloors = 55
ostankino_tower.buildingType = "Bussiness Building"

print(ostankino_tower == evolution_tower)