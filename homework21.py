from random import randint, choice


class Buiding:
    total = 0

    def __init__(self, name):
        self.name = name
        self.numberOfFloors = randint(1, 21)
        self.buildingType = choice(['деревянное', 'бетонное', 'каменное', 'кирпичное'])
        Buiding.total += 1

    def __str__(self):
        list_ = list(map(lambda x, y: '\t' + str(x) + ' = ' + str(y) + '\n', self.__dict__.keys(),
                         self.__dict__.values()))
        return f'\n"{self.name}":\n' + ' '.join(list_)


buid_list = [Buiding('Здание №'+str(i)) for i in range(1, 41)]

print(*buid_list)
print('Общее количество зданий:', Buiding.total)