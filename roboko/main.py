from termcolor import cprint

def frame(func):
    def wrapper(*args, **kwargs):
        cprint('*' * 60, 'green')
        func(*args, **kwargs)
        cprint('*' * 60, 'green')
    return wrapper


class Greeting(object):
    def __init__(self):
        cprint('####Greetingクラスのオブジェクトを初期化####', 'yellow')
    @frame
    def hello(self, name):
        cprint(f'こんにちは!私は{name}です。あなたの名前は何ですか？', 'green')
        cprint(f'Hello, I am {name}. What is your name?','green')


greeting = Greeting()

greeting.hello('Roboko')

user_name = input()

print(user_name, 'さん。どこのレストランが好きですか？')
print(user_name, 'which restaurants do you like?')

favorite_restaurant = input()

print('Roboko:',user_name, 'さん。ありがとうとございました。')
print('Roboko:', 'Thank you so much',user_name,'!')

