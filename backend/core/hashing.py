from passlib.context import CryptContext

passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    @staticmethod
    def hash_passwd(passwd):
        return passwd_context.hash(passwd)

    @staticmethod
    def verify_passwd(plain_passwd, hashed_passwd):
        return passwd_context.verify(plain_passwd, hashed_passwd)
