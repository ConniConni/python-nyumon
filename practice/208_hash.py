import hashlib

user_name = "user1"
user_pass = "password"
db = {}

# user_passをutf-8でbytes表記に変換
password = bytes(user_pass, "utf-8")
# password = user_pass.encode("utf-8") も同じ挙動になる

# passwordをハッシュ化
digest = hashlib.sha256(password).hexdigest()
# dbに値を追加
db[user_name] = digest
print(db)
