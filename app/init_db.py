from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.database import SessionLocal, UserDB

# Фейковые данные пользователей
fake_users_db = {
    "user": {
        "username": "user",
        "full_name": "John Doe",
        "email": "john@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # password: secret
        "disabled": False,
    }
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def init_db():
    db = SessionLocal()
    
    # Проверяем, есть ли уже пользователи в базе
    user_count = db.query(UserDB).count()
    if user_count == 0:
        # Добавляем тестового пользователя
        for username, user_data in fake_users_db.items():
            db_user = UserDB(
                username=user_data["username"],
                email=user_data["email"],
                full_name=user_data["full_name"],
                hashed_password=user_data["hashed_password"],
                disabled=user_data["disabled"]
            )
            db.add(db_user)
        
        db.commit()
    
    db.close()

if __name__ == "__main__":
    init_db()
    print("База данных инициализирована.")