import sqlite3
import datetime


def baza():


    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()


    cursor.execute("""CREATE TABLE IF NOT EXISTS otchet(
                    data TEXT,
                    user TEXT,
                    Касса утром INT,
                    Выручка INT,
                    Безнал INT,
                    Наличными INT,
                    Инкассации INT,
                    Доп_расходы INT,
                    Факт INT);
                    """)
    conn.commit()

def record(date, user, money_in_the_morning, proceeds, cashless, cash_1, collection, costs, fact):
    pass
    cursor.execute("""INSERT INTO otchet(
                    
                    """)