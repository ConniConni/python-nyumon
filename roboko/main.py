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
        cprint(f'{user_name}: which restaurants do you like?', 'green')
    
    @frame
    def recommend_restaurant(self, restaurant_name):
            cprint(f'私のおすすめのレストランは、{restaurant_name}です。', 'green')
            cprint(f'I recommend {restaurant_name} restaurant.', 'green')
            cprint('このレストランは好きですか[Yes/No]', 'green')
            cprint('Do you like it?[y/n]', 'green')


    @frame
    def see_you(self, user_name):
        cprint(f'{self.robot_name}: {user_name}さん。ありがとうとございました。', 'green')
        cprint(f'{self.robot_name}! Thank you so much {user_name}!', 'green')


def check_file(file_name, restaurant_name, choice_count=1):
    # CSVのヘッダーを定義
    fieldnames = ['Name', 'Count']
    restaurant_found_flag = False

    # ファイルがない場合は、ヘッダーをつけてファイルを新規作成する
    if not os.path.isfile(file_name):
        with open(file_name, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            writer.writeheader()
    # ファイルがある場合は、現在の記録を確認し、レストランの好みを確認する
    else:
        with open(file_name, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            updated_restaurant_list = []
            for row in reader:
                print(row['Name'], row['Count'])

                if row['Name'] == favorite_restaurant:
                    updated_count = int(row['Count']) + 1
                    updated_restaurant_list.append({
                        'Name':favorite_restaurant,
                        'Count':updated_count
                    })
                    restaurant_found_flag = True
                    print(updated_restaurant_list)

                else:
                    updated_restaurant_list.append(row)

        # 入力されたレストラン名がCSVにある場合、ファイルの回数を更新する
        with open(file_name, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(updated_restaurant_list)

    # 入力されたレストラン名がCSVにない場合、ファイルに記録する
    if not restaurant_found_flag:
        with open(file_name, 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            writer.writerow({'Name': restaurant_name, 'Count': choice_count})
    else:
        pass

# おすすめのレストランを提案し、ユーザーの好みを尋ねる
def ranking_restaurant(file_name):
    popular_restaurant = ''
    comparison_count = 0
    with open(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if len(popular_restaurant) == 0:
                comparison_count = row['Count']
                popular_restaurant = row['Name']
                print(f'最も人気なレストランは{popular_restaurant}です')
            else:
                if comparison_count < row['Count']:
                    comparison_count = row['Count']
                    popular_restaurant = row['Name']
                    print(f'最も人気なレストランは{popular_restaurant}です')
                else:
                    not_most_popular_restaurant = row['Name']
                    print(f'{not_most_popular_restaurant}よりも人気なレストランがあるようです')
        return popular_restaurant



# Restaurantクラスのインスタンスを生成
path = 'restaurant.csv'
roboko = RestaurantRobot('Roboko')

# ユーザーの名前を尋ねる
roboko.hello()
user_name = input()

# レストランロボットのオススメ提案を受ける
if os.path.isfile(path):
    result = ranking_restaurant(path)
    roboko.recommend_restaurant(result)
    reply_to_recommendation = input()
    # お気に入りのレストランが見つかったら提案を終了する
    if reply_to_recommendation == 'Yes':
        print(f'レストラン: {result} を気に入ってもらえて嬉しいです。')
    # お気に入りのレストランではなかった場合、次を提案する
    else:
        pass
else:
    pass

# お気に入りのレストランを尋ねる
roboko.favorite_restaurant(user_name)
favorite_restaurant = input()

check_file(path,favorite_restaurant)


# プログラムを終了する
roboko.see_you(user_name)


