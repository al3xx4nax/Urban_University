class AgeError(Exception):
    pass


class GenderError(Exception):
    pass


class SmallAgeError(Exception):
    pass


def person(age, gender):
    if not isinstance(age, int) or age <= 0 or age > 100:
        raise AgeError('Неверно введён возраст!', 'Введите целое число от 1 до 100')
    if age < 18:
        raise SmallAgeError('Вы еще не достигли избирательного возраста!')
    if gender != 'мужчина' and gender != 'женщина':
        raise GenderError('Неверно указан пол!', 'Введите свой пол по примеру: "мужчина" или "женщина"')
    print(f' \tИзбиратель: \nВозраст: {age} \nПол: {gender}')


try:
    person(20, 'женщина')
except AgeError as a:
    print(a)
    raise
except SmallAgeError as b:
    print(b)
    raise
except GenderError as c:
    print(c)
    raise
