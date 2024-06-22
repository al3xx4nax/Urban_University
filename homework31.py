def create_operation(operation):
    if operation == 'multiplication':
        def multiplication(x, y):
            return x * y

        return multiplication
    elif operation == 'division':
        def division(x, y):
            if y == 0:
                return 'Error: Division by zero'
            else:
                return x // y

        return division


my_func_div = create_operation("division")
my_func_multiply = create_operation("multiplication")

square = lambda x: x * x


class Rect:
    def __init__(self, a, b):
        self.value_1 = a
        self.value_2 = b

    def __call__(self):
        return self.value_1 * self.value_2


rect = Rect(2, 4)

print(f'\tЗадание 1: Фабрика функций\n'
      f'6 / 2 = {my_func_div(6, 2)}\n'
      f'6 / 3 = {my_func_div(6, 3)}\n'
      f'6 / 0 = {my_func_div(6, 0)}\n'
      f'3 * 2 = {my_func_multiply(3, 2)}\n'
      f'3 * 3 = {my_func_multiply(3, 3)}\n'
      f'3 * 0 = {my_func_multiply(3, 0)}')
print(f'\tЗадание 2: Лямбда\n'
      f'Квадрат числа 12 = {square(12)}\n'
      f'Квадрат числа 16 = {square(16)}\n'
      f'Квадрат числа 25 = {square(25)}')
print(f'\tЗадание 3: Вызываемые объекты\n'
      f'Стороны: {rect.value_1}, {rect.value_2}\n'
      f'Площадь: {rect()}')
