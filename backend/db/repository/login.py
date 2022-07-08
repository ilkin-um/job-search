from db.models.users import User
from sqlalchemy.orm import Session
from core.hashing import Hasher


def get_user(username: User, db: Session):
    user = db.query(User).filter(User.email == username).first()
    return user


def authenticate_user(username: str, password: str, db: Session):
    user = get_user(username=username, db=db)
    if not user or not Hasher.verify_passwd(password, user.hashed_password):
        return False
    return user
