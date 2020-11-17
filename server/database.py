import sqlite3


def checkUser(info, connection='assets/users.sqlite'):
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
        except Exception as i:
            print(i)

    return f"{bool(len(returned))}<SEP>{(password,) in returned}"


def newUser(userName, password, connection='assets/users.sqlite'):
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
        except Exception as i:
            print(i)
            return False


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "newuser":
            if len(sys.argv) == 4:
                newUser(sys.argv[2], sys.argv[3])
                print(f"Added new user {sys.argv[2]}")
            else:
                print("Username and/or password is/are not specified")
        else:
            print("Invalid argument")
    else:
        print("No argument specifild")