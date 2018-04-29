# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from settings import Ui_Dialog as settingDailog
import webbrowser as wb
import os
import subprocess
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import glob2
import json
import re
from bs4 import  BeautifulSoup
import requests
#import pyttsx
import string
from multiprocessing import Queue
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #self.engine = pyttsx.init()
        #self.engine.setProperty('rate', 140)
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
        self.surl = 'https://google.com/search?q='
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        #MainWindow.resize(415, 150)
        MainWindow.setFixedSize(415, 150)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.center()
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setGeometry(5,5,60,40)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))


#---------------------------------------------------------YoutubeDownloadBox----------------------------------------
        youtubeDownloaderButtonIcon = QtGui.QIcon()
        youtubeDownloaderButtonIcon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/_download.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)


        self.youtubeDownloaderBox = QtGui.QGroupBox(self.centralwidget)
        self.youtubeDownloaderBox.setGeometry(QtCore.QRect(0, 0, 401, 111))
        self.youtubeDownloaderBox.setTitle(_fromUtf8(""))
        self.youtubeDownloaderBox.setObjectName(_fromUtf8("youtubeDownloaderBox"))
        
        self.youtubeAudioButton = QtGui.QRadioButton(self.youtubeDownloaderBox)
        self.youtubeAudioButton.setGeometry(QtCore.QRect(210, 60, 61, 17))
        self.youtubeAudioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.youtubeAudioButton.setObjectName(_fromUtf8("youtubeVideoButton"))

        self.youtubeDowloadButton = QtGui.QPushButton(self.youtubeDownloaderBox)
        self.youtubeDowloadButton.setGeometry(QtCore.QRect(320, 20, 75, 23))
        self.youtubeDowloadButton.setIcon(youtubeDownloaderButtonIcon)
        self.youtubeDowloadButton.setObjectName(_fromUtf8("youtubeDowloadButton"))

        
        self.youtubeVideoComboBox = QtGui.QComboBox(self.youtubeDownloaderBox)
        self.youtubeVideoComboBox.setGeometry(QtCore.QRect(10, 20, 81, 22))
        self.youtubeVideoComboBox.setObjectName(_fromUtf8("youtubeVideoComboBox"))
        self.youtubeVideoComboBox.addItem(_fromUtf8(""))
        self.youtubeVideoComboBox.addItem(_fromUtf8(""))
        self.youtubeVideoComboBox.addItem(_fromUtf8(""))
        self.youtubeVideoComboBox.addItem(_fromUtf8(""))
        self.youtubeVideoComboBox.addItem(_fromUtf8(""))
        self.youtubeVideoComboBox.addItem(_fromUtf8(""))
        self.youtubeVideoComboBox.addItem(_fromUtf8(""))
        self.youtubeVideoComboBox.addItem(_fromUtf8(""))
        self.youtubeVideoComboBox.addItem(_fromUtf8(""))

        self.youtubeVideoButton = QtGui.QRadioButton(self.youtubeDownloaderBox)
        self.youtubeVideoButton.setGeometry(QtCore.QRect(130, 60, 61, 17))
        self.youtubeVideoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.youtubeVideoButton.setObjectName(_fromUtf8("youtubeAudioButton"))

        self.youtubeUrlLine = QtGui.QLineEdit(self.youtubeDownloaderBox)
        self.youtubeUrlLine.setGeometry(QtCore.QRect(100, 20, 211, 21))
        self.youtubeUrlLine.setAutoFillBackground(False)
        self.youtubeUrlLine.setObjectName(_fromUtf8("youtubeUrlLine"))

        
        self.youtubeAudioComboBox = QtGui.QComboBox(self.youtubeDownloaderBox)
        self.youtubeAudioComboBox.setGeometry(QtCore.QRect(10, 20, 81, 22))
        self.youtubeAudioComboBox.setObjectName(_fromUtf8("youtubeAudioComboBox"))
        self.youtubeAudioComboBox.addItem(_fromUtf8(""))
        self.youtubeAudioComboBox.addItem(_fromUtf8(""))
        self.youtubeAudioComboBox.addItem(_fromUtf8(""))


#----------------------------------------------------------TvShowBox-------------------------------------------------
        self.tvshowBox = QtGui.QGroupBox(self.centralwidget)
        self.tvshowBox.setGeometry(QtCore.QRect(0, 0, 401, 111))
        self.tvshowBox.setTitle(_fromUtf8(""))
        self.tvshowBox.setObjectName(_fromUtf8("tvshowBox"))
        self.showNameLine = QtGui.QLineEdit(self.tvshowBox)
        self.showNameLine.setGeometry(QtCore.QRect(20, 40, 151, 21))
        self.showNameLine.setObjectName(_fromUtf8("showNameLine"))
        self.showSeasonLine = QtGui.QLineEdit(self.tvshowBox)
        self.showSeasonLine.setGeometry(QtCore.QRect(180, 40, 61, 20))
        self.showSeasonLine.setObjectName(_fromUtf8("showSeasonLine"))
        self.showEpLine = QtGui.QLineEdit(self.tvshowBox)
        self.showEpLine.setGeometry(QtCore.QRect(250, 40, 51, 20))
        self.showEpLine.setObjectName(_fromUtf8("showEpLine"))
        self.showNameLabel = QtGui.QLabel(self.tvshowBox)
        self.showNameLabel.setGeometry(QtCore.QRect(69, 20, 61, 16))
        self.showNameLabel.setObjectName(_fromUtf8("showNameLabel"))
        self.showSeasonLabel = QtGui.QLabel(self.tvshowBox)
        self.showSeasonLabel.setGeometry(QtCore.QRect(192, 20, 46, 13))
        self.showSeasonLabel.setObjectName(_fromUtf8("showSeasonLabel"))
        self.showEpLabel = QtGui.QLabel(self.tvshowBox)
        self.showEpLabel.setGeometry(QtCore.QRect(257, 20, 51, 16))
        self.showEpLabel.setObjectName(_fromUtf8("showEpLabel"))
        self.showServerBox = QtGui.QComboBox(self.tvshowBox)
        self.showServerBox.setGeometry(QtCore.QRect(310, 40, 81, 22))
        self.showServerBox.setObjectName(_fromUtf8("showServerBox"))
        self.showServerBox.addItem(_fromUtf8(""))
        self.showServerBox.addItem(_fromUtf8(""))
        self.showServerBox.addItem(_fromUtf8(""))
        self.showServerBox.addItem(_fromUtf8(""))
        self.showDownloadButton = QtGui.QPushButton(self.tvshowBox)
        self.showDownloadButton.setGeometry(QtCore.QRect(100, 70, 75, 23))
        self.showDownloadButton.setObjectName(_fromUtf8("showDownloadButton"))
        self.showWatchButton = QtGui.QPushButton(self.tvshowBox)
        self.showWatchButton.setGeometry(QtCore.QRect(210, 70, 75, 23))
        self.showWatchButton.setObjectName(_fromUtf8("showWatchButton"))

        
#-----------------------------------------SearchBox------------------------------------------------------------------
        self.searchBox = QtGui.QGroupBox(self.centralwidget)
        self.searchBox.setGeometry(QtCore.QRect(0, 0, 421, 101))
        self.searchBox.setTitle(_fromUtf8(""))
        self.searchBox.setObjectName(_fromUtf8("searchBox"))
        self.lineEdit = QtGui.QLineEdit(self.searchBox)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 211, 21))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.searchBox)
        self.pushButton.setGeometry(QtCore.QRect(330, 20, 75, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox = QtGui.QGroupBox(self.searchBox)
        self.groupBox.setGeometry(QtCore.QRect(40, 50, 341, 41))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.defaultButton = QtGui.QRadioButton(self.groupBox)
        self.defaultButton.setGeometry(QtCore.QRect(20, 10, 61, 17))
        self.defaultButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.defaultButton.setObjectName(_fromUtf8("defaultButton"))
        self.chromeButton = QtGui.QRadioButton(self.groupBox)
        self.chromeButton.setGeometry(QtCore.QRect(90, 10, 61, 17))
        self.chromeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chromeButton.setObjectName(_fromUtf8("chromeButton"))
        self.firefoxButton = QtGui.QRadioButton(self.groupBox)
        self.firefoxButton.setGeometry(QtCore.QRect(160, 10, 61, 17))
        self.firefoxButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.firefoxButton.setObjectName(_fromUtf8("firefoxButton"))
        self.IEButton = QtGui.QRadioButton(self.groupBox)
        self.IEButton.setGeometry(QtCore.QRect(230, 10, 41, 17))
        self.IEButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.IEButton.setObjectName(_fromUtf8("IEButton"))
        self.operaButton = QtGui.QRadioButton(self.groupBox)
        self.operaButton.setGeometry(QtCore.QRect(280, 10, 51, 17))
        self.operaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.operaButton.setObjectName(_fromUtf8("operaButton"))

#--------------------------------------------------------Box-------------------------------------------------------
        self.sitesBox = QtGui.QComboBox(self.searchBox)
        self.sitesBox.setGeometry(QtCore.QRect(20, 20, 81, 22))
        self.sitesBox.setObjectName(_fromUtf8("sitesBox"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/search/_google.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sitesBox.addItem(icon1, _fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/search/_wikipedia.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sitesBox.addItem(icon2, _fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/search/_bing.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sitesBox.addItem(icon3, _fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/search/_youtube.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sitesBox.addItem(icon4, _fromUtf8(""))
        self.sitesBox.activated.connect(lambda: self.cbText("search"))
        self.sitesBox.setVisible(True)

        self.shoppingBox = QtGui.QComboBox(self.searchBox)
        self.shoppingBox.setGeometry(QtCore.QRect(20, 20, 81, 22))
        self.shoppingBox.setObjectName(_fromUtf8("shoppingBox"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/shopping/_amazon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shoppingBox.addItem(icon1, _fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/shopping/_flipkart.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shoppingBox.addItem(icon2, _fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/shopping/_ebay.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shoppingBox.addItem(icon3, _fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/shopping/_snapdeal.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shoppingBox.addItem(icon4, _fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icons/shopping/_jabong.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shoppingBox.addItem(icon5, _fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("icons/shopping/_myntra.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shoppingBox.addItem(icon6, _fromUtf8(""))
        self.shoppingBox.activated.connect(lambda: self.cbText("shopping"))
        self.shoppingBox.setVisible(False)

        self.musicBox = QtGui.QComboBox(self.searchBox)
        self.musicBox.setGeometry(QtCore.QRect(20, 20, 81, 22))
        self.musicBox.setObjectName(_fromUtf8("musicBox"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/music/_gaana.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.musicBox.addItem(icon1, _fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/music/_hungama.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.musicBox.addItem(icon2, _fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/music/_soundcloud.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.musicBox.addItem(icon3, _fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/music/_saavn.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.musicBox.addItem(icon4, _fromUtf8(""))
        self.musicBox.activated.connect(lambda: self.cbText("music"))
        self.musicBox.setVisible(False)

        self.playBox = QtGui.QComboBox(self.searchBox)
        self.playBox.setGeometry(QtCore.QRect(20, 20, 81, 22))
        self.playBox.setObjectName(_fromUtf8("playBox"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/play/_video.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playBox.addItem(icon1, _fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/play/_mp3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playBox.addItem(icon2, _fromUtf8(""))
        self.playBox.activated.connect(lambda: self.cbText("play"))
        self.playBox.setVisible(False)

        
#--------------------------------ToolBar---------------------------------------------------------
        self.searchAction = QAction(QIcon("icons/white/_search.png"),"&Search",self)
        self.searchAction.setShortcut("Ctrl+s")
        self.searchAction.triggered.connect(self.searchToolbar)
        
        self.shoppingAction = QAction(QIcon("icons/white/_shopping.png"),"&Shopping",self)
        self.shoppingAction.setShortcut("Ctrl+p")
        self.shoppingAction.triggered.connect(self.shoppingToolbar)
        
        self.musicAction = QAction(QIcon("icons/white/_music.png"),"&Music",self)
        self.musicAction.setShortcut("Ctrl+m")
        self.musicAction.triggered.connect(self.musicToolbar)

        self.playAction = QAction(QIcon("icons/white/_play.png"),"&Play Songs",self)
        self.playAction.setShortcut("Ctrl+Shift+p")
        self.playAction.triggered.connect(self.playToolbar)
        
        self.tvshowAction = QAction(QIcon("icons/white/_tv.png"),"&TV Shows",self)
        self.tvshowAction.setShortcut("Ctrl+Shift+s")
        self.tvshowAction.triggered.connect(self.tvshowToolbar)

        self.youtubeDownloaderAction = QAction(QIcon("icons/white/_youtube.png"),"&Youtube Downloader",self)
        self.youtubeDownloaderAction.setShortcut("Ctrl+Shift+s")
        self.youtubeDownloaderAction.triggered.connect(self.youtubeDownloaderToolbar)
        
        self.settingAction = QAction(QIcon("icons/white/_settings.png"),"&Settings",self)
        self.settingAction.setShortcut("Ctrl+Shift+s")
        self.settingAction.triggered.connect(self.settingToolbar)


        
        self._toolbar = self.addToolBar("Menu")
        self._toolbar.addAction(self.searchAction)
        self._toolbar.addAction(self.shoppingAction)
        self._toolbar.addAction(self.musicAction)
        self._toolbar.addAction(self.playAction)
        self._toolbar.addAction(self.tvshowAction)
        self._toolbar.addAction(self.youtubeDownloaderAction)
        self._toolbar.addAction(self.settingAction)        
        
#---------------------------------------------Cursor---------------------------------------------------
        self.defaultButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chromeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.firefoxButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.IEButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.operaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

#---------------------------------------------Toggled Buttons-------------------------------------------
        self.defaultButton.toggled.connect(self.btnstate)
        self.defaultButton.setChecked(True)
        self.chromeButton.toggled.connect(self.btnstate)
        self.firefoxButton.toggled.connect(self.btnstate)
        self.IEButton.toggled.connect(self.btnstate)
        self.operaButton.toggled.connect(self.btnstate)
        #self.lineEdit.textChanged.connect(lambda: self.ontextChanged(files)) 
        self.lineEdit.returnPressed.connect(self.search)
        self.pushButton.clicked.connect(self.search)
        self.showWatchButton.clicked.connect(lambda: self.TvshowButton("watch"))
        self.showDownloadButton.clicked.connect(lambda: self.TvshowButton("download"))
        self.showServerBox.activated.connect(self.showServer)


#----------------------------------------------------youtube-------------------------------------------
        self.youtubeAudioComboBox.hide()
        self.youtubeVideoButton.setChecked(True)
        
        self.youtubeVideoButton.toggled.connect(lambda:self.youtubeRadiobtnState(self.youtubeVideoButton))
        self.youtubeAudioButton.toggled.connect(lambda:self.youtubeRadiobtnState(self.youtubeAudioButton))
        self.youtubeVideoComboBox.activated.connect(self.youtubeQualityBox)
        self.youtubeAudioComboBox.activated.connect(self.youtubeQualityBox)
        self.showDownloadButton.clicked.connect(lambda: self.TvshowButton("download"))
        self.youtubeDowloadButton.clicked.connect(self.youtubeDowload)
        self.youtubeUrlLine.returnPressed.connect(self.youtubeDowload)
#------------------------------------------------GroupBox----------------------------------------------
        self.searchBox.setStyleSheet("QGroupBox {  border: 0px}")
        self.groupBox.setStyleSheet("QGroupBox {border: 1px solid gray;}")
        self.tvshowBox.setStyleSheet("QGroupBox { border: 0px;}")
        self.youtubeDownloaderBox.setStyleSheet("QGroupBox { border: 0px;}")
        self.searchBox.show()
        self.tvshowBox.hide()
        self.youtubeDownloaderBox.hide()
        
#-------------------------------------------------PlaceHolder------------------------------------------
        self.lineEdit.setPlaceholderText("Seach Aything")
        self.showNameLine.setPlaceholderText("Enter Show Name")
        self.showSeasonLine.setPlaceholderText("1-100")
        self.showEpLine.setPlaceholderText("1-100")
                
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CP Search", None))
        #self.groupBox.setTitle(_translate("MainWindow", "GroupBox", None))
        self.defaultButton.setText(_translate("MainWindow", "Default", None))
        self.chromeButton.setText(_translate("Chrome", "Chrome", None))
        self.firefoxButton.setText(_translate("MainWindow", "Firefox", None))
        self.IEButton.setText(_translate("MainWindow", "IE", None))
        self.operaButton.setText(_translate("MainWindow", "Opera", None))
        self.pushButton.setText(_translate("MainWindow", "Search", None))
        self.sitesBox.setItemText(0, _translate("MainWindow", "Google", None))
        self.sitesBox.setItemText(1, _translate("MainWindow", "Wikipedia", None))
        self.sitesBox.setItemText(2, _translate("MainWindow", "Bing", None))
        self.sitesBox.setItemText(3, _translate("MainWindow", "Youtube", None))
        self.shoppingBox.setItemText(0, _translate("MainWindow", "Amazon", None))
        self.shoppingBox.setItemText(1, _translate("MainWindow", "Flipkart", None))
        self.shoppingBox.setItemText(2, _translate("MainWindow", "Ebay", None))
        self.shoppingBox.setItemText(3, _translate("MainWindow", "Snapdeal", None))
        self.shoppingBox.setItemText(4, _translate("MainWindow", "Jabong", None))
        self.shoppingBox.setItemText(5, _translate("MainWindow", "Myntra", None))
        self.musicBox.setItemText(0, _translate("MainWindow", "Gaana", None))
        self.musicBox.setItemText(1, _translate("MainWindow", "Hungama", None))
        self.musicBox.setItemText(2, _translate("MainWindow", "SoundCloud", None))
        self.musicBox.setItemText(3, _translate("MainWindow", "Saavn", None))
        self.playBox.setItemText(0, _translate("MainWindow", "Mp3", None))
        self.playBox.setItemText(1, _translate("MainWindow", "Video", None))


        self.showNameLabel.setText(_translate("MainWindow", "Show Name", None))
        self.showSeasonLabel.setText(_translate("MainWindow", "Season", None))
        self.showEpLabel.setText(_translate("MainWindow", "Episode", None))
        self.showServerBox.setItemText(0, _translate("MainWindow", "Server 01", None))
        self.showServerBox.setItemText(1, _translate("MainWindow", "Server 02", None))
        self.showServerBox.setItemText(2, _translate("MainWindow", "Server 03", None))
        self.showServerBox.setItemText(3, _translate("MainWindow", "Server 04", None))
        self.showDownloadButton.setText(_translate("MainWindow", "Download", None))
        self.showWatchButton.setText(_translate("MainWindow", "Watch", None))
        self.youtubeAudioButton.setText(_translate("MainWindow", "Audio", None))
        self.youtubeDowloadButton.setText(_translate("MainWindow", "Download", None))
        self.youtubeVideoComboBox.setItemText(0, _translate("MainWindow", "Best Quality", None))
        self.youtubeVideoComboBox.setItemText(1, _translate("MainWindow", "4K", None))
        self.youtubeVideoComboBox.setItemText(2, _translate("MainWindow", "2K", None))
        self.youtubeVideoComboBox.setItemText(3, _translate("MainWindow", "Full HD", None))
        self.youtubeVideoComboBox.setItemText(4, _translate("MainWindow", "HD", None))
        self.youtubeVideoComboBox.setItemText(5, _translate("MainWindow", "High", None))
        self.youtubeVideoComboBox.setItemText(6, _translate("MainWindow", "Medium", None))
        self.youtubeVideoComboBox.setItemText(7, _translate("MainWindow", "Low", None))
        self.youtubeVideoComboBox.setItemText(8, _translate("MainWindow", "Very Low", None))
        self.youtubeVideoButton.setText(_translate("MainWindow", "Video", None))
        self.youtubeAudioComboBox.setItemText(0, _translate("MainWindow", "Best Quality", None))
        self.youtubeAudioComboBox.setItemText(1, _translate("MainWindow", "160", None))
        self.youtubeAudioComboBox.setItemText(2, _translate("MainWindow", "128", None))

        MainWindow.setWindowIcon(QtGui.QIcon("icons/_search.png"))

    def cbText(self, t):
        self.t = t
        if(self.t == 'search'):
            self.site = (str(self.sitesBox.currentText()))
        elif(self.t == 'shopping'):
            self.site = (str(self.shoppingBox.currentText()))
        elif(self.t == 'music'):
            self.site = (str(self.musicBox.currentText()))
        elif(self.t == 'play'):
            self.site = (str(self.playBox.currentText()))
#----------------------------------------------Search-------------------------------------------------
        if self.site == 'Google':
            self.surl = 'https://google.com/search?q='
        elif self.site == 'Youtube':
            self.surl = "https://www.youtube.com/results?search_query="
        elif self.site == 'Bing':
            self.surl = 'https://www.bing.com/search?q='
        elif self.site == 'Wikipedia':
            self.surl = 'https://en.wikipedia.org/w/index.php?search='

#---------------------------------------------Shopping--------------------------------------------------
        elif self.site == 'Amazon':
            self.surl = 'https://www.amazon.in/s/field-keywords='
        elif self.site == 'Flipkart':
            self.surl = "https://www.flipkart.com/search?q="
        elif self.site == 'Ebay':
            self.surl = 'https://www.ebay.in/sch/i.html?_nkw='
        elif self.site == 'Snapdeal':
            self.surl = 'https://www.snapdeal.com/search?keyword='
        elif self.site == 'Myntra':
            self.surl = 'https://www.myntra.com/'
        elif self.site == 'Jabong':
            self.surl = 'https://www.jabong.com/find/?q='

#-----------------------------------------------Music--------------------------------------------------
        elif self.site == 'Gaana':
            self.surl = 'http://gaana.com/search/'
        elif self.site == 'Hungama':
            self.surl = "http://www.hungama.com/search/"
        elif self.site == 'Soundcloud':
            self.surl = 'https://soundcloud.com/search?q='
        elif self.site == 'Saavn':
            self.surl = 'https://www.saavn.com/search/'


#------------------------------------------------Play---------------------------------------------------
        elif self.site == 'Video':
            self.files = glob2.glob(self.videoPath+'\**\*.mp4')
            self.surl = 'mp4'
        elif self.site == 'Mp3':
            self.files = glob2.glob(self.mp3Path+'\**\*.mp3')
            self.surl = 'mp3'

    def btnstate(self):
        if self.defaultButton.isChecked() == True:
            return 'default'
        elif self.firefoxButton.isChecked() == True:
            return 'firefox'
        elif self.chromeButton.isChecked() == True:
            return 'chrome'
        elif self.IEButton.isChecked() == True:
            return 'IE'
        elif self.operaButton.isChecked() == True:
            return 'opera'

##        if b.text() == "Chrome":
##            if b.isChecked() == True:
##                return (b.text())
##        if b.text() == "Firefox":
##            if b.isChecked() == True:
##                return (b.text())
##        if b.text() == "IE":
##            if b.isChecked() == True:
##                return (b.text())
##        if b.text() == "Opera":
##            if b.isChecked() == True:
##                return (b.text())
##            
    def search(self):
        self.searchText = self.lineEdit.text()
        self.url = self.surl+self.searchText
        self.browser = self.btnstate()

        if(self.surl == 'mp3'):
            for file in self.files:
                if self.searchText.lower() in file.lower():
                    found = file
                    self.statusbar.showMessage(found)
                    subprocess.Popen([self.playerPath, found])

        elif(self.surl == 'mp4'):
            for file in self.files:
                if self.searchText.lower() in file.lower():
                    found = file
                    self.statusbar.showMessage(found)
                    subprocess.Popen([self.playerPath, found])
        else:
            if self.browser == 'default':
                subprocess.Popen([self.firefoxPath,
        '-new-tab', self.url])
            elif self.browser == 'firefox':
                subprocess.Popen([self.firefoxPath,
        '-new-tab', self.url])
            elif self.browser == 'chrome':
                subprocess.Popen([self.chromePath,
        '-new-tab', self.url])
            elif self.browser == 'opera':
                subprocess.Popen([self.operaPath,
        '-new-tab', self.url])
            elif self.browser == 'IE':
                wb.get(self.IEPath).open_new_tab(self.url)
            #rq  = requests.get(self.url)
            #serverdata = rq.text
            #serverSoup = BeautifulSoup(serverdata, 'lxml')
            #find = serverSoup.body.find('p')
            #print(find.text)
            #self.engine.say(find.text)
            #self.engine.runAndWait()


    def TvshowButton(self, cat):
        capsShowName = string.capwords(self.showNameLine.text())
        self.showSearchName = self.showNameLine.text()
        self.showSeasonName = self.showSeasonLine.text()
        self.showEpName = self.showEpLine.text()
        self.server = self.showServer()

        self.statusbar.showMessage("Seaching... | "+ self.showSearchName)
        
        self.searchServer(self.server,self.showSearchName)
        self.statusbar.showMessage("Found Show... | "+ self.showSearchName)
        
        self.searchServer(self.server,self.showSeasonName)
        self.statusbar.showMessage("Found Season "+self.showSeasonName+"...")


        self.searchServer(self.server,"720")
        self.statusbar.showMessage("Found Season "+self.showSeasonName+"...")
    
        self.searchServer(self.server,self.showEpName)
        self.statusbar.showMessage("Found Episode "+self.showEpName+"...")
        if cat == 'watch':        
            subprocess.Popen([self.playerPath, self.server])
        elif cat == 'download':
            subprocess.Popen([r"C:\Program Files (x86)\Internet Download Manager\IDMan.exe","/d", self.server])
        self.statusbar.showMessage("Done.")


    def showServer(self):
        showServer = (str(self.showServerBox.currentText()))
        if showServer == 'Server 01':
            return 'http://dl.funsaber.net/serial/'
        elif showServer == 'Server 02':
            return 'http://dl2.my98music.com/Data/Serial/'
        elif showServer == 'Server 03':
            return 'http://dl.my-film.in/serial/'
        elif showServer == 'Server 04':
            return 'http://dl.tehmovies.com/94/series/'

    def searchToolbar(self):
        self.youtubeDownloaderBox.hide()
        self.searchBox.show()
        self.tvshowBox.hide()
        self.groupBox.show()
        self.sitesBox.setVisible(True)
        self.shoppingBox.setVisible(False)
        self.musicBox.setVisible(False)
        self.playBox.setVisible(False)
        self.searchText = ''
        self.surl = 'https://google.com/search?q='
        
    def shoppingToolbar(self):
        self.youtubeDownloaderBox.hide()
        self.searchBox.show()
        self.tvshowBox.hide()
        self.groupBox.show()
        self.sitesBox.setVisible(False)
        self.shoppingBox.setVisible(True)
        self.musicBox.setVisible(False)
        self.playBox.setVisible(False)
        self.searchText = ''
        self.surl = 'https://www.amazon.in/s/field-keywords='
        
    
    def musicToolbar(self):
        self.searchBox.show()
        self.tvshowBox.hide()
        self.youtubeDownloaderBox.hide()
        self.groupBox.show()
        self.sitesBox.setVisible(False)
        self.shoppingBox.setVisible(False)
        self.musicBox.setVisible(True)
        self.playBox.setVisible(False)
        self.searchText = ''
        self.surl = 'http://gaana.com/search/'

    def playToolbar(self):
        self.searchBox.show()
        self.tvshowBox.hide()
        self.youtubeDownloaderBox.hide()
        self.surl = 'mp3'
        self.sitesBox.setVisible(False)
        self.shoppingBox.setVisible(False)
        self.musicBox.setVisible(False)
        self.playBox.setVisible(True)
        self.groupBox.hide()

    def settingToolbar(self):
        widget = QtGui.QDialog()
        ui = settingDailog()
        ui.setupUi(widget)
        widget.exec_()

    def tvshowToolbar(self):
        self.youtubeDownloaderBox.hide()
        self.searchBox.hide()
        self.tvshowBox.show()

    def youtubeDownloaderToolbar(self):
        self.yotubeDownloadOption = "Video"
        self.videoQuality = "Best Quality"
        self.audioQuality = "Best Quality"
        self.youtubeDownloaderBox.show()
        self.searchBox.hide()
        self.tvshowBox.hide()

    def searchServer(self, server, search):
        rq  = requests.get(server)
        serverdata = rq.text
        serverSoup = BeautifulSoup(serverdata, 'lxml')
        findShowName = serverSoup.body.findAll('a',text=re.compile(search), limit=1)
        for link in findShowName:
            fou = link.get("href")
            self.server = self.server+fou

    def youtubeRadiobtnState(self,b):
        if b.text() == "Video":
            if self.youtubeVideoButton.isChecked() == True:
                self.yotubeDownloadOption = "Video"
                self.youtubeVideoComboBox.show()
                self.youtubeAudioComboBox.hide()
        elif b.text() == "Audio":
            if self.youtubeAudioButton.isChecked() == True:
                self.yotubeDownloadOption = "Audio"
                self.youtubeVideoComboBox.hide()
                self.youtubeAudioComboBox.show()
            
    def youtubeQualityBox(self):
        self.videoQuality = (str(self.youtubeVideoComboBox.currentText()))
        self.audioQuality = (str(self.youtubeAudioComboBox.currentText()))


    def youtubeDowload(self):
        url = self.youtubeUrlLine.text()
        self.jsonFileRead = open("settings\download.json","r")
        self.jsonFileData = json.loads(self.jsonFileRead.read())
        self.jsonFileData["option"]["url"] = url
        self.jsonFileData["option"]["videoQuality"] = self.videoQuality
        self.jsonFileData["option"]["audioQuality"] = self.audioQuality
        self.jsonFileData["option"]["downloadOption"] = self.yotubeDownloadOption
        self.jsonFileRead.close()
        self.settingsWrite = open("settings\download.json","w")
        json.dump(self.jsonFileData, self.settingsWrite)
        self.settingsWrite.close()
        self.statusbar.showMessage("Downloading...")
        subprocess.Popen(['VideoDownload.exe'])

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
