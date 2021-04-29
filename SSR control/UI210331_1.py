# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI210331_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(150, 122, 514, 359))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.TextCOM = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.TextCOM.setFont(font)
        self.TextCOM.setObjectName("TextCOM")
        self.gridLayout.addWidget(self.TextCOM, 3, 0, 1, 1)
        self.pbstart = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        self.pbstart.setFont(font)
        self.pbstart.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pbstart.setMouseTracking(False)
        self.pbstart.setObjectName("pbstart")
        self.gridLayout.addWidget(self.pbstart, 4, 0, 1, 1)
        self.pbquit = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        self.pbquit.setFont(font)
        self.pbquit.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pbquit.setMouseTracking(False)
        self.pbquit.setObjectName("pbquit")
        self.gridLayout.addWidget(self.pbquit, 4, 2, 1, 1)
        self.pbstop = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        self.pbstop.setFont(font)
        self.pbstop.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pbstop.setMouseTracking(False)
        self.pbstop.setObjectName("pbstop")
        self.gridLayout.addWidget(self.pbstop, 4, 1, 1, 1)
        self.TextLoop = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.TextLoop.setFont(font)
        self.TextLoop.setObjectName("TextLoop")
        self.gridLayout.addWidget(self.TextLoop, 2, 0, 1, 1)
        self.TextCloseTime = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.TextCloseTime.setFont(font)
        self.TextCloseTime.setObjectName("TextCloseTime")
        self.gridLayout.addWidget(self.TextCloseTime, 1, 0, 1, 1)
        self.TextOpenTime = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.TextOpenTime.setFont(font)
        self.TextOpenTime.setObjectName("TextOpenTime")
        self.gridLayout.addWidget(self.TextOpenTime, 0, 0, 1, 1)
        self.OpenTimeLeft = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.OpenTimeLeft.setFont(font)
        self.OpenTimeLeft.setObjectName("OpenTimeLeft")
        self.gridLayout.addWidget(self.OpenTimeLeft, 0, 2, 1, 1)
        self.CloseTimeLeft = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.CloseTimeLeft.setFont(font)
        self.CloseTimeLeft.setObjectName("CloseTimeLeft")
        self.gridLayout.addWidget(self.CloseTimeLeft, 1, 2, 1, 1)
        self.TimesLeft = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.TimesLeft.setFont(font)
        self.TimesLeft.setObjectName("TimesLeft")
        self.gridLayout.addWidget(self.TimesLeft, 2, 2, 1, 1)
        self.opentime = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.opentime.setFont(font)
        self.opentime.setObjectName("opentime")
        self.gridLayout.addWidget(self.opentime, 0, 1, 1, 1)
        self.closetime = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.closetime.setFont(font)
        self.closetime.setObjectName("closetime")
        self.gridLayout.addWidget(self.closetime, 1, 1, 1, 1)
        self.loop = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.loop.setFont(font)
        self.loop.setObjectName("loop")
        self.gridLayout.addWidget(self.loop, 2, 1, 1, 1)
        self.com = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.com.setFont(font)
        self.com.setObjectName("com")
        self.gridLayout.addWidget(self.com, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 23))
        self.menubar.setObjectName("menubar")
        self.menuUV_controler = QtWidgets.QMenu(self.menubar)
        self.menuUV_controler.setObjectName("menuUV_controler")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuUV_controler.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TextCOM.setText(_translate("MainWindow", "COM:"))
        self.pbstart.setText(_translate("MainWindow", "Start"))
        self.pbquit.setText(_translate("MainWindow", "Quit"))
        self.pbstop.setText(_translate("MainWindow", "Stop"))
        self.TextLoop.setText(_translate("MainWindow", "Loop:"))
        self.TextCloseTime.setText(_translate("MainWindow", "CloseTime:"))
        self.TextOpenTime.setText(_translate("MainWindow", "OpenTime:"))
        self.OpenTimeLeft.setText(_translate("MainWindow", "/s"))
        self.CloseTimeLeft.setText(_translate("MainWindow", "/s"))
        self.TimesLeft.setText(_translate("MainWindow", "/Times"))
        self.opentime.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.closetime.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.loop.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.com.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">COM4</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuUV_controler.setTitle(_translate("MainWindow", "UV controller"))