# ascii_letters: stringモジュールで提供されるアルファベットの小文字と大文字をすべて含む文字列定数
# AES暗号アルゴリズムのブロックサイズは16バイト
# 16文字のランダムなキーを生成
import string
import random

from Crypto.Cipher import AES

# print(AES.block_size)
# print(string.ascii_letters)
# key1 = random.choice(string.ascii_letters)
# key2 = random.choice(string.ascii_letters)
# key = key1 + key2
key = "".join(random.choice(string.ascii_letters) for _ in range(AES.block_size))
# print(key)
iv = "".join(random.choice(string.ascii_letters) for _ in range(AES.block_size))

plaintext = "fdafejiwaifdjafewafeaf"
print(plaintext)
print(f"変更前の文字列の長さ:{len(plaintext)}")
# AESアルゴリズムを使った新しい暗号化セッションを開始するための関数呼び出し
# AES.new([暗号化キー], [暗号利用モード], 初期化ベクトル)
# cipher = AES.new(key, AES.MODE_CBC, iv)
padding_length = AES.block_size - len(plaintext) % AES.block_size
plaintext += chr(padding_length) * padding_length
print(plaintext)
print(f"変更後の文字列の長さ:{len(plaintext)}")
