from PyQt5 import QtCore, QtGui, QtWidgets


class login(object):
    def setupUi(self, MainWindow, app):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 300)
        MainWindow.setAutoFillBackground(True)
        self.app = app
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

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.userName_box, self.passWord_box)
        MainWindow.setTabOrder(self.passWord_box, self.loginButton)
        MainWindow.setTabOrder(self.loginButton, self.userColor)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.usrename_label.setText(_translate("MainWindow", "Username :"))
        self.password_label.setText(_translate("MainWindow", "Password :"))
        
        self.passWord_box.setText("123456")
        self.userName_box.setText("devNull")
    
    def chech_cred(self):
        user = ("devNull", "123456")
        colors = (
            red:="rgb(250, 0, 0)",
            green:="rgb(0, 200, 0)"
            )
        pass_color = colors[self.passWord_box.text() == user[1]]
        user_color = colors[self.userName_box.text() == user[0]]
        self.userColor.setStyleSheet(f"background-color: {user_color};")
        self.passColor.setStyleSheet(f"background-color: {pass_color};")
        if (green, green) == (pass_color, user_color):
            self.app.quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = login()
    ui.setupUi(MainWindow, app)
    MainWindow.show()
    print('-------------test-------------')
    if not app.exec_():
        app.quit()

    print("hallo")
