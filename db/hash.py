from passlib.context import CryptContext


pwd_cnt = CryptContext(schemes='bcrypt', deprecated='auto')

class Hash:
    def bcrypt(password):
        return pwd_cnt.hash(password)
    
    def verify(hashed_pwd, plain_pwd):
        pwd_cnt.verify(plain_pwd, hashed_pwd)
