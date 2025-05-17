import os
import sqlite3
from app.init_db import init_db

# Инициализируем базу данных заново
init_db()
print("База данных обновлена.")

# Проверяем содержимое таблицы профессий
conn = sqlite3.connect("grader.sqlite")
cursor = conn.cursor()
cursor.execute("SELECT * FROM professions")
professions = cursor.fetchall()
conn.close()

print(f"Количество профессий в базе данных: {len(professions)}")
for profession in professions:
    print(f"ID: {profession[0]}, Название: {profession[1]}")