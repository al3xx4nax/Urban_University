x = 38
print('дратути!')
if x < 0:
    print('меньше нуля')
print('дотвидания!')

a, b = 25, 15

if a > b:
    print('a > b')
if a < b:
    print('a , b')
if a > b and a > 0:
    print('Успех')
if (a > b) and (b > 0 or b < 25):
    print('Успех')
if b > 10 and b <= 15:
    print('Успех')

c, d = '3424324', '23232'

if '3424324' > '23232':
    print('Успех')
if d < c:
    print('Успех')

e, f = [11, 13], [111, 1]

if e < f:
    print('Успех')

if '60' != 5:
    print('Успех')

if '6' > 5:
    print('Успех')
if [10, 15] > 5:
    print('Успех')