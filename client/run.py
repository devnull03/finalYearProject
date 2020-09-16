
try :
    from client import login
except TypeError :
    print("nope")
except BaseException :
    print("yeee")
