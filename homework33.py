import itertools


def all_variants(my_str):
    temp_list = []
    for lst_1 in range(1, len(my_str) + 1):
        temp_list.append(list(itertools.combinations(my_str, lst_1)))
    for lst_2 in temp_list:
        for lst_3 in lst_2:
            if ''.join(lst_3) != 'ac':
                yield ''.join(lst_3)


a = all_variants("abc")
for i in a:
    print(i)
