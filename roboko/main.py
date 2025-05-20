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
    def hello(self, robot_name):
        cprint(f'こんにちは!私は{robot_name}です。あなたの名前は何ですか？', 'green')
        cprint(f'Hello, I am {robot_name}. What is your name?','green')

class FavoriteRestaurant(object):
    def __init__(self):
        cprint('####FavoriteRestaurantクラスのオブジェクトを初期化####', 'yellow')
    
    @frame
    def question(self, user_name):
        cprint(f'{user_name}, さん。どこのレストランが好きですか？', 'green')
        cprint(f'{user_name}, which restaurants do you like?', 'green')


greeting = Greeting()

greeting.hello('Roboko')

user_name = input()

favorite_restaurant = FavoriteRestaurant()
favorite_restaurant.question(user_name)

favorite_restaurant = input()

print('Roboko:',user_name, 'さん。ありがとうとございました。')
print('Roboko:', 'Thank you so much',user_name,'!')

