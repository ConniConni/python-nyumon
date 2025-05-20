# mian.pyの書き方

from lesson_package import human

print(__name__)

def main():
    print(human.cry())

# if文を入れることで呼び出されるだけでは実行されなくなる
if __name__ == '__main__':
    main()
