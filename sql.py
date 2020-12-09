import psycopg2
from psycopg2 import sql
import json
import utils

db = psycopg2.connect(host="ec2-18-232-143-90.compute-1.amazonaws.com",
                      user="piakexgytmjras",
                      database="d5ajg15n8fdv7a",
                      port="5432",
                      password="eb0ac0264fa02800ec07fbc880b3a4437a53de79ab7e4eea5c6634795499ce52")

cursor = db.cursor()


def authenticateUser(user_id, password):
    sqlquery = sql.SQL('select * from users where {user_id} = %s and {password} = %s').format(
        user_id=sql.Identifier("user_id"),
        password=sql.Identifier("password")
    )
    cursor.execute(sqlquery, (user_id, password))
    data = cursor.fetchall()
    print(True if data else False)


def getChats(user_id):
    sqlquery = sql.SQL('select chats from users where {user_id} = %s').format(
        user_id=sql.Identifier("user_id")
    )
    cursor.execute(sqlquery, (user_id,))
    data = cursor.fetchone()[0]
    data = utils.strToDict(data) if data else {}
    return data


def addChats(user_id, chat_name, chat_id):
    chats = json.dumps(getChats(user_id).update({chat_id: chat_name}))

    sqlquery = sql.SQL('update users set {chats} = %s where {user_id} = %s').format(
        chats=sql.Identifier("chats"),
        user_id=sql.Identifier("user_id")
    )
    cursor.execute(sqlquery, (chats, user_id))
    db.commit()
