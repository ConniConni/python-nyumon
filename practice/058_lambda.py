l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# 関数を定義し、実行
def sample_func(word):
    return word.capitalize()
change_words(l, sample_func)

# lambdaを（無名関数）使って簡単にかく
# ２行削減できる
sample_func = change_words(l, lambda word: word.capitalize())

