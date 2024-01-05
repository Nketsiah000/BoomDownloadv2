from PySide6 import QtCore, QtGui, QtWidgets
from newDownload import newDownload

def addMusicSortingTag(parent, text : str, tooltip : str, objectName : str = "musicSortingTag" ):

        self = parent.ui

        self.musicSortingTag = QtWidgets.QFrame(parent=self.musicSortingAreaLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.musicSortingTag.sizePolicy().hasHeightForWidth())
        self.musicSortingTag.setSizePolicy(sizePolicy)
        self.musicSortingTag.setMinimumSize(QtCore.QSize(0, 35))
        self.musicSortingTag.setMaximumSize(QtCore.QSize(16777215, 40))
        self.musicSortingTag.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.musicSortingTag.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.musicSortingTag.setObjectName(objectName)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.musicSortingTag)
        self.horizontalLayout_6.setContentsMargins(10, 3, 2, 3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.musicSortingTagLabel = QtWidgets.QLabel(parent=self.musicSortingTag)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.musicSortingTagLabel.sizePolicy().hasHeightForWidth())
        self.musicSortingTagLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.musicSortingTagLabel.setFont(font)
        self.musicSortingTagLabel.setObjectName("musicSortingTagLabel")
        self.horizontalLayout_6.addWidget(self.musicSortingTagLabel)
        self.musicSortingTagBtn = QtWidgets.QPushButton(parent=self.musicSortingTag)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.musicSortingTagBtn.sizePolicy().hasHeightForWidth())
        self.musicSortingTagBtn.setSizePolicy(sizePolicy)
        self.musicSortingTagBtn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/main/Icons/Cancel.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.musicSortingTagBtn.setIcon(icon10)
        self.musicSortingTagBtn.setIconSize(QtCore.QSize(26, 26))
        self.musicSortingTagBtn.setFlat(True)
        self.musicSortingTagBtn.setObjectName("musicSortingTagBtn")
        self.horizontalLayout_6.addWidget(self.musicSortingTagBtn, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.musicSortingAreaLayout_2.addWidget(self.musicSortingTag)

        self.musicSortingTagBtn.clicked.connect(self.musicSortingTag.deleteLater) # type: ignore

        _translate = QtCore.QCoreApplication.translate

        self.musicSortingTagLabel.setText(_translate("MainWindow", text))
        self.musicSortingTagBtn.setToolTip(_translate("MainWindow", tooltip))

def addMusicFrame(parent, text="", size="0.00"):

        self = parent.ui

        self.MusicResultFrame = QtWidgets.QFrame(parent=self.musicResultsAreaLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MusicResultFrame.sizePolicy().hasHeightForWidth())
        self.MusicResultFrame.setSizePolicy(sizePolicy)
        self.MusicResultFrame.setMinimumSize(QtCore.QSize(0, 80))
        self.MusicResultFrame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.MusicResultFrame.setStyleSheet("")
        self.MusicResultFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.MusicResultFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.MusicResultFrame.setObjectName("MusicResultFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MusicResultFrame)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(10, 10, 20, 10)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playButton = QtWidgets.QPushButton(parent=self.MusicResultFrame)
        self.playButton.setMinimumSize(QtCore.QSize(50, 50))
        self.playButton.setMaximumSize(QtCore.QSize(50, 50))
        self.playButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/main/Icons/Music Single small.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.playButton.setIcon(icon11)
        self.playButton.setIconSize(QtCore.QSize(36, 36))
        self.playButton.setFlat(True)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton)
        self.musicResultname = QtWidgets.QLabel(parent=self.MusicResultFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.musicResultname.sizePolicy().hasHeightForWidth())
        self.musicResultname.setSizePolicy(sizePolicy)
        self.musicResultname.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.musicResultname.setFont(font)
        self.musicResultname.setStyleSheet("background:none;")
        self.musicResultname.setObjectName("musicResultname")
        self.horizontalLayout.addWidget(self.musicResultname)
        spacerItem3 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.musicResultSize = QtWidgets.QLabel(parent=self.MusicResultFrame)
        self.musicResultSize.setStyleSheet("background:none;")
        self.musicResultSize.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.musicResultSize.setObjectName("musicResultSize")
        self.horizontalLayout.addWidget(self.musicResultSize)
        self.musicResultType = QtWidgets.QLabel(parent=self.MusicResultFrame)
        self.musicResultType.setStyleSheet("background:none;")
        self.musicResultType.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.musicResultType.setObjectName("musicResultType")
        self.horizontalLayout.addWidget(self.musicResultType)
        self.musicResultComment = QtWidgets.QLabel(parent=self.MusicResultFrame)
        self.musicResultComment.setStyleSheet("background:none;")
        self.musicResultComment.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.musicResultComment.setObjectName("musicResultComment")
        self.horizontalLayout.addWidget(self.musicResultComment)
        self.downloadButton = QtWidgets.QPushButton(parent=self.MusicResultFrame)
        self.downloadButton.setMinimumSize(QtCore.QSize(50, 50))
        self.downloadButton.setMaximumSize(QtCore.QSize(50, 50))
        self.downloadButton.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/main/Icons/download.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.downloadButton.setIcon(icon12)
        self.downloadButton.setIconSize(QtCore.QSize(36, 36))
        self.downloadButton.setFlat(True)
        self.downloadButton.setObjectName("downloadButton")
        self.horizontalLayout.addWidget(self.downloadButton)
        self.musicResultsAreaLayout_2.addWidget(self.MusicResultFrame)
        
        _translate = QtCore.QCoreApplication.translate

        self.playButton.setToolTip(_translate("MainWindow", "Play"))
        self.musicResultname.setText(_translate("MainWindow", text))
        self.musicResultname.setToolTip(text)
        self.musicResultSize.setText(_translate("MainWindow", f"{size:.2f}MB"))
        self.musicResultType.setText(_translate("MainWindow", "Type"))
        self.musicResultComment.setText(_translate("MainWindow", "comment"))
        self.downloadButton.setToolTip(_translate("MainWindow", "Download"))

        self.downloadButton.clicked.connect(lambda: newDownload(parent, text, f"{size:.2f}MB").start())


