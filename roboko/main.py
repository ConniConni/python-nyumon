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


# Restaurantクラスのインスタンスを生成
roboko = RestaurantRobot('Roboko')

# ユーザーの名前を尋ねる
roboko.hello()
user_name = input()

# お気に入りのレストランを尋ねる
roboko.favorite_restaurant(user_name)
favorite_restaurant = input()

# 答えてもらったレストランをファイルに記録
# try:
#     with open('restaurant.csv', 'r+') as f:
#         print('ファイルの中身は以下のとおりです。')
#         print(f.read())
#         f.write(f'{favorite_restaurant}\n')

# except FileNotFoundError:
#     print('ファイルが存在しません。新しいファイルを作成します。')
#     with open('restaurant.csv', 'a') as f:
#         f.write(f'{favorite_restaurant},\n')

# try:
#     with open('restaurant.csv', 'r+') as csv_file:
#         print('既存ファイルに記録しました。')
#         fieldnames = ['Name', 'Count']
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         writer.writerow({'Name': favorite_restaurant,'Count': 1})
# except FileNotFoundError:
#     print('ファイルが存在しません。新しいファイルを作成します。')
#     with open('restaurant.csv', 'w') as csv_file:
#         fieldnames = ['Name', 'Count']
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerow({'Name': favorite_restaurant,'Count': 1})

# ①ファイルの存在確認
# True:  ファイル更新
# False: ファイル作成
#       （1）ヘッダーを書き込み
#        (2)１行目を書き込み
#　共通処理
#  (1)ファイルの存在確認
#  (2)fieldnames定義
#  (3)dictwriteメソッド実行 #各行に辞書型で書き込む

path = 'restaurant.csv'
is_file = os.path.isfile(path)

if not os.path.isfile(path):
    with open('restaurant.csv', 'w+') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        print('新規ファイル作成')
        writer.writeheader()

else:
    pass
with open('restaurant.csv', 'a+') as csv_file:
    print('ファイル更新')
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writerow({'Name': favorite_restaurant, 'Count': 1})




# プログラムを終了する
roboko.see_you(user_name)


