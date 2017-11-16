# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import json

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(645, 375)
        self.settingsFile = open("settings.json","r")
        self.jsonFile = json.loads(self.settingsFile.read())
        self.firefoxPath = self.jsonFile["browser"]["firefox"]
        self.chromePath = self.jsonFile["browser"]["chrome"]
        self.IEPath = self.jsonFile["browser"]["IE"]
        self.operaPath = self.jsonFile["browser"]["opera"]
        self.playerPath = self.jsonFile["media"]["player"]
        self.mp3Path = self.jsonFile["media"]["mp3"]
        self.videoPath = self.jsonFile["media"]["video"]
        self.settingsFile.close()

        self.youtubesettingsFile = open("settings\download.json","r")
        self.youtubejsonFile = json.loads(self.youtubesettingsFile.read())
        self.yotutbeDownloadOutput = self.youtubejsonFile["option"]["output"]
        self.youtubesettingsFile.close()
        
        self.confirmBox = QtGui.QDialogButtonBox(Dialog)
        self.confirmBox.setGeometry(QtCore.QRect(10, 320, 621, 32))
        self.confirmBox.setOrientation(QtCore.Qt.Horizontal)
        self.confirmBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.confirmBox.setObjectName(_fromUtf8("confirmBox"))
        self.confirmBox.clicked.connect(self.confirmButton)
        
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(30, 20, 601, 281))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.chromeLine = QtGui.QLineEdit(self.tab)
        self.chromeLine.setGeometry(QtCore.QRect(108, 61, 414, 20))
        self.chromeLine.setObjectName(_fromUtf8("chromeLine"))
        self.chromeLabel = QtGui.QLabel(self.tab)
        self.chromeLabel.setGeometry(QtCore.QRect(50, 64, 46, 13))
        self.chromeLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.chromeLabel.setObjectName(_fromUtf8("chromeLabel"))
        self.operaLabel = QtGui.QLabel(self.tab)
        self.operaLabel.setGeometry(QtCore.QRect(50, 127, 46, 13))
        self.operaLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.operaLabel.setObjectName(_fromUtf8("operaLabel"))
        self.OperaLine = QtGui.QLineEdit(self.tab)
        self.OperaLine.setGeometry(QtCore.QRect(108, 129, 414, 20))
        self.OperaLine.setObjectName(_fromUtf8("OperaLine"))
        self.firefoxLine = QtGui.QLineEdit(self.tab)
        self.firefoxLine.setGeometry(QtCore.QRect(108, 27, 414, 20))
        self.firefoxLine.setObjectName(_fromUtf8("firefoxLine"))
        self.IELine = QtGui.QLineEdit(self.tab)
        self.IELine.setGeometry(QtCore.QRect(108, 94, 414, 20))
        self.IELine.setObjectName(_fromUtf8("IELine"))
        self.IELabel = QtGui.QLabel(self.tab)
        self.IELabel.setGeometry(QtCore.QRect(50, 97, 46, 13))
        self.IELabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.IELabel.setObjectName(_fromUtf8("IELabel"))
        self.firefoxLabel = QtGui.QLabel(self.tab)
        self.firefoxLabel.setGeometry(QtCore.QRect(50, 30, 46, 13))
        self.firefoxLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.firefoxLabel.setObjectName(_fromUtf8("firefoxLabel"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.mp3Line = QtGui.QLineEdit(self.tab_2)
        self.mp3Line.setGeometry(QtCore.QRect(98, 20, 414, 20))
        self.mp3Line.setObjectName(_fromUtf8("mp3Line"))
        self.mp3Label = QtGui.QLabel(self.tab_2)
        self.mp3Label.setGeometry(QtCore.QRect(40, 23, 46, 13))
        self.mp3Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.mp3Label.setObjectName(_fromUtf8("mp3Label"))
        self.videoLine = QtGui.QLineEdit(self.tab_2)
        self.videoLine.setGeometry(QtCore.QRect(98, 57, 414, 20))
        self.videoLine.setObjectName(_fromUtf8("videoLine"))
        self.videoLabel = QtGui.QLabel(self.tab_2)
        self.videoLabel.setGeometry(QtCore.QRect(30, 60, 61, 16))
        self.videoLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.videoLabel.setObjectName(_fromUtf8("videoLabel"))
        self.playerLine = QtGui.QLineEdit(self.tab_2)
        self.playerLine.setGeometry(QtCore.QRect(98, 93, 414, 20))
        self.playerLine.setObjectName(_fromUtf8("playerLine"))
        self.playerLabel = QtGui.QLabel(self.tab_2)
        self.playerLabel.setGeometry(QtCore.QRect(30, 94, 61, 20))
        self.playerLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.playerLabel.setObjectName(_fromUtf8("playerLabel"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.yotubeDownloadPathLine = QtGui.QLineEdit(self.tab_2)
        self.yotubeDownloadPathLine.setGeometry(QtCore.QRect(152, 129, 361, 20))
        self.yotubeDownloadPathLine.setObjectName(_fromUtf8("yotubeDownloadPathLine"))
        self.yotubeDownloadPathLabel = QtGui.QLabel(self.tab_2)
        self.yotubeDownloadPathLabel.setGeometry(QtCore.QRect(30, 130, 114, 20))
        self.yotubeDownloadPathLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.yotubeDownloadPathLabel.setObjectName(_fromUtf8("playerLabel"))
#---------------------------------------setText------------------------------------
        self.firefoxLine.setText(self.firefoxPath)
        self.chromeLine.setText(self.chromePath)
        self.IELine.setText(self.IEPath)
        self.OperaLine.setText(self.operaPath)
        self.playerLine.setText(self.playerPath)
        self.mp3Line.setText(self.mp3Path)
        self.videoLine.setText(self.videoPath)
        self.yotubeDownloadPathLine.setText(self.yotutbeDownloadOutput)
#------------------------------------------------------------------------------------
        
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)

        QtCore.QObject.connect(self.confirmBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.confirmBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.chromeLabel.setText(_translate("Dialog", "Chrome", None))
        self.operaLabel.setText(_translate("Dialog", "Opera", None))
        self.IELabel.setText(_translate("Dialog", "IE", None))
        self.firefoxLabel.setText(_translate("Dialog", "Firefox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tab 1", None))
        self.mp3Label.setText(_translate("Dialog", "Mp3 Path", None))
        self.videoLabel.setText(_translate("Dialog", "Video Path", None))
        self.playerLabel.setText(_translate("Dialog", "Music Player", None))
        self.yotubeDownloadPathLabel.setText(_translate("Dialog", "Youtube Download Path", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2", None))


    def confirmButton(self, button):
        sb = self.confirmBox.standardButton(button)
        if sb == QtGui.QDialogButtonBox.Ok:
            self.firefoxText = self.firefoxLine.text()
            self.chromeText = self.chromeLine.text()
            self.IEText = self.IELine.text()
            self.operaText = self.OperaLine.text()
            self.playerText = self.playerLine.text()
            self.mp3Text = self.mp3Line.text()
            self.videoText = self.videoLine.text()
            self.yotubeDownloadPathText = self.yotubeDownloadPathLine.text()
            self.jsonFileRead = open("settings.json","r")
            self.jsonFileData = json.loads(self.jsonFileRead.read())
            self.jsonFileData["browser"]["firefox"] = self.firefoxText
            self.jsonFileData["browser"]["chrome"] = self.chromeText
            self.jsonFileData["browser"]["IE"] = self.IEText
            self.jsonFileData["browser"]["opera"] = self.operaText
            self.jsonFileData["media"]["player"] = self.playerText
            self.jsonFileData["media"]["mp3"] = self.mp3Text
            self.jsonFileData["media"]["video"] = self.videoText
            self.jsonFileRead.close()

            self.settingsWrite = open("settings.json","w")
            json.dump(self.jsonFileData, self.settingsWrite)
            self.settingsWrite.close()

            self.yotutubejsonFileRead = open("settings\download.json","r")
            self.yotutubejsonFileData = json.loads(self.yotutubejsonFileRead.read())
            self.yotutubejsonFileData["option"]["output"] = self.yotubeDownloadPathText
            self.jsonFileRead.close()
            self.yotutubesettingsWrite = open("settings\download.json","w")
            json.dump(self.yotutubejsonFileData, self.yotutubesettingsWrite)
            self.yotutubesettingsWrite.close()
            
        elif sb == QtGui.QDialogButtonBox.Cancel:
            pass
