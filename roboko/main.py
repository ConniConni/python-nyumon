from termcolor import cprint

def frame(func):
    def wrapper(*args, **kwargs):
        cprint('*' * 60, 'green')
        func(*args, **kwargs)
        cprint('*' * 60, 'green')
    return wrapper


class Greeting(object):
    def __init__(self, robot_name):
        self.robot_name = robot_name
        cprint('####Greetingクラスのオブジェクトを初期化####', 'yellow')
    @frame
    def hello(self):
        cprint(f'こんにちは!私は{self.robot_name}です。あなたの名前は何ですか？', 'green')
        cprint(f'Hello, I am {self.robot_name}. What is your name?','green')

class FavoriteRestaurant(object):
    def __init__(self, user_name):
        self.user_name = user_name
        cprint('####FavoriteRestaurantクラスのオブジェクトを初期化####', 'yellow')

    @frame
    def question(self):
        cprint(f'{user_name}さん。どこのレストランが好きですか？', 'green')
        cprint(f'{self.user_name}which restaurants do you like?', 'green')

class GoodBye(object):
    def __init__(self, robot_name, user_name):
        self.robot_name = robot_name
        self.user_name = user_name
        cprint('####GoodByeクラスのオブジェクトを初期化####', 'yellow')

    @frame
    def see_you(self):
        cprint(f'{self.robot_name}: {self.user_name}さん。ありがとうとございました。', 'green')
        cprint(f'{self.robot_name}: Thank you so much {self.user_name}!', 'green')

greeting = Greeting('Roboko')

greeting.hello()

user_name = input()

favorite_restaurant = FavoriteRestaurant(user_name)
favorite_restaurant.question()

favorite_restaurant = input()

good_bye = GoodBye('Roboko',user_name)
good_bye.see_you()


