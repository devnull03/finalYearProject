import time
from login import startLogin

a = False
try :
    a = startLogin()
except  :
    print("nope")
else :
    time.sleep(2)
    if a :
        from mainPage import startMainPage
        startMainPage()
