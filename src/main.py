# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proyecto_p2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import APILogger
import APIMethods
import JsonToTopicMap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 842)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Token = QtWidgets.QWidget()
        self.Token.setObjectName("Token")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Token)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 210, 696, 199))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 75 28pt \"Rockwell\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Token)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(360, 10, 367, 191))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("font: 72pt \"Rockwell\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Token)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(390, 420, 331, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setStyleSheet("font: 14pt \"Segoe UI Variable\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(self.Token)
        self.pushButton.setGeometry(QtCore.QRect(460, 650, 93, 28))
        self.pushButton.setObjectName("pushButton")
        # lineEdit -> QLabel
        self.lineEdit = QtWidgets.QLabel(self.Token)
        self.lineEdit.setGeometry(QtCore.QRect(460, 590, 211, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.Token)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 650, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.Token, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(470, 0, 144, 54))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setStyleSheet("font: 28pt \"Rockwell\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 200, 251, 461))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        # self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 247, 457))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listView_3 = QtWidgets.QListView(self.scrollAreaWidgetContents)
        self.listView_3.setGeometry(QtCore.QRect(0, 0, 251, 461))
        self.listView_3.setObjectName("listView_3")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.listView_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(760, 120, 2, 2))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(70, 150, 111, 31))
        self.label_5.setStyleSheet("font: 75 20pt \"Rockwell\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(630, 150, 131, 31))
        self.label_6.setStyleSheet("font: 75 20pt \"Rockwell\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(910, 150, 91, 51))
        self.label_7.setStyleSheet("font: 75 20pt \"Rockwell\";")
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 690, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(50, 90, 701, 31))
        self.label_8.setStyleSheet("font: 12pt \"Segoe UI Variable\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(280, 200, 251, 461))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # self.scrollArea_2 = QtWidgets.QScrollArea(self.horizontalLayoutWidget_3)
        # self.scrollArea_2.setWidgetResizable(True)
        # self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 247, 457))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.listView_4 = QtWidgets.QListView(self.scrollAreaWidgetContents_2)
        self.listView_4.setGeometry(QtCore.QRect(0, 0, 251, 461))
        self.listView_4.setObjectName("listView_4")
        # self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.addWidget(self.listView_4)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(560, 200, 241, 461))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        # self.scrollArea_3 = QtWidgets.QScrollArea(self.horizontalLayoutWidget_4)
        # self.scrollArea_3.setWidgetResizable(True)
        # self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 237, 457))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.listView_5 = QtWidgets.QListView(self.scrollAreaWidgetContents_3)
        self.listView_5.setGeometry(QtCore.QRect(0, 0, 251, 461))
        self.listView_5.setObjectName("listView_5")
        # self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_4.addWidget(self.listView_5)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(830, 200, 251, 461))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        # self.scrollArea_4 = QtWidgets.QScrollArea(self.horizontalLayoutWidget_5)
        # self.scrollArea_4.setWidgetResizable(True)
        # self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 247, 457))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.listView_6 = QtWidgets.QListView(self.scrollAreaWidgetContents_4)
        self.listView_6.setGeometry(QtCore.QRect(0, 0, 251, 461))
        self.listView_6.setObjectName("listView_6")
        # self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_5.addWidget(self.listView_6)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(340, 150, 131, 31))
        self.label_10.setStyleSheet("font: 75 20pt \"Rockwell\";")
        self.label_10.setObjectName("label_10")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 690, 91, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(650, 690, 91, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(920, 690, 91, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(470, 0, 144, 54))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_9.setStyleSheet("font: 28pt \"Rockwell\";")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 140, 241, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab)
        self.pushButton_11.setGeometry(QtCore.QRect(310, 140, 93, 28))
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(50, 240, 991, 461))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.scrollArea_7 = QtWidgets.QScrollArea(self.verticalLayoutWidget_11)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 987, 457))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.listView_7 = QtWidgets.QListView(self.scrollAreaWidgetContents_7)
        self.listView_7.setGeometry(QtCore.QRect(-5, 1, 991, 461))
        self.listView_7.setObjectName("listView_7")
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.verticalLayout_11.addWidget(self.scrollArea_7)
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(50, 90, 701, 31))
        self.label_19.setStyleSheet("font: 12pt \"Segoe UI Variable\";")
        self.label_19.setObjectName("label_19")
        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(470, 0, 144, 54))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_20.setStyleSheet("font: 28pt \"Rockwell\";")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_12.addWidget(self.label_20)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 140, 241, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_12.setGeometry(QtCore.QRect(310, 140, 93, 28))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_13.setGeometry(QtCore.QRect(450, 140, 93, 28))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_14.setGeometry(QtCore.QRect(590, 140, 93, 28))
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_21 = QtWidgets.QLabel(self.tab_5)
        self.label_21.setGeometry(QtCore.QRect(50, 90, 701, 31))
        self.label_21.setStyleSheet("font: 12pt \"Segoe UI Variable\";")
        self.label_21.setObjectName("label_21")
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(50, 240, 991, 461))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.scrollArea_8 = QtWidgets.QScrollArea(self.verticalLayoutWidget_13)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 987, 457))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.listView_8 = QtWidgets.QListView(self.scrollAreaWidgetContents_8)
        self.listView_8.setGeometry(QtCore.QRect(-5, 1, 991, 461))
        self.listView_8.setObjectName("listView_8")
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout_13.addWidget(self.scrollArea_8)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayoutWidget_15 = QtWidgets.QWidget(self.tab_7)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(470, 0, 144, 54))
        self.verticalLayoutWidget_15.setObjectName("verticalLayoutWidget_15")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_15)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.label_23.setStyleSheet("font: 28pt \"Rockwell\";")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_15.addWidget(self.label_23)
        #self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_7)
        #self.lineEdit_5.setGeometry(QtCore.QRect(40, 140, 241, 31))
        #self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_15.setGeometry(QtCore.QRect(310, 140, 93, 28))
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayoutWidget_16 = QtWidgets.QWidget(self.tab_7)
        self.verticalLayoutWidget_16.setGeometry(QtCore.QRect(50, 240, 991, 461))
        self.verticalLayoutWidget_16.setObjectName("verticalLayoutWidget_16")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_16)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.scrollArea_9 = QtWidgets.QScrollArea(self.verticalLayoutWidget_16)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setObjectName("scrollArea_9")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 987, 457))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.listView_9 = QtWidgets.QListView(self.scrollAreaWidgetContents_9)
        self.listView_9.setGeometry(QtCore.QRect(0, 0, 991, 461))
        self.listView_9.setObjectName("listView_9")
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)
        self.verticalLayout_16.addWidget(self.scrollArea_9)
        self.label_24 = QtWidgets.QLabel(self.tab_7)
        self.label_24.setGeometry(QtCore.QRect(50, 90, 701, 31))
        self.label_24.setStyleSheet("font: 12pt \"Segoe UI Variable\";")
        self.label_24.setObjectName("label_24")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(self.tab_6)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(470, 0, 144, 54))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_14)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        self.label_22.setStyleSheet("font: 28pt \"Rockwell\";")
        self.label_22.setObjectName("label_22")
        self.verticalLayout_14.addWidget(self.label_22)
        self.verticalLayoutWidget_17 = QtWidgets.QWidget(self.tab_6)
        self.verticalLayoutWidget_17.setGeometry(QtCore.QRect(180, 240, 311, 401))
        self.verticalLayoutWidget_17.setObjectName("verticalLayoutWidget_17")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_17)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.listView = QtWidgets.QListView(self.verticalLayoutWidget_17)
        self.listView.setObjectName("listView")
        self.verticalLayout_17.addWidget(self.listView)
        self.label_25 = QtWidgets.QLabel(self.tab_6)
        self.label_25.setGeometry(QtCore.QRect(50, 90, 701, 31))
        self.label_25.setStyleSheet("font: 12pt \"Segoe UI Variable\";")
        self.label_25.setObjectName("label_25")
        self.verticalLayoutWidget_18 = QtWidgets.QWidget(self.tab_6)
        self.verticalLayoutWidget_18.setGeometry(QtCore.QRect(590, 240, 311, 401))
        self.verticalLayoutWidget_18.setObjectName("verticalLayoutWidget_18")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_18)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.listView_2 = QtWidgets.QListView(self.verticalLayoutWidget_18)
        self.listView_2.setObjectName("listView_2")
        self.verticalLayout_18.addWidget(self.listView_2)
        self.label_26 = QtWidgets.QLabel(self.tab_6)
        self.label_26.setGeometry(QtCore.QRect(280, 190, 111, 41))
        self.label_26.setStyleSheet("font: 75 20pt \"Rockwell\";")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_6)
        self.label_27.setGeometry(QtCore.QRect(620, 190, 251, 41))
        self.label_27.setStyleSheet("font: 75 20pt \"Rockwell\";")
        self.label_27.setObjectName("label_27")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_16.setGeometry(QtCore.QRect(280, 660, 93, 28))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_17.setGeometry(QtCore.QRect(710, 660, 93, 28))
        self.pushButton_17.setObjectName("pushButton_17")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setGeometry(QtCore.QRect(0, 0, 1081, 341))
        self.label_28.setStyleSheet("font: 28pt \"Rockwell\";")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        self.label_29.setGeometry(QtCore.QRect(310, 340, 311, 31))
        self.label_29.setStyleSheet("font: 12pt \"Segoe UI Variable\";")
        self.label_29.setObjectName("label_29")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(720, 340, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_30 = QtWidgets.QLabel(self.tab_3)
        self.label_30.setGeometry(QtCore.QRect(310, 400, 311, 31))
        self.label_30.setStyleSheet("font: 12pt \"Segoe UI Variable\";")
        self.label_30.setObjectName("label_30")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(720, 400, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_31 = QtWidgets.QLabel(self.tab_3)
        self.label_31.setGeometry(QtCore.QRect(310, 460, 311, 31))
        self.label_31.setStyleSheet("font: 12pt \"Segoe UI Variable\";")
        self.label_31.setObjectName("label_31")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_9.setGeometry(QtCore.QRect(720, 460, 93, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_32 = QtWidgets.QLabel(self.tab_3)
        self.label_32.setGeometry(QtCore.QRect(310, 520, 311, 31))
        self.label_32.setStyleSheet("font: 12pt \"Segoe UI Variable\";")
        self.label_32.setObjectName("label_32")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_10.setGeometry(QtCore.QRect(720, 520, 93, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Bienvenidos a nuestra App</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#00aaff;\">Wazuh</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Para comenzar genere un token</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Generar"))
        self.pushButton.clicked.connect(self.get_header)
        self.lineEdit.setText("")
        self.pushButton_2.setText(_translate("MainWindow", "Limpiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Token), _translate("MainWindow", "Token"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#00aaff;\">Wazuh</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#aa0000;\">Crítica</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ff8922;\">Media</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#e2cc52;\">Baja</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Actualizar \n"
"Critica"))
        self.pushButton_3.clicked.connect(self.vulnerability_by_criticality_critical)
        self.label_8.setText(_translate("MainWindow", "Consulta las vulnerabilidades por alguna criticidad específica de todos los agentes:"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">Alta</span></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Actualizar \n"
"Alta"))
        self.pushButton_4.clicked.connect(self.vulnerability_by_criticality_high)
        self.pushButton_5.setText(_translate("MainWindow", "Actualizar \n"
"Media"))
        self.pushButton_5.clicked.connect(self.vulnerability_by_criticality_medium)
        self.pushButton_6.setText(_translate("MainWindow", "Actualizar \n"
"Baja"))
        self.pushButton_6.clicked.connect(self.vulnerability_by_criticality_low)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Vulnerabilidades"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#00aaff;\">Wazuh</span></p></body></html>"))
        self.pushButton_11.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_11.clicked.connect(self.vulnerabilities_by_keyword)

        self.label_19.setText(_translate("MainWindow", "Busca vulnerabilidades por alguna palabra clave:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Palabra clave"))

        # Agente

        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#00aaff;\">Wazuh</span></p></body></html>"))
        
        self.pushButton_12.setText(_translate("MainWindow", "Actualizar"))
        self.pushButton_12.clicked.connect(self.upgrade_agents)

        self.pushButton_13.setText(_translate("MainWindow", "Reiniciar"))
        self.pushButton_13.clicked.connect(self.restart_agents)

        self.pushButton_14.setText(_translate("MainWindow", "Borrar"))
        self.pushButton_14.clicked.connect(self.delete_agents)

        self.label_21.setText(_translate("MainWindow", "Modifica el agente:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Agente"))

        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#00aaff;\">Wazuh</span></p></body></html>"))
        #self.lineEdit_5.setPlaceholderText("Vulnerabilidad")
        self.pushButton_15.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_15.clicked.connect(self.get_common_agent_vulnerabilites)
        self.label_24.setText(_translate("MainWindow", "Mostrar equipos que tengan alguna vulnerabilidad en común:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "En común"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#00aaff;\">Wazuh</span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "Top 10 de agentes y vulnerabilidades:"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#00aaff;\">Agente</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#00aaff;\">Vulnerabilidad</span></p></body></html>"))
        self.pushButton_16.setText(_translate("MainWindow", "Actualizar"))
        self.pushButton_16.clicked.connect(self.top_10_agents)
        self.pushButton_17.setText(_translate("MainWindow", "Actualizar"))
        self.pushButton_17.clicked.connect(self.top_10_vulnerabilities)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Top 10"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; color:#00aaff;\">Wazuh</span></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\">Descargar reporte de configuración:</p></body></html>"))
        self.pushButton_7.setText(_translate("MainWindow", "Descargar"))
        self.pushButton_7.clicked.connect(self.save_configuration) # Descarga de la
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\">Descargar inf de logs y resumen:</p></body></html>"))
        self.pushButton_8.setText(_translate("MainWindow", "Descargar"))
        self.pushButton_8.clicked.connect(self.save_logs) # Descarga de los logs
        self.pushButton_8.clicked.connect(self.save_log_summary) # Descarga del sumario
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\">Descargar todos los grupos:</p></body></html>"))
        self.pushButton_9.setText(_translate("MainWindow", "Descargar"))
        self.pushButton_9.clicked.connect(self.save_groups)
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\">Descargar estatus de las tareas:</p></body></html>"))
        self.pushButton_10.setText(_translate("MainWindow", "Descargar"))
        self.pushButton_10.clicked.connect(self.get_tasks_status)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Configuración"))

# Funciones propias
    def get_header(self):
        self.header = APILogger.get_header()
        self.lineEdit.setText("Token generado con éxito") if self.header is not None else self.lineEdit.setText("No funcionó unu")
        return None

    def vulnerability_by_criticality_critical(self):
        vulnerabilities = APIMethods.vulnerability_by_criticality("Critical", self.header)
        # vulnerabilities = ["a","b","c","d","e","f","g"]
        model = QtGui.QStandardItemModel()
        self.listView_3.setModel(model)

        for i in vulnerabilities:
            str_item = f"{i}"
            item = QtGui.QStandardItem(str(str_item))
            model.appendRow(item)
        
        self.horizontalLayout.removeWidget(self.listView_3)
        self.horizontalLayout.addWidget(self.listView_3)

    def vulnerability_by_criticality_high(self):
        vulnerabilities = APIMethods.vulnerability_by_criticality("High", self.header)
        # vulnerabilities = ["a","b","c","d","e","f"]
        model = QtGui.QStandardItemModel()
        self.listView_4.setModel(model)

        for i in vulnerabilities:
            str_item = f"{i}"
            item = QtGui.QStandardItem(str(str_item))
            model.appendRow(item)
        
        self.horizontalLayout_3.removeWidget(self.listView_4)
        self.horizontalLayout_3.addWidget(self.listView_4)

    def vulnerability_by_criticality_medium(self):
        vulnerabilities = APIMethods.vulnerability_by_criticality("Medium", self.header)
        # vulnerabilities = ["a","b","c","d","e"]
        model = QtGui.QStandardItemModel()
        self.listView_5.setModel(model)

        for i in vulnerabilities:
            str_item = f"{i}"
            item = QtGui.QStandardItem(str(str_item))
            model.appendRow(item)
        
        self.horizontalLayout_4.removeWidget(self.listView_5)
        self.horizontalLayout_4.addWidget(self.listView_5)

    def vulnerability_by_criticality_low(self):
        vulnerabilities = APIMethods.vulnerability_by_criticality("Low", self.header)
        # vulnerabilities = ["a","b","c","d"]
        model = QtGui.QStandardItemModel()
        self.listView_6.setModel(model)

        for i in vulnerabilities:
            str_item = f"{i}"
            item = QtGui.QStandardItem(str(str_item))
            model.appendRow(item)
        
        self.horizontalLayout_5.removeWidget(self.listView_6)
        self.horizontalLayout_5.addWidget(self.listView_6)

    def vulnerabilities_by_keyword(self):
        lineEdit_string = self.lineEdit_3.text()
        vulnerabilities = APIMethods.vulnerabilities_by_keyword(lineEdit_string, self.header)
        model = QtGui.QStandardItemModel()
        self.listView_7.setModel(model)

        for i in vulnerabilities:
            str_item = f"{i}"
            item = QtGui.QStandardItem(str(str_item))
            model.appendRow(item)
        
        self.verticalLayout_11.removeWidget(self.listView_7)
        self.verticalLayout_11.addWidget(self.listView_7)

    def upgrade_agents(self):
        lineEdit_string = self.lineEdit_4.text()
        result = APIMethods.upgrade_agents(lineEdit_string, self.header)
        self.addElementToAgentLog(result)

    def restart_agents(self):
        lineEdit_string = self.lineEdit_4.text()
        result = APIMethods.restart_agents(lineEdit_string, self.header)
        self.addElementToAgentLog(result)
    
    def delete_agents(self):
        lineEdit_string = self.lineEdit_4.text()
        result = APIMethods.delete_agents(lineEdit_string, self.header)
        self.addElementToAgentLog(result)

    def addElementToAgentLog(self, line: str):
        #listView_8
        model = QtGui.QStandardItemModel()
        self.listView_8.setModel(model)
        item = QtGui.QStandardItem(str(line))
        model.appendRow(item)

    def get_common_agent_vulnerabilites(self):
        #listView_9
        model = QtGui.QStandardItemModel()
        self.listView_9.setModel(model)
        api_res = APIMethods.get_vulnerabilities_with_agents(self.header)
        for key in api_res.keys():
            if len(api_res[key]):
                string = "Agents "
                for agent in api_res[key]:
                    str += f"{agent}, "
                string = f" have {key} as a common vulnerability."
                item = QtGui.QStandardItem(string)
                model.appendRow(item)
    
    def top_10_vulnerabilities(self):
        top_10 = APIMethods.top_n_vulnerabilities(10, self.header)
        # top_10 = [('uno', 1), ('dos', 2), ('tres', 3)]
        model = QtGui.QStandardItemModel()
        self.listView_2.setModel(model)
        
        for i in top_10:
            str_item = f"{i[0]} se encuentra en {i[1]} agentes"
            item = QtGui.QStandardItem(str(str_item))
            model.appendRow(item)
        
        self.verticalLayout_18.removeWidget(self.listView_2)
        self.verticalLayout_18.addWidget(self.listView_2)
        
    def top_10_agents(self):
        top_10 = APIMethods.top_n_agents(10, self.header)
        # top_10 = [('uno', 1), ('dos', 2), ('tres', 3)]
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        
        for i in top_10:
            # str_item = f"{i[0]} se encuentra en {i[1]} agentes"
            str_item = i
            item = QtGui.QStandardItem(str(str_item))
            model.appendRow(item)
        
        self.verticalLayout_17.removeWidget(self.listView)
        self.verticalLayout_17.addWidget(self.listView)
    
    def save_configuration(self):
        json_conf = APIMethods.get_configuration(self.header)
        JsonToTopicMap.json_to_xtm(json_conf, "configuration")
    
    def save_logs(self):
        json_log = APIMethods.get_logs(self.header)
        JsonToTopicMap.json_to_xtm(json_log, "logs")
        
    def save_log_summary(self):
        json_log = APIMethods.get_log_summary(self.header)
        JsonToTopicMap.json_to_xtm(json_log, "log_summary")

    def save_groups(self):
        json_groups = APIMethods.get_groups(self.header)
        JsonToTopicMap.json_to_xtm(json_groups, "groups")

    def get_tasks_status(self):
        json_tasks = APIMethods.get_task_status(self.header)
        JsonToTopicMap.json_to_xtm(json_tasks, "tasks_status")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())