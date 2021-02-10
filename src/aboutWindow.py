# About Window
#
# Created by: nbebaw

from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("About")
        MainWindow.resize(400, 170)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 170))
        MainWindow.setMaximumSize(QtCore.QSize(400, 170))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        path = os.path.dirname(os.path.abspath(__file__))
        icon = QtGui.QIcon(os.path.join(path, "icons/icon.png"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("About")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 60, 60))
        self.label.setMinimumSize(QtCore.QSize(60, 60))
        self.label.setMaximumSize(QtCore.QSize(60, 60))
        self.label.setSizeIncrement(QtCore.QSize(60, 60))
        self.label.setBaseSize(QtCore.QSize(60, 60))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(os.path.join(path, "icons/icon.png")))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(217, 71, 60, 30))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 100, 331, 51))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("About", "About"))
        self.label_2.setText(_translate("About", "Boost Changer"))
        self.label_3.setText(_translate("About", "v0.1.1"))
        self.label_4.setText(_translate("About", "Tray application to control CPU turbo boost in order \nto consuming less battery voltage on Linux"))
