x = input()
x =int(x)

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('a is positive')
    a = str(a)
    print(type(a),type(b))
    if b > 0:
        print('b is positive')
        b += 1
        print(b)



