# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seoul_main_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 850)
        MainWindow.setMinimumSize(QtCore.QSize(600, 850))
        MainWindow.setMaximumSize(QtCore.QSize(600, 850))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.open_page = QtWidgets.QWidget()
        self.open_page.setObjectName("open_page")
        self.label = QtWidgets.QLabel(self.open_page)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 851))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/background.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.open_page)
        self.label_2.setGeometry(QtCore.QRect(180, 250, 301, 71))
        self.label_2.setStyleSheet("font: 81 30pt \"Pretendard ExtraBold\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.open_page)
        self.main_page_1 = QtWidgets.QWidget()
        self.main_page_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_page_1.setObjectName("main_page_1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_page_1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(self.main_page_1)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 55, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem1)
        self.main_page_title = QtWidgets.QLabel(self.frame_3)
        self.main_page_title.setMinimumSize(QtCore.QSize(0, 40))
        self.main_page_title.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Pretendard Light")
        font.setPointSize(20)
        self.main_page_title.setFont(font)
        self.main_page_title.setObjectName("main_page_title")
        self.verticalLayout_3.addWidget(self.main_page_title)
        self.main_sub_title = QtWidgets.QLabel(self.frame_3)
        self.main_sub_title.setMinimumSize(QtCore.QSize(0, 96))
        self.main_sub_title.setMaximumSize(QtCore.QSize(16777215, 96))
        font = QtGui.QFont()
        font.setFamily("Pretendard SemiBold")
        font.setPointSize(28)
        self.main_sub_title.setFont(font)
        self.main_sub_title.setObjectName("main_sub_title")
        self.verticalLayout_3.addWidget(self.main_sub_title)
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 545))
        self.frame.setStyleSheet("QPushButton{\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.let_today_weather = QtWidgets.QLabel(self.frame)
        self.let_today_weather.setMinimumSize(QtCore.QSize(0, 30))
        self.let_today_weather.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Pretendard Light")
        font.setPointSize(16)
        self.let_today_weather.setFont(font)
        self.let_today_weather.setObjectName("let_today_weather")
        self.verticalLayout_2.addWidget(self.let_today_weather)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border: 1px solid black;")
        self.widget.setObjectName("widget")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.wheather_icon = QtWidgets.QLabel(self.widget)
        self.wheather_icon.setMinimumSize(QtCore.QSize(265, 135))
        self.wheather_icon.setMaximumSize(QtCore.QSize(265, 135))
        self.wheather_icon.setScaledContents(True)
        self.wheather_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.wheather_icon.setObjectName("wheather_icon")
        self.horizontalLayout_12.addWidget(self.wheather_icon)
        self.temp_label = QtWidgets.QLabel(self.widget)
        self.temp_label.setObjectName("temp_label")
        self.horizontalLayout_12.addWidget(self.temp_label)
        self.verticalLayout_2.addWidget(self.widget)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 210))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.food_btn = QtWidgets.QPushButton(self.frame_2)
        self.food_btn.setMinimumSize(QtCore.QSize(170, 150))
        self.food_btn.setMaximumSize(QtCore.QSize(16777215, 150))
        self.food_btn.setObjectName("food_btn")
        self.horizontalLayout_4.addWidget(self.food_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.sleep_btn = QtWidgets.QPushButton(self.frame_2)
        self.sleep_btn.setMinimumSize(QtCore.QSize(170, 150))
        self.sleep_btn.setObjectName("sleep_btn")
        self.horizontalLayout_4.addWidget(self.sleep_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.tour_btn = QtWidgets.QPushButton(self.frame_2)
        self.tour_btn.setMinimumSize(QtCore.QSize(170, 150))
        self.tour_btn.setObjectName("tour_btn")
        self.horizontalLayout_4.addWidget(self.tour_btn)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.all_show_btn = QtWidgets.QPushButton(self.frame)
        self.all_show_btn.setMinimumSize(QtCore.QSize(0, 150))
        self.all_show_btn.setMaximumSize(QtCore.QSize(16777215, 150))
        self.all_show_btn.setStyleSheet("")
        self.all_show_btn.setObjectName("all_show_btn")
        self.verticalLayout_2.addWidget(self.all_show_btn)
        self.verticalLayout_3.addWidget(self.frame)
        spacerItem4 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout.addWidget(self.frame_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.main_page_1)
        self.main_page_2 = QtWidgets.QWidget()
        self.main_page_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_page_2.setObjectName("main_page_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main_page_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.frame_5 = QtWidgets.QFrame(self.main_page_2)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 220))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.back_2_btn = QtWidgets.QPushButton(self.frame_4)
        self.back_2_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.back_2_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.back_2_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_2_btn.setIcon(icon)
        self.back_2_btn.setIconSize(QtCore.QSize(60, 60))
        self.back_2_btn.setObjectName("back_2_btn")
        self.horizontalLayout_3.addWidget(self.back_2_btn)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_4.addWidget(self.frame_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem8)
        self.main_2_title_lab = QtWidgets.QLabel(self.frame_5)
        self.main_2_title_lab.setMinimumSize(QtCore.QSize(0, 100))
        self.main_2_title_lab.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.main_2_title_lab.setFont(font)
        self.main_2_title_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.main_2_title_lab.setObjectName("main_2_title_lab")
        self.verticalLayout_4.addWidget(self.main_2_title_lab)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 570))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.horizontalLayout_5.addWidget(self.frame_5)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.stackedWidget.addWidget(self.main_page_2)
        self.main_page_3 = QtWidgets.QWidget()
        self.main_page_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_page_3.setObjectName("main_page_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.main_page_3)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.frame_7 = QtWidgets.QFrame(self.main_page_3)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 220))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.back_3_btn = QtWidgets.QPushButton(self.frame_8)
        self.back_3_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.back_3_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.back_3_btn.setText("")
        self.back_3_btn.setIcon(icon)
        self.back_3_btn.setIconSize(QtCore.QSize(60, 60))
        self.back_3_btn.setObjectName("back_3_btn")
        self.horizontalLayout_7.addWidget(self.back_3_btn)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.verticalLayout_7.addWidget(self.frame_8)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem12)
        self.main_3_title_lab = QtWidgets.QLabel(self.frame_7)
        self.main_3_title_lab.setMinimumSize(QtCore.QSize(0, 100))
        self.main_3_title_lab.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.main_3_title_lab.setFont(font)
        self.main_3_title_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.main_3_title_lab.setObjectName("main_3_title_lab")
        self.verticalLayout_7.addWidget(self.main_3_title_lab)
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 570))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_9)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_8.addWidget(self.scrollArea)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem13)
        self.verticalLayout_7.addWidget(self.frame_9)
        self.horizontalLayout_6.addWidget(self.frame_7)
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem14)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.stackedWidget.addWidget(self.main_page_3)
        self.main_page_4 = QtWidgets.QWidget()
        self.main_page_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_page_4.setObjectName("main_page_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.main_page_4)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem15)
        self.frame_10 = QtWidgets.QFrame(self.main_page_4)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 220))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.back_4_btn = QtWidgets.QPushButton(self.frame_11)
        self.back_4_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.back_4_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.back_4_btn.setText("")
        self.back_4_btn.setIcon(icon)
        self.back_4_btn.setIconSize(QtCore.QSize(60, 60))
        self.back_4_btn.setObjectName("back_4_btn")
        self.horizontalLayout_9.addWidget(self.back_4_btn)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem16)
        self.verticalLayout_10.addWidget(self.frame_11)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_10.addItem(spacerItem17)
        self.main_4_title_lab = QtWidgets.QLabel(self.frame_10)
        self.main_4_title_lab.setMinimumSize(QtCore.QSize(0, 100))
        self.main_4_title_lab.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.main_4_title_lab.setFont(font)
        self.main_4_title_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.main_4_title_lab.setObjectName("main_4_title_lab")
        self.verticalLayout_10.addWidget(self.main_4_title_lab)
        self.frame_12 = QtWidgets.QFrame(self.frame_10)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 570))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_13.setStyleSheet("background-color: rgb(255, 239, 181);\n"
"border-radius: 15px;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.img_label = QtWidgets.QLabel(self.frame_13)
        self.img_label.setMinimumSize(QtCore.QSize(120, 0))
        self.img_label.setMaximumSize(QtCore.QSize(120, 120))
        self.img_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 60px;")
        self.img_label.setObjectName("img_label")
        self.horizontalLayout_10.addWidget(self.img_label)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.name_lab = QtWidgets.QLabel(self.frame_13)
        self.name_lab.setObjectName("name_lab")
        self.verticalLayout_13.addWidget(self.name_lab)
        self.type_lab = QtWidgets.QLabel(self.frame_13)
        self.type_lab.setObjectName("type_lab")
        self.verticalLayout_13.addWidget(self.type_lab)
        self.location_lab = QtWidgets.QLabel(self.frame_13)
        self.location_lab.setObjectName("location_lab")
        self.verticalLayout_13.addWidget(self.location_lab)
        self.horizontalLayout_10.addLayout(self.verticalLayout_13)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.verticalLayout_11.addWidget(self.frame_13)
        self.map_widget = QtWidgets.QWidget(self.frame_12)
        self.map_widget.setMaximumSize(QtCore.QSize(16777215, 515))
        self.map_widget.setObjectName("map_widget")
        self.label_6 = QtWidgets.QLabel(self.map_widget)
        self.label_6.setGeometry(QtCore.QRect(180, 190, 141, 31))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_11.addWidget(self.map_widget)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem18)
        self.verticalLayout_10.addWidget(self.frame_12)
        self.horizontalLayout_8.addWidget(self.frame_10)
        spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem19)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.stackedWidget.addWidget(self.main_page_4)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "서울 관광 프로그램"))
        self.main_page_title.setText(_translate("MainWindow", "서울 여행 추천기"))
        self.main_sub_title.setText(_translate("MainWindow", "000님, \n"
"서울 여행을 준비하세요."))
        self.let_today_weather.setText(_translate("MainWindow", "오늘의 서울 날씨는.."))
        self.wheather_icon.setText(_translate("MainWindow", "날씨 아이콘"))
        self.temp_label.setText(_translate("MainWindow", "온도"))
        self.food_btn.setText(_translate("MainWindow", "맛집"))
        self.sleep_btn.setText(_translate("MainWindow", "숙박"))
        self.tour_btn.setText(_translate("MainWindow", "관광"))
        self.all_show_btn.setText(_translate("MainWindow", "전체 지도 보기"))
        self.main_2_title_lab.setText(_translate("MainWindow", "가고싶은 서울의 장소를 선택하세요!\n"
"인기있는 음식점들만 소개해 드립니다."))
        self.main_3_title_lab.setText(_translate("MainWindow", "00구의 유명한 음식점을 안내해드려요!"))
        self.main_4_title_lab.setText(_translate("MainWindow", "00구의 유명한 음식점을 안내해드려요!"))
        self.img_label.setText(_translate("MainWindow", "TextLabel"))
        self.name_lab.setText(_translate("MainWindow", "이름"))
        self.type_lab.setText(_translate("MainWindow", "업종"))
        self.location_lab.setText(_translate("MainWindow", "위치"))
        self.label_6.setText(_translate("MainWindow", "여기에 지도 나옴"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
