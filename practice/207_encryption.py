# ascii_letters: stringモジュールで提供されるアルファベットの小文字と大文字をすべて含む文字列定数
# AES暗号アルゴリズムのブロックサイズは16バイト
# 16文字のランダムなキーを生成
# ファイルでも実行
import string
import random

from Crypto.Cipher import AES

# print(AES.block_size)
# print(string.ascii_letters)
# key1 = random.choice(string.ascii_letters)
# key2 = random.choice(string.ascii_letters)
# key = key1 + key2
key_bytes = "".join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
).encode("utf-8")
# print(key)
iv_bytes = "".join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
).encode("utf-8")

# plaintext_bytes = "fdafejiwaifdjafewafeaf".encode("utf-8")
with open("plaintext", "r") as f, open("enc.dat", "wb") as e:
    plaintext_bytes = f.read().encode("utf-8")
    print(plaintext_bytes)
    print(f"変更前の文字列の長さ:{len(plaintext_bytes)}")
    # AESアルゴリズムを使った新しい暗号化セッションを開始するための関数呼び出し
    # AES-CBC 前の暗号化ブロックを用いて暗号化。最初の暗号化ブロックのみ初期化ベクトル(iv)を用いる
    # AES.new([暗号化キー], [暗号利用モード], 初期化ベクトル)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    padding_length = AES.block_size - len(plaintext_bytes) % AES.block_size
    plaintext_bytes += (chr(padding_length) * padding_length).encode("utf-8")
    print(plaintext_bytes)
    print(f"変更後の文字列の長さ:{len(plaintext_bytes)}")
    cipher_text = cipher.encrypt(plaintext_bytes)
    e.write(cipher_text)

with open("enc.dat", "rb") as e:
    # 復元
    cipher2 = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    decrypted_text = cipher2.decrypt(e.read())
    # 復元結果をパディングを含めて出力
    print(decrypted_text)
    # パディングした文字列を出力
    print(decrypted_text[-1])
    # 復元結果をパディングを除いて出力
    print(decrypted_text[: -decrypted_text[-1]])
