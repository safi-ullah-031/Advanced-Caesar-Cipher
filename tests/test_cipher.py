import pytest
from caesar_des_encryption import CaesarDESCipher

def test_encryption():
    cipher = CaesarDESCipher("test_key", 3)
    encrypted_text = cipher.encrypt("HELLO")
    assert encrypted_text != "HELLO"  # Should be different after encryption

def test_decryption():
    cipher = CaesarDESCipher("test_key", 3)
    encrypted_text = cipher.encrypt("HELLO")
    decrypted_text = cipher.decrypt(encrypted_text)
    assert decrypted_text == "HELLO"  # Should return original text
