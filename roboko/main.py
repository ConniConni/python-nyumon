from termcolor import cprint
import csv
import os

def frame(func):
    def wrapper(*args, **kwargs):
        cprint('*' * 60, 'green')
        func(*args, **kwargs)
        cprint('*' * 60, 'green')
    return wrapper

class RestaurantRobot(object):
    def __init__(self, robot_name):
        self.robot_name = robot_name
        cprint('####Greetingクラスのオブジェクトを初期化####', 'yellow')

    @frame
    def hello(self):
        cprint(f'こんにちは!私は{self.robot_name}です。あなたの名前は何ですか？', 'green')
        cprint(f'Hello, I am {self.robot_name}. What is your name?','green')

    @frame
    def favorite_restaurant(self, user_name):
        cprint(f'{user_name}さん。どこのレストランが好きですか？', 'green')
        cprint(f'{user_name}which restaurants do you like?', 'green')

    @frame
    def see_you(self, user_name):
        cprint(f'{self.robot_name}: {user_name}さん。ありがとうとございました。', 'green')
        cprint(f'{self.robot_name}: Thank you so much {user_name}!', 'green')


def check_file(file_name, restaurant_name, choice_count=1):
    # CSVのヘッダーを定義
    fieldnames = ['Name', 'Count']

    # ファイルがない場合は、ヘッダーをつけてファイルを新規作成する
    if not os.path.isfile(file_name):
        with open(file_name, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            writer.writeheader()
    # ファイルがある場合は、現在の記録を確認する
    else:
        with open(file_name, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                most_popular_restaurant = row['Name']
                print(most_popular_restaurant)

    # 入力値をファイルに記録する
    with open(file_name, 'a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        writer.writerow({'Name': restaurant_name, 'Count': choice_count})

# Restaurantクラスのインスタンスを生成
roboko = RestaurantRobot('Roboko')

# ユーザーの名前を尋ねる
roboko.hello()
user_name = input()

# お気に入りのレストランを尋ねる
roboko.favorite_restaurant(user_name)
favorite_restaurant = input()

path = 'restaurant.csv'
check_file(path,favorite_restaurant)




# プログラムを終了する
roboko.see_you(user_name)


