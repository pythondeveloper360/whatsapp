
from datetime import datetime
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
    return (True if data else False)


def getChats(user_id):
    sqlquery = sql.SQL('select chats from users where {user_id} = %s').format(
        user_id=sql.Identifier("user_id")
    )
    cursor.execute(sqlquery, (user_id,))
    data = cursor.fetchone()[0]
    return utils.Converter(data)._dict() if data else []


def addChats(user_id, chat_name, chat_id):
    sqlquery = sql.SQL('select chats from users where {user_id} = %s').format(
        user_id=sql.Identifier("user_id")
    )
    cursor.execute(sqlquery, (user_id,))
    data = cursor.fetchone()[0]
    if "{"+chat_id+":"+chat_name+"}" not in data:
        data.append("{"+chat_id+":"+chat_name+"}")
        sqlquery = sql.SQL("update users set {chats} = %s where {user_id} = %s").format(
            chats=sql.Identifier("chats"),
            user_id=sql.Identifier("user_id")
        )
        cursor.execute(sqlquery, (data, user_id))
        db.commit()
        return True
    else:
        return False


def getChattings(user_id, chat_id):
    rdata = []
    sqlquery = sql.SQL('select * from messages where {from_id} = %s or {to_id} = %s').format(
        from_id=sql.Identifier("from_id"),
        to_id=sql.Identifier("to_id")
    )
    cursor.execute(sqlquery, (user_id, chat_id))
    data = cursor.fetchall()
    if data:
        for i in range(len(data)):
            rdata.append(dict(from_id=data[i][0], to_id=data[i][1], from_name=data[i]
                              [2], to_name=data[i][3], msg=data[i][4], time=data[i][5]))
        return rdata
    else:
        return False


def getNameFromId(id):
    sqlquery = sql.SQL('select name from users where {user_id} = %s').format(
        user_id=sql.Identifier("user_id")
    )
    cursor.execute(sqlquery, (id,))
    data = cursor.fetchone()
    return data[0] if data else False


def sendMsg(from_id, to_id, msg):
    current_time = datetime.now().strftime("%H:%M:%S")
    sqlquery = sql.SQL(
        'insert into messages ({from_id},{to_id},{from_name},{to_name},{msg_body},{time}) values (%s,%s,%s,%s,%s,%s)').format(
            from_id=sql.Identifier("from_id"),
            to_id=sql.Identifier("to_id"),
            from_name=sql.Identifier("from_name"),
            to_name=sql.Identifier("to_name"),
            msg_body=sql.Identifier("msg_body"),
            time=sql.Identifier("time")
    )
    cursor.execute(sqlquery, (from_id, to_id, getNameFromId(
        from_id), getNameFromId(to_id), msg, current_time))
    db.commit()
