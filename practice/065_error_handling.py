l = [1 ,2 ,3]
i = 5
del l

try:
    l [i]
except IndexError as ex:
    print(f"Don't worry: {ex}")
except NameError as ex:
    print(f"catch NameError: {ex}")
else:
    print(l)

print('last')
