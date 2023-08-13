from vtils import util
from vtils.util import Cipher

def test_version():
    assert util.get_version() == 'Ver. 0.0.9'


def test_security():
    text = "This is just for testing"
    key = "AbCdEf1234567890AbCdEf1234567890"
    cipher = Cipher(key)
    encrypted = cipher.encrypt(text)
    decrypted = cipher.decrypt(encrypted)
    assert decrypted == text