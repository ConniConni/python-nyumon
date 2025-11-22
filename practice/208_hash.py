import base64
import os
import hashlib

user_name = "user1"
user_pass = "password"
db = {}

salt = base64.b64encode(os.urandom(32))


# # ハッシュ化を繰り返す処理はメソッド化されている
# def get_digest(password):
#     # user_passをutf-8でbytes表記に変換
#     password = bytes(password, "utf-8")
#     # password = user_pass.encode("utf-8") も同じ挙動になる

#     # passwordをハッシュ化
#     digest = hashlib.sha256(salt + password).hexdigest()
#     for _ in range(10000):
#         digest = hashlib.sha256(bytes(digest, "utf-8")).hexdigest()
#     return digest

# 上記関数の処理をメソッドを使って再現
digest = hashlib.pbkdf2_hmac("sha256", bytes("password", "utf-8"), salt, 10000).hex()

# dbに値を追加
# db[user_name] = get_digest(user_pass)
db[user_name] = digest


# ２回目以降のログインのユーザー確認
def is_login(user_name, user_pass):
    # return get_digest(user_pass) == db[user_name]
    return (
        hashlib.pbkdf2_hmac("sha256", bytes(user_pass, "utf-8"), salt, 10000).hex()
        == db[user_name]
    )


print(db)
print(is_login(user_name, user_pass))
# ユーザーが異なるパスワードで実行するとFalseとなる
print(is_login(user_name, "test"))
