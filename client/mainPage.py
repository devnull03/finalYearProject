from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path


class MainPage(object):
    def __init__(self, **kwargs):
        self.app = kwargs["app"]
        self.DISCONNECT_MESSAGE = kwargs["DISCONNECT_MESSAGE"]
        self.SEPARATOR = kwargs["SEPARATOR"]
        self.LOGIN_MESSAGE = kwargs["LOGIN_MESSAGE"]
        self.send = kwargs["send-func"]
        self.send_file = kwargs["file-func"]
        self.participants = {}

        self.mode = kwargs["mode"]
        self.task = kwargs["task"]
        self.time = kwargs["time"]
        self.ex = kwargs["examples"]

        self.start = False
        self.count = self.time*60
        self.sent = False
        self.countdown = 6
        self.started = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(460, 800))
        MainWindow.setMaximumSize(QtCore.QSize(460, 800))
        
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        MainWindow.setFont(font)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Timer = QtWidgets.QLabel(self.centralwidget)
        self.Timer.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.Timer.setAlignment(QtCore.Qt.AlignCenter)
        self.Timer.setObjectName("Timer")
        
        self.task_container = QtWidgets.QScrollArea(self.centralwidget)
        self.task_container.setGeometry(QtCore.QRect(20, 110, 421, 201))
        self.task_container.setWidgetResizable(True)
        self.task_container.setObjectName("task_container")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 419, 199))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        font.setPointSize(13)
        self.task_desc = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.task_desc.setFont(font)
        self.task_desc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.task_desc.setWordWrap(True)
        self.task_desc.setObjectName("task_desc")
        self.verticalLayout_3.addWidget(self.task_desc)
        self.task_container.setWidget(self.scrollAreaWidgetContents_5)
        
        self.top_divider = QtWidgets.QFrame(self.centralwidget)
        self.top_divider.setGeometry(QtCore.QRect(20, 40, 421, 20))
        self.top_divider.setFrameShape(QtWidgets.QFrame.HLine)
        self.top_divider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_divider.setObjectName("top_divider")
        
        self.Mode = QtWidgets.QLabel(self.centralwidget)
        self.Mode.setGeometry(QtCore.QRect(230, 10, 211, 31))
        self.Mode.setAlignment(QtCore.Qt.AlignCenter)
        self.Mode.setObjectName("Mode")
        
        self.Task = QtWidgets.QLabel(self.centralwidget)
        self.Task.setGeometry(QtCore.QRect(20, 80, 81, 21))
        font.setPointSize(19)
        self.Task.setFont(font)
        self.Task.setObjectName("Task")
        
        self.Examples = QtWidgets.QLabel(self.centralwidget)
        self.Examples.setGeometry(QtCore.QRect(20, 325, 111, 31))
        self.Examples.setObjectName("Examples")

        self.example_container = QtWidgets.QScrollArea(self.centralwidget)
        self.example_container.setGeometry(QtCore.QRect(20, 360, 421, 131))
        self.example_container.setWidgetResizable(True)
        self.example_container.setObjectName("example_container")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 419, 129))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.examples = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        font.setPointSize(13)
        self.examples.setFont(font)
        self.examples.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.examples.setObjectName("examples")
        self.verticalLayout_2.addWidget(self.examples)
        self.example_container.setWidget(self.scrollAreaWidgetContents_6)
        
        self.top_divider_2 = QtWidgets.QFrame(self.centralwidget)
        self.top_divider_2.setGeometry(QtCore.QRect(20, 512, 421, 20))
        self.top_divider_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.top_divider_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_divider_2.setObjectName("top_divider_2")
        self.top_divider_3 = QtWidgets.QFrame(self.centralwidget)
        self.top_divider_3.setGeometry(QtCore.QRect(20, 592, 421, 20))
        self.top_divider_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.top_divider_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_divider_3.setObjectName("top_divider_3")
        
        self.file = QtWidgets.QLineEdit(self.centralwidget)
        self.file.setGeometry(QtCore.QRect(20, 560, 231, 31))
        font.setPointSize(10)
        self.file.setFont(font)
        self.file.setObjectName("file")

        self.Select_file = QtWidgets.QLabel(self.centralwidget)
        self.Select_file.setGeometry(QtCore.QRect(20, 533, 121, 21))
        font.setPointSize(13)
        self.Select_file.setFont(font)
        self.Select_file.setObjectName("Select_file")
        
        self.finish_button = QtWidgets.QPushButton(self.centralwidget)
        self.finish_button.setGeometry(QtCore.QRect(340, 560, 101, 31))
        font.setPointSize(12)
        self.finish_button.setFont(font)
        self.finish_button.setObjectName("finish_button")
        self.finish_button.clicked.connect(self.file_func)

        self.select_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_button.setGeometry(QtCore.QRect(260, 560, 71, 31))
        self.select_button.setFont(font)
        self.select_button.setObjectName("select_button")
        self.select_button.clicked.connect(lambda: self.showDialog(MainWindow))

        self.players_area = QtWidgets.QScrollArea(self.centralwidget)
        self.players_area.setGeometry(QtCore.QRect(20, 620, 421, 161))
        self.players_area.setWidgetResizable(True)
        self.players_area.setObjectName("players_area")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 419, 159))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout.setObjectName("verticalLayout")
        font.setPointSize(14)
        self.players = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.players.setFont(font)
        self.players.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.players.setObjectName("players")
        self.verticalLayout.addWidget(self.players)
        self.players_area.setWidget(self.scrollAreaWidgetContents_3)

        timer = QtCore.QTimer(MainWindow)
        timer.timeout.connect(self.showTime) 
        timer.start(1000)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clash of Code | Main"))
        self.Timer.setText(_translate("MainWindow", f"{self.time}:00"))
        self.task_desc.setText(_translate("MainWindow", self.task))
        self.Mode.setText(_translate("MainWindow", f"Mode : {self.mode.title()}"))
        self.Task.setText(_translate("MainWindow", "Task"))
        self.Examples.setText(_translate("MainWindow", "Examples"))
        self.examples_list = "\n".join(f"solution({i})-> {self.ex[i]}" for i in self.ex)
        self.examples.setText(_translate("MainWindow", self.examples_list))
        self.Select_file.setText(_translate("MainWindow", "Select File"))
        self.finish_button.setText(_translate("MainWindow", "Finish"))
        self.select_button.setText(_translate("MainWindow", "Select"))
        self.update_board()

    def update_board(self):
        pp = self.participants
        self.participant_list = "\n".join(
            f"{i+1}. {j}"+f" - {pp[j]['%']}% - length {pp[j]['len']} - time {pp[j]['time']}"*bool(pp[j]['time']) for i,j in enumerate(pp))
        self.players.setText(self.participant_list)

    def update(self):
        _translate = QtCore.QCoreApplication.translate
        self.task_desc.setText(_translate("MainWindow", self.task))
        self.examples_list = "\n".join(f"solution({i})-> {self.ex[i]}" for i in self.ex)
        self.examples.setText(_translate("MainWindow", self.examples_list))

    def showDialog(self, MainWindow):
        home_dir = str(Path.home())
        fname = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open file', home_dir, "python files (*.py)")
        self.file.setText(fname[0])
  
    def showTime(self): 
        if not self.started and self.start and self.count == self.time*60:
            self.countdown -= 1
            if self.countdown == 0:
                self.started = True
            self.Timer.setText(f"0:0{self.countdown}")
            return
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

    def file_func(self):
        if self.start and not self.sent and self.started:
            self.send_file(self.file.text())
            self.sent = True
            self.app.quit()


if __name__ == "__main__":
    import sys
    import random
    import os

    if '\\client' not in (cwd := os.getcwd()):
        os.chdir(f"{cwd}\\client")

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    test_info = {
        "mode": "Shortest",
        "time": 10,
        "task": "Test task " * 50,
        "examples": {
            1: 1,
            2: 4,
            3: 9,
            4: 16,
            5: 25,
            6: 36,
            7: 49
        }
    }

    def test(*args):
        var = ("True", "False")
        # return f'{random.choice(var)}<SEP>{random.choice(var)}'*
        print(ui.sent)
    d = {
        "DISCONNECT_MESSAGE": "!DISCONNECT",
        "SEPARATOR": '<SEP>',
        "LOGIN_MESSAGE": 'sendInfo',
        "send-func": test,
        "file-func": test,
        "app": app
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
    ui = MainPage(**test_info, **d)
    ui.setupUi(MainWindow)
    ui.participants = p
    ui.update_board()
    MainWindow.show()
    # input()
    ui.start_timer()
    sys.exit(app.exec_())
