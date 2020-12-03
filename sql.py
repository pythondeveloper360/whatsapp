import psycopg2
from psycopg2 import sql

db = psycopg2.connect(host = "ec2-18-232-143-90.compute-1.amazonaws.com",
            user = "piakexgytmjras",
            database = "d5ajg15n8fdv7a",
            port = "5432",
            password = "eb0ac0264fa02800ec07fbc880b3a4437a53de79ab7e4eea5c6634795499ce52")

cursor = db.cursor()



def authenticateUser(user_id,password):
    sqlquery = sql.SQL('select * from users where {user_id} = %s and {password} = %s').format(
        user_id = sql.Identifier("user_id"),
        password = sql.Identifier("password")
    )
    cursor.execute(sqlquery,(user_id,password))
    data = cursor.fetchall()
    print(True if data else False)
