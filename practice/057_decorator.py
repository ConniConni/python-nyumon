def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

# デコレータを使って同様の記述
@print_info
def add_num(a, b):
    return a + b

# f = print_info(add_num)
# r = f(10, 20)
# print(r)

# デコレータを使って同様の記述
f = add_num(10, 20)
print(f)