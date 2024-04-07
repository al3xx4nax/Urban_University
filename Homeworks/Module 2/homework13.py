def print_params(a=1, b='строка', c=True):
    print(a, b, c)


#1
print_params()
print_params(2, True, False)
print_params(a=1, b='строка', c=True)
print_params(a=1, b=25, c=True)
print_params(a=1, b='строка', c=[1,2,3])

#2
values_list = [1, 'строка', True]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = [True, 'строка']
print_params(*values_list_2, 42)