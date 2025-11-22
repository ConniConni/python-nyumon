# ascii_letters: stringモジュールで提供されるアルファベットの小文字と大文字をすべて含む文字列定数
# AES暗号アルゴリズムのブロックサイズは16バイト
# 16文字のランダムなキーを生成
import string
import random

from Crypto.Cipher import AES

print(AES.block_size)
print(string.ascii_letters)
# key1 = random.choice(string.ascii_letters)
# key2 = random.choice(string.ascii_letters)
# key = key1 + key2
key = "".join(random.choice(string.ascii_letters) for _ in range(AES.block_size))
print(key)
