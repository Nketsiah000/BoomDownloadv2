# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(994, 610)
        icon = QIcon()
        icon.addFile(u":/main/Icons/Tinder.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"color: rgb(186, 186, 186);\n"
"background-color: rgb(0, 9, 19);")
        MainWindow.setIconSize(QSize(36, 36))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame#detailsFrame {\n"
"	border: 2px solid rgba(255, 255, 255, 0);\n"
"	border-left-color: white;\n"
"}\n"
"QFrame#sideFrame .QWidget {\n"
"	border: 1px solid rgba(68, 68, 68, 175);\n"
"	border-radius: 5px;\n"
"}\n"
"QFrame#sideFrame .QWidget QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QFrame#sideFrame .QWidget:hover {\n"
"	background-color: rgb(80, 80, 80);\n"
"}\n"
"QFrame#searchLayout_1 {\n"
"	border: 1px solid rgba(68, 68, 68, 175);\n"
"	border-radius: 10px;\n"
"}\n"
"QFrame#searchLayout_1 > * {\n"
"	border-radius: 10px;\n"
"}\n"
"QFrame#sideFrame QPushButton:pressed {\n"
"	background-color: rgb(80, 80, 80);\n"
"	border: none;\n"
"}\n"
"QFrame#sortingFrame > QFrame {\n"
"	border: 1px solid rgba(68, 68, 68, 175);\n"
"	border-radius: 10px;\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.topFrame = QFrame(self.centralwidget)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setMaximumSize(QSize(16777215, 120))
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchLeftSpacer = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.searchLeftSpacer)

        self.searchLayout_1 = QFrame(self.topFrame)
        self.searchLayout_1.setObjectName(u"searchLayout_1")
        self.searchLayout_1.setMaximumSize(QSize(16777215, 65))
        self.searchLayout = QHBoxLayout(self.searchLayout_1)
        self.searchLayout.setSpacing(5)
        self.searchLayout.setObjectName(u"searchLayout")
        self.searchLayout.setContentsMargins(-1, -1, 7, -1)
        self.lineEdit = QLineEdit(self.searchLayout_1)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setFrame(False)

        self.searchLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.searchLayout_1)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMaximumSize(QSize(60, 60))
        icon1 = QIcon()
        icon1.addFile(u":/main/Icons/Search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(36, 36))
        self.pushButton.setFlat(True)

        self.searchLayout.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.searchLayout_1)

        self.searchRightSpacer = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.searchRightSpacer)


        self.gridLayout.addWidget(self.topFrame, 0, 1, 1, 1)

        self.sideFrame = QFrame(self.centralwidget)
        self.sideFrame.setObjectName(u"sideFrame")
        self.sideFrame.setMaximumSize(QSize(120, 16777215))
        self.sideFrame.setFrameShape(QFrame.StyledPanel)
        self.sideFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sideFrame)
        self.verticalLayout_2.setSpacing(11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logoFrame = QFrame(self.sideFrame)
        self.logoFrame.setObjectName(u"logoFrame")
        self.logoFrame.setMinimumSize(QSize(0, 90))
        self.logoFrame.setMaximumSize(QSize(16777215, 120))
        self.logoFrame.setFrameShape(QFrame.StyledPanel)
        self.logoFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.logoFrame)

        self.sideMenu = QVBoxLayout()
        self.sideMenu.setSpacing(20)
        self.sideMenu.setObjectName(u"sideMenu")
        self.sideMenu.setContentsMargins(10, -1, 10, 10)
        self.musicBtn = QWidget(self.sideFrame)
        self.musicBtn.setObjectName(u"musicBtn")
        self.musicBtn.setMinimumSize(QSize(80, 0))
        self.pdfLayout_5 = QVBoxLayout(self.musicBtn)
        self.pdfLayout_5.setSpacing(3)
        self.pdfLayout_5.setObjectName(u"pdfLayout_5")
        self.pdfLayout_5.setContentsMargins(3, 2, 3, 2)
        self.musicIcon = QPushButton(self.musicBtn)
        self.musicIcon.setObjectName(u"musicIcon")
        icon2 = QIcon()
        icon2.addFile(u":/main/Icons/Music.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.musicIcon.setIcon(icon2)
        self.musicIcon.setIconSize(QSize(36, 36))
        self.musicIcon.setFlat(True)

        self.pdfLayout_5.addWidget(self.musicIcon)

        self.musicLabel = QLabel(self.musicBtn)
        self.musicLabel.setObjectName(u"musicLabel")
        self.musicLabel.setAlignment(Qt.AlignCenter)
        self.musicLabel.setWordWrap(True)

        self.pdfLayout_5.addWidget(self.musicLabel)


        self.sideMenu.addWidget(self.musicBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.videosBtn = QWidget(self.sideFrame)
        self.videosBtn.setObjectName(u"videosBtn")
        self.videosBtn.setMinimumSize(QSize(80, 0))
        self.pdfLayout_4 = QVBoxLayout(self.videosBtn)
        self.pdfLayout_4.setSpacing(3)
        self.pdfLayout_4.setObjectName(u"pdfLayout_4")
        self.pdfLayout_4.setContentsMargins(3, 2, 3, 2)
        self.videosIcon = QPushButton(self.videosBtn)
        self.videosIcon.setObjectName(u"videosIcon")
        icon3 = QIcon()
        icon3.addFile(u":/main/Icons/Bookmark.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.videosIcon.setIcon(icon3)
        self.videosIcon.setIconSize(QSize(36, 36))
        self.videosIcon.setFlat(True)

        self.pdfLayout_4.addWidget(self.videosIcon)

        self.videosLabel = QLabel(self.videosBtn)
        self.videosLabel.setObjectName(u"videosLabel")
        self.videosLabel.setAlignment(Qt.AlignCenter)
        self.videosLabel.setWordWrap(True)

        self.pdfLayout_4.addWidget(self.videosLabel)


        self.sideMenu.addWidget(self.videosBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.moviesBtn = QWidget(self.sideFrame)
        self.moviesBtn.setObjectName(u"moviesBtn")
        self.moviesBtn.setMinimumSize(QSize(80, 0))
        self.pdfLayout_3 = QVBoxLayout(self.moviesBtn)
        self.pdfLayout_3.setSpacing(3)
        self.pdfLayout_3.setObjectName(u"pdfLayout_3")
        self.pdfLayout_3.setContentsMargins(3, 2, 3, 2)
        self.moviesIcon = QPushButton(self.moviesBtn)
        self.moviesIcon.setObjectName(u"moviesIcon")
        self.moviesIcon.setIcon(icon)
        self.moviesIcon.setIconSize(QSize(36, 36))
        self.moviesIcon.setFlat(True)

        self.pdfLayout_3.addWidget(self.moviesIcon)

        self.moviesLabel = QLabel(self.moviesBtn)
        self.moviesLabel.setObjectName(u"moviesLabel")
        self.moviesLabel.setAlignment(Qt.AlignCenter)
        self.moviesLabel.setWordWrap(True)

        self.pdfLayout_3.addWidget(self.moviesLabel)


        self.sideMenu.addWidget(self.moviesBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pdfBtn = QWidget(self.sideFrame)
        self.pdfBtn.setObjectName(u"pdfBtn")
        self.pdfBtn.setMinimumSize(QSize(80, 0))
        self.pdfLayout = QVBoxLayout(self.pdfBtn)
        self.pdfLayout.setSpacing(3)
        self.pdfLayout.setObjectName(u"pdfLayout")
        self.pdfLayout.setContentsMargins(3, 2, 3, 2)
        self.pdfIcon = QPushButton(self.pdfBtn)
        self.pdfIcon.setObjectName(u"pdfIcon")
        icon4 = QIcon()
        icon4.addFile(u":/main/Icons/Document.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pdfIcon.setIcon(icon4)
        self.pdfIcon.setIconSize(QSize(36, 36))
        self.pdfIcon.setFlat(True)

        self.pdfLayout.addWidget(self.pdfIcon)

        self.pdfLabel = QLabel(self.pdfBtn)
        self.pdfLabel.setObjectName(u"pdfLabel")
        self.pdfLabel.setAlignment(Qt.AlignCenter)
        self.pdfLabel.setWordWrap(True)

        self.pdfLayout.addWidget(self.pdfLabel)


        self.sideMenu.addWidget(self.pdfBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.sideMenu.addItem(self.verticalSpacer)

        self.settingsBtn = QWidget(self.sideFrame)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(80, 0))
        self.pdfLayout_2 = QVBoxLayout(self.settingsBtn)
        self.pdfLayout_2.setSpacing(3)
        self.pdfLayout_2.setObjectName(u"pdfLayout_2")
        self.pdfLayout_2.setContentsMargins(3, 2, 3, 2)
        self.settingsIcon = QPushButton(self.settingsBtn)
        self.settingsIcon.setObjectName(u"settingsIcon")
        icon5 = QIcon()
        icon5.addFile(u":/main/Icons/Settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsIcon.setIcon(icon5)
        self.settingsIcon.setIconSize(QSize(36, 36))
        self.settingsIcon.setFlat(True)

        self.pdfLayout_2.addWidget(self.settingsIcon)

        self.settingsLabel = QLabel(self.settingsBtn)
        self.settingsLabel.setObjectName(u"settingsLabel")
        self.settingsLabel.setAlignment(Qt.AlignCenter)
        self.settingsLabel.setWordWrap(True)

        self.pdfLayout_2.addWidget(self.settingsLabel)


        self.sideMenu.addWidget(self.settingsBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addLayout(self.sideMenu)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 5)

        self.gridLayout.addWidget(self.sideFrame, 0, 0, 3, 1)

        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.mainFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sortingFrame = QFrame(self.mainFrame)
        self.sortingFrame.setObjectName(u"sortingFrame")
        self.sortingFrame.setMaximumSize(QSize(16777215, 70))
        self.sortingFrame.setFrameShape(QFrame.StyledPanel)
        self.sortingFrame.setFrameShadow(QFrame.Raised)
        self.sortingTag = QFrame(self.sortingFrame)
        self.sortingTag.setObjectName(u"sortingTag")
        self.sortingTag.setGeometry(QRect(20, 10, 177, 50))
        self.sortingTag.setMinimumSize(QSize(0, 50))
        self.sortingTag.setFrameShape(QFrame.StyledPanel)
        self.sortingTag.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.sortingTag)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 2, 5)
        self.sortingTagLabel = QLabel(self.sortingTag)
        self.sortingTagLabel.setObjectName(u"sortingTagLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sortingTagLabel.sizePolicy().hasHeightForWidth())
        self.sortingTagLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.sortingTagLabel)

        self.sortingTagBtn = QPushButton(self.sortingTag)
        self.sortingTagBtn.setObjectName(u"sortingTagBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sortingTagBtn.sizePolicy().hasHeightForWidth())
        self.sortingTagBtn.setSizePolicy(sizePolicy3)
        icon6 = QIcon()
        icon6.addFile(u":/main/Icons/Close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sortingTagBtn.setIcon(icon6)
        self.sortingTagBtn.setIconSize(QSize(24, 24))
        self.sortingTagBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.sortingTagBtn)


        self.gridLayout_2.addWidget(self.sortingFrame, 0, 0, 1, 1)

        self.detailsFrame = QFrame(self.mainFrame)
        self.detailsFrame.setObjectName(u"detailsFrame")
        self.detailsFrame.setMaximumSize(QSize(250, 16777215))
        self.detailsFrame.setFrameShape(QFrame.StyledPanel)
        self.detailsFrame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.detailsFrame, 0, 1, 2, 1)

        self.resultsFrame = QFrame(self.mainFrame)
        self.resultsFrame.setObjectName(u"resultsFrame")
        self.resultsFrame.setFrameShape(QFrame.StyledPanel)
        self.resultsFrame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.resultsFrame, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.mainFrame, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Boom Fast Search", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Everything", None))
        self.pushButton.setText("")
        self.musicIcon.setText("")
        self.musicLabel.setText(QCoreApplication.translate("MainWindow", u"Music", None))
        self.videosIcon.setText("")
        self.videosLabel.setText(QCoreApplication.translate("MainWindow", u"Videos", None))
        self.moviesIcon.setText("")
        self.moviesLabel.setText(QCoreApplication.translate("MainWindow", u"Movies", None))
        self.pdfIcon.setText("")
        self.pdfLabel.setText(QCoreApplication.translate("MainWindow", u"PDF", None))
        self.settingsIcon.setText("")
        self.settingsLabel.setText(QCoreApplication.translate("MainWindow", u"Setings", None))
        self.sortingTagLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.sortingTagBtn.setText("")
    # retranslateUi

