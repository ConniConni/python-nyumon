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

print(db)
