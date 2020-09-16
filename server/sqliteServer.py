import sqlite3
from sqlite3 import Error

def checkUser(connection,userName,password):
    returned = None
    with sqlite3.connect(connection) as conn :
        cur = conn.cursor()
        try :
            cur.execute(f'''
                    select password from users where userName = \"{userName}\"            
                ''')
            conn.commit()
            returned = cur.fetchall()
        except Error as i :
            print(i)

    return f"{bool(len(returned))}<SEP>{(password,) in returned}"

def newUser(connection,userName,password):
    with sqlite3.connect(connection) as conn :
        cur = conn.cursor()
        try :
            cur.execute(f'''
                    insert into users values (
                        \"{userName}\",\"{password}\"
                    )
                ''')
            conn.commit()
            return True
        except Error as i :
            print(i)
            return False
