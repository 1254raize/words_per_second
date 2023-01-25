# Form implementation generated from reading ui file 'words_per_second.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 617)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.typed_text = QtWidgets.QTextEdit(self.centralwidget)
        self.typed_text.setGeometry(QtCore.QRect(40, 310, 471, 241))
        self.typed_text.setObjectName("typed_text")
        self.text_to_type = QtWidgets.QLabel(self.centralwidget)
        self.text_to_type.setGeometry(QtCore.QRect(40, 30, 471, 241))
        self.text_to_type.setStyleSheet("border: 2px double gray")
        self.text_to_type.setText("")
        self.text_to_type.setWordWrap(True)
        self.text_to_type.setObjectName("text_to_type")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(560, 180, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("border: 2px solid;\n"
"border-radius: 10px;\n"
"background-color: lightgreen")
        self.start_button.setObjectName("start_button")
        self.timer = QtWidgets.QLCDNumber(self.centralwidget)
        self.timer.setGeometry(QtCore.QRect(560, 30, 141, 121))
        self.timer.setDigitCount(2)
        self.timer.setProperty("value", 60.0)
        self.timer.setObjectName("timer")
        self.text_results = QtWidgets.QLabel(self.centralwidget)
        self.text_results.setGeometry(QtCore.QRect(560, 450, 141, 101))
        self.text_results.setStyleSheet("border: 2px double gray")
        self.text_results.setText("")
        self.text_results.setObjectName("text_results")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(560, 320, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.stop_button.setFont(font)
        self.stop_button.setStyleSheet("border: 2px solid;\n"
"border-radius: 10px;\n"
"background-color: crimson")
        self.stop_button.setObjectName("stop_button")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 280, 471, 21))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "START"))
        self.stop_button.setText(_translate("MainWindow", "STOP"))