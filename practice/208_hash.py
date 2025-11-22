import hashlib

user_name = "user1"
user_pass = "password"
db = {}


def get_digest(password):
    # user_passをutf-8でbytes表記に変換
    password = bytes(password, "utf-8")
    # password = user_pass.encode("utf-8") も同じ挙動になる

    # passwordをハッシュ化
    digest = hashlib.sha256(password).hexdigest()
    return digest


# dbに値を追加
db[user_name] = get_digest(user_pass)


# ２回目以降のログインのユーザー確認
def is_login(user_name, user_pass):
    return get_digest(user_pass) == db[user_name]


print(db)
print(is_login(user_name, user_pass))
# ユーザーが異なるパスワードで実行するとFalseとなる
print(is_login(user_name, "test"))
