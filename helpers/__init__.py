import string
import random
from passlib.hash import pbkdf2_sha256

def randomString(length):
    randString = ''.join(random.choices(string.ascii_lowercase +string.ascii_uppercase, k=length))
    return str(randString)

def hashThis(string):
    return pbkdf2_sha256.hash(string)

def verifyHash(string,hash):
   return pbkdf2_sha256.verify(string,hash)