import sqlite3
from sqlite3 import Error


def checkUser(info, connection='users.sqlite'):
    returned = None
    info = info.split('<SEP>')
    if len(info) == 0:
        return 'False<SEP>False'
    elif len(info) == 1:
        userName, password = info[0], None
    else:
        userName, password = info
    with sqlite3.connect(connection) as conn:
        cur = conn.cursor()
        try:
            cur.execute(f'''
                    select password from users where userName = \"{userName}\"            
                ''')
            conn.commit()
            returned = cur.fetchall()
        except Error as i:
            print(i)

    return f"{bool(len(returned))}<SEP>{(password,) in returned}"


def newUser(connection, userName, password):
    with sqlite3.connect(connection) as conn:
        cur = conn.cursor()
        try:
            cur.execute('''
                    create table if not exists users(
                        username char(16) primary key,
                        password char(16) default \'000\'
                )
                ''')
            cur.execute(f'''
                    insert into users values (
                        \"{userName}\",\"{password}\"
                )
                ''')
            conn.commit()
            return True
        except Error as i:
            print(i)
            return False


if __name__ == "__main__":

    # print(
    #     checkUser('devNull<SEP>123456')
    # )
    newUser('users.sqlite', 'admin', 'admin')
