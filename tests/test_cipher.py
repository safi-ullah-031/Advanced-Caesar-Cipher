import sys
import os

# Add project root to Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from caesar_des_encryption import CaesarDESCipherEncrypt
from caesar_des_decryption import CaesarDESCipherDecrypt

def test_encryption():
    cipher = CaesarDESCipherEncrypt("test_key", 3)
    encrypted_text = cipher.encrypt("HELLO")
    assert encrypted_text != "HELLO"

def test_decryption():
    cipher_enc = CaesarDESCipherEncrypt("test_key", 3)
    cipher_dec = CaesarDESCipherDecrypt("test_key", 3)

    encrypted_text = cipher_enc.encrypt("HELLO")
    decrypted_text = cipher_dec.decrypt(encrypted_text)

    assert decrypted_text == "HELLO"
