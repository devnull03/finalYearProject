from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
import time

from PyQt5.QtWidgets import QWidget

class MainPage(object):
    def __init__(self, **kwargs):
        self.mode = kwargs["mode"]
        self.task = kwargs["task"]
        self.time = kwargs["time"]
        ex = kwargs["examples"]
        self.examples_list = "\n".join(
            f"solution({i})-> {ex[i]}" for i in ex
        )
        self.start = False
        self.count = self.time*60

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
        
        main_font = QtGui.QFont()
        main_font.setFamily("Times New Roman")
        main_font.setPointSize(15)
        MainWindow.setFont(main_font)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Timer = QtWidgets.QLabel(self.centralwidget)
        self.Timer.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.Timer.setAlignment(QtCore.Qt.AlignCenter)
        self.Timer.setObjectName("Timer")
        
        self.task_container = QtWidgets.QScrollArea(self.centralwidget)
        self.task_container.setGeometry(QtCore.QRect(20, 110, 421, 201))
        self.task_container.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.task_container.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.task_container.setWidgetResizable(False)
        self.task_container.setObjectName("task_container")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 419, 279))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.task_desc = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.task_desc.setGeometry(QtCore.QRect(10, 10, 381, 351))
        font_13 = QtGui.QFont()
        font_13.setPointSize(13)
        self.task_desc.setFont(font_13)
        self.task_desc.setTextFormat(QtCore.Qt.AutoText)
        self.task_desc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.task_desc.setWordWrap(True)
        self.task_desc.setObjectName("task_desc")
        self.task_container.setWidget(self.scrollAreaWidgetContents)
        
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
        font = QtGui.QFont()
        font.setPointSize(19)
        self.Task.setFont(font)
        self.Task.setObjectName("Task")
        
        self.Examples = QtWidgets.QLabel(self.centralwidget)
        self.Examples.setGeometry(QtCore.QRect(20, 325, 111, 31))
        self.Examples.setObjectName("Examples")
        self.example_container = QtWidgets.QScrollArea(self.centralwidget)
        self.example_container.setGeometry(QtCore.QRect(20, 360, 421, 131))
        self.example_container.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.example_container.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.example_container.setWidgetResizable(False)
        self.example_container.setObjectName("example_container")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 419, 279))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.examples = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.examples.setGeometry(QtCore.QRect(10, 10, 401, 151))
        self.examples.setFont(font_13)
        self.examples.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.examples.setWordWrap(True)
        self.examples.setObjectName("examples")
        self.example_container.setWidget(self.scrollAreaWidgetContents_2)
        
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
        self.finish_button.clicked.connect(self.start_timer)

        self.select_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_button.setGeometry(QtCore.QRect(260, 560, 71, 31))
        self.select_button.setFont(font)
        self.select_button.setObjectName("select_button")
        self.select_button.clicked.connect(lambda: self.showDialog(MainWindow))
        
        timer = QtCore.QTimer(MainWindow)
        timer.timeout.connect(self.showTime) 
        timer.start(1000)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clash of Code"))
        self.Timer.setText(_translate("MainWindow", f"{self.time}:00"))
        self.task_desc.setText(_translate("MainWindow", self.task))
        self.Mode.setText(_translate("MainWindow", f"Mode : {self.mode}"))
        self.Task.setText(_translate("MainWindow", "Task"))
        self.Examples.setText(_translate("MainWindow", "Examples"))
        self.examples.setText(_translate("MainWindow", self.examples_list))
        self.Select_file.setText(_translate("MainWindow", "Select File"))
        self.finish_button.setText(_translate("MainWindow", "Finish"))
        self.select_button.setText(_translate("MainWindow", "Select"))

    def showDialog(self, MainWindow):
        home_dir = str(Path.home())
        fname = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open file', home_dir, "python files (*.py)")
        # print(fname)
        self.file.setText(fname[0])
  
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
    test_info = {
        "mode": "Shortest",
        "time": 1,
        "task": "Test task " * 10,
        "examples": {
            1: 1,
            2: 4,
            3: 9
        }
    }
    ui = MainPage(**test_info)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
