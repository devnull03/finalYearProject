from PyQt5 import QtCore, QtGui, QtWidgets


class ServerGui(object):
    def __init__(self, **kwargs):
        self.participants = kwargs["participants"]
        self.mode = kwargs["mode"]
        self.time = int(kwargs["time"])
        self.start = False
        self.count = self.time*60

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(723, 448)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(723, 448))
        MainWindow.setMaximumSize(QtCore.QSize(723, 448))
        MainWindow.setWindowOpacity(1.0)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.player_scroll_area = QtWidgets.QScrollArea(self.centralwidget)
        self.player_scroll_area.setGeometry(QtCore.QRect(40, 110, 641, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player_scroll_area.sizePolicy().hasHeightForWidth())
        self.player_scroll_area.setSizePolicy(sizePolicy)
        self.player_scroll_area.setTabletTracking(False)
        self.player_scroll_area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.player_scroll_area.setWidgetResizable(True)
        self.player_scroll_area.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.player_scroll_area.setObjectName("player_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 639, 179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.playres = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.playres.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.playres.setFont(font)
        self.playres.setTabletTracking(True)
        self.playres.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.playres.setObjectName("playres")
        self.verticalLayout.addWidget(self.playres)
        self.player_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.Timer = QtWidgets.QLabel(self.centralwidget)
        self.Timer.setGeometry(QtCore.QRect(50, 20, 101, 31))
        font.setPointSize(15)
        self.Timer.setFont(font)
        self.Timer.setAlignment(QtCore.Qt.AlignCenter)
        self.Timer.setObjectName("Timer")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(37, 50, 646, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.mode_label = QtWidgets.QLabel(self.centralwidget)
        self.mode_label.setGeometry(QtCore.QRect(390, 20, 281, 31))
        self.mode_label.setFont(font)
        self.mode_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mode_label.setObjectName("mode_label")
        
        self.player_label = QtWidgets.QLabel(self.centralwidget)
        self.player_label.setGeometry(QtCore.QRect(40, 70, 161, 31))
        self.player_label.setFont(font)
        self.player_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.player_label.setObjectName("player_label")
        
        self.start_timer_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_timer_button.setGeometry(QtCore.QRect(40, 370, 141, 41))
        font.setPointSize(12)
        self.start_timer_button.setFont(font)
        self.start_timer_button.setObjectName("start_timer_button")
        self.start_timer_button.clicked.connect(self.start_timer)

        timer = QtCore.QTimer(MainWindow)
        timer.timeout.connect(self.showTime) 
        timer.start(1000)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clash of Code | Admin"))
        self.Timer.setText(_translate("MainWindow", f"{self.time}:00"))
        self.mode_label.setText(_translate("MainWindow", f"Mode : {self.mode}"))
        self.player_label.setText(_translate("MainWindow", "Players"))
        self.start_timer_button.setText(_translate("MainWindow", "Start"))
        self.update_board()
    
    def update_board(self):
        pp = self.participants
        self.participant_list = "\n".join(
            f"{i+1}. {j}"+f" - {pp[j]['%']}% - length {pp[j]['len']} - time {pp[j]['time']}"*bool(pp[j]['time']) for i,j in enumerate(pp))
        self.playres.setText(self.participant_list)

    def showTime(self): 
        if self.start: 
            self.count -= 1
            if self.count == 0: 
                self.start = False
                self.Timer.setText("0:00")
                self.select_button.click()
        if self.start: 
            minuts = self.count//60
            seconds = "0"*((s:=self.count%60)<10) + str(s)
            self.Timer.setText(f"{minuts}:{seconds}")

    def start_timer(self): 
        self.start = True
        if self.count == 0: 
            self.start = False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    info = {
        "mode": "shortest",
        "time": 15,
    }
    participants = [
            "admin",
            "dev",
            "Null",
            "test",
            "test test",
            "test test test",
            "another test",
            "another another test",
            "last test"
        ]
    p = {}
    for i in participants:
        p.update({i: {"time": None, "%": None, "len": None}})

    p.update({"dev": {"time":"0:10", "%":100.0, "len":22}})
    ui = ServerGui(**info, participants=p)
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.update_board()
    sys.exit(app.exec_())
