from PyQt5 import QtCore, QtGui, QtWidgets

class Login(object):
    def __init__(self, **kwargs):
        self.app = kwargs["app"]
        self.DISCONNECT_MESSAGE = kwargs["DISCONNECT_MESSAGE"]
        self.SEPARATOR = kwargs["SEPARATOR"]
        self.LOGIN_MESSAGE = kwargs["LOGIN_MESSAGE"]
        self.send = kwargs["send-func"]
        self.result = (False, None)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 300)
        MainWindow.setAutoFillBackground(True)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(550, 300))
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")

        self.userName_box = QtWidgets.QLineEdit(self.centralwidget)
        self.userName_box.setGeometry(QtCore.QRect(190, 100, 200, 30))
        self.userName_box.setMinimumSize(QtCore.QSize(200, 30))
        self.userName_box.setObjectName("userName_box")
        self.userName_box.returnPressed.connect(self.chech_cred)

        self.passWord_box = QtWidgets.QLineEdit(self.centralwidget)
        self.passWord_box.setGeometry(QtCore.QRect(190, 170, 200, 30))
        self.passWord_box.setMinimumSize(QtCore.QSize(200, 30))
        self.passWord_box.setObjectName("passWord_box")
        self.passWord_box.returnPressed.connect(self.chech_cred)

        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(220, 210, 140, 28))
        self.loginButton.setMinimumSize(QtCore.QSize(140, 25))
        self.loginButton.setFlat(False)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.chech_cred)
        
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setItalic(False)
        font.setKerning(True)

        self.usrename_label = QtWidgets.QLabel(self.centralwidget)
        self.usrename_label.setGeometry(QtCore.QRect(190, 75, 151, 21))
        self.usrename_label.setFont(font)
        self.usrename_label.setObjectName("usrename_label")

        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(190, 145, 151, 21))
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)

        self.userColor = QtWidgets.QGraphicsView(self.centralwidget)
        self.userColor.setGeometry(QtCore.QRect(140, 100, 30, 30))
        self.userColor.setMinimumSize(QtCore.QSize(30, 30))
        self.userColor.setBackgroundBrush(brush)
        self.userColor.setInteractive(False)
        self.userColor.setObjectName("userColor")

        self.passColor = QtWidgets.QGraphicsView(self.centralwidget)
        self.passColor.setGeometry(QtCore.QRect(140, 170, 30, 30))
        self.passColor.setMinimumSize(QtCore.QSize(30, 30))
        self.passColor.setBackgroundBrush(brush)
        self.passColor.setInteractive(False)
        self.passColor.setObjectName("passColor")

        self.alert = QtWidgets.QLabel(self.centralwidget)
        self.alert.setGeometry(QtCore.QRect(10, 270, 271, 21))
        font.setPointSize(12)
        self.alert.setFont(font)
        self.alert.setStyleSheet("color: \"red\"")
        self.alert.setObjectName("alert")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.userName_box, self.passWord_box)
        MainWindow.setTabOrder(self.passWord_box, self.loginButton)
        MainWindow.setTabOrder(self.loginButton, self.userColor)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clash of Code | Login"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.usrename_label.setText(_translate("MainWindow", "Username :"))
        self.password_label.setText(_translate("MainWindow", "Password :"))
    
    def chech_cred(self):
        user = ("devNull", "123456")
        user = (self.userName_box.text(), self.passWord_box.text())
        user_check = self.send(self.SEPARATOR.join(('login',*user))).split(self.SEPARATOR)
        colors = (
            red:="rgb(250, 0, 0)",
            green:="rgb(0, 200, 0)"
            )
        user_color = colors[user_check[0] == "True"]
        pass_color = colors[user_check[1] == "True"]
        self.userColor.setStyleSheet(f"background-color: {user_color};")
        self.passColor.setStyleSheet(f"background-color: {pass_color};")
        if (green, green) == (pass_color, user_color):
            self.result = (True, user[0])
            self.app.quit()

    def set_alert(self, cmd):
        _translate = QtCore.QCoreApplication.translate
        self.alert.setText(_translate("MainWindow", cmd))

if __name__ == "__main__":
    import sys, random, os
    if '\\client' not in (cwd:=os.getcwd()):
        os.chdir(f"{cwd}\\client")

    def test(*args):
        var = ("True", "False")
        return f'{random.choice(var)}<SEP>{random.choice(var)}'

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    d = {
        "app": app,
        "DISCONNECT_MESSAGE": "!DISCONNECT",
        "SEPARATOR": '<SEP>',
        "LOGIN_MESSAGE": 'sendInfo',
        "send-func": test
    }
    ui = Login(**d)
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.set_alert("Test")
    print('-------------test-------------')
    if not app.exec_():
        app.quit()

    print(ui.result)
