from PySide6 import QtCore, QtGui, QtWidgets

from threading import Thread
import requests
import os
import time

class newDownload(QtWidgets.QWidget):
    download_complete = QtCore.Signal()
    progress_signal = QtCore.Signal()

    def __init__(self, parent, link: str, size: int):
        
        super().__init__()
        self.size = size
        self.p = parent
        self.downloadLink = link

        self.current_dir = os.getcwd()
        self.folder = "Boom Downloads"
        self.fileDirectory : str = os.path.join(self.current_dir, self.folder)
        self.createDirectory()

        self.n = 1
        self.progress = 0.00
        self.stop_signal = False
        self.fileName : str = "Downloaded with boom"
        self.constructFileName()

        self.filePath : str = os.path.join(self.fileDirectory, self.fileName)
        
        self.download_complete.connect(lambda: self.addToHistory())
        self.progress_signal.connect(lambda: self.updateProgress())

    def start(self):
        self.constructDownloadWidget()

        self.newDownloadThread = Thread(target= self.download)
        self.newDownloadThread.start()

    def download(self):
        try:
            chunk_size = 1024
            if os.path.isfile(self.filePath): # If the file has been downloaded and paused
                downloaded = os.path.getsize(self.filePath)
            else:
                downloaded = 0

            download_request = requests.get(self.downloadLink, stream=True)

            if download_request.status_code == 200:
                size = int(download_request.headers.get('content-length', 0))
                with open(self.filePath, 'ab') as f:
                    for data in download_request.iter_content(chunk_size):
                        if self.stop_signal:
                            break
                        f.write(data)
                        downloaded += len(data)
                        self.progress = (downloaded / size) * 100
                        self.progress_signal.emit()

            else: print("Connection Error")

            if not self.stop_signal:
                print("Download completed")
                self.deleteDownloadWidget()
            else:
                print("Download was stopped")

        except Exception as e:
            print(e)
            self.stop_signal = True

        self.download_complete.emit()

    def updateProgress(self):
        self.p.ui.downloadProgressBar.setProperty("value", self.progress)
        self.p.ui.downloadProgressLabel.setText(f"{self.progress:.2f}%")
        
    def addToHistory(self):
        h = newHistory(self.p, self.fileName, self.size, self.downloadLink, self.filePath)
        h.constructHistoryWidget()

    def deleteDownloadWidget(self):
        time.sleep(2)
        self.p.ui.downloadWidget.deleteLater()

    def stop(self):
        self.stop_signal = True
        if self.newDownloadThread.is_alive():
            self.newDownloadThread.join()
            self.deleteFile()
            self.p.ui.downloadWidget.deleteLater()

    def pauseResume(self):
        if self.stop_signal:
            self.stop_signal = False
            print("Download resume")
            self.start()
        else:
            self.stop_signal = True
            print("Download pause")

    def createDirectory(self):
        try: 
            os.makedirs(self.fileDirectory)
        except OSError as e :
            print(e)

    def deleteFile(self):
        if os.path.isfile(self.filePath):
            try:
                os.remove(self.filePath)
                print("File removed successfully")
            except OSError as e:
                print(e)
        else:
            print("File does not exist")

    def renameFile(self):
        self.fileName = self.fileName.strip(".mp3")
        self.fileName = self.fileName.strip(f" ({self.n})")

        self.n = self.n + 1
        self.fileName = self.fileName + f" ({self.n})" + ".mp3"

        if os.path.isfile(os.path.join(self.fileDirectory, self.fileName)):
            self.renameFile()

    def constructFileName(self):
        self.fileName = self.downloadLink.rpartition("/")
        self.fileName = self.fileName[2].replace("_", " ")
        self.fileName = self.fileName.replace("-", " ")
        self.fileName = self.fileName.replace("   ", " - ")
        self.fileName = self.fileName.replace("  ", " ")
        self.fileName = self.fileName.replace("%20", " ")

        if os.path.isfile(os.path.join(self.fileDirectory, self.fileName)):
            self.renameFile()
        else:
            print("We can create ", self.fileName)
            
    def myAnimateProperty(self, uiElement: any, property:str, initialValue: any, endValue: any, duration: int):
        
        self.newAnimation = QtCore.QPropertyAnimation(uiElement, property)
        self.newAnimation.setDuration(duration)
        self.newAnimation.setStartValue(initialValue)
        self.newAnimation.setEndValue(endValue)
        self.newAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.newAnimation.start()
    
    def constructDownloadWidget(self):
        self.p.ui.downloadWidget = QtWidgets.QWidget(parent=self.p.ui.ongoingDownloadsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.downloadWidget.sizePolicy().hasHeightForWidth())
        self.p.ui.downloadWidget.setSizePolicy(sizePolicy)
        self.p.ui.downloadWidget.setObjectName(f"{self.fileName}_downloadWidget")
        self.p.ui.gridLayout_2 = QtWidgets.QGridLayout(self.p.ui.downloadWidget)
        self.p.ui.gridLayout_2.setContentsMargins(15, 10, 15, 10)
        self.p.ui.gridLayout_2.setSpacing(10)
        self.p.ui.gridLayout_2.setObjectName(f"{self.fileName}_gridLayout_2")
        self.p.ui.downloadLink = QtWidgets.QLabel(parent=self.p.ui.downloadWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.downloadLink.sizePolicy().hasHeightForWidth())
        self.p.ui.downloadLink.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.p.ui.downloadLink.setFont(font)
        self.p.ui.downloadLink.setObjectName(f"{self.fileName}_downloadLink")
        self.p.ui.gridLayout_2.addWidget(self.p.ui.downloadLink, 1, 0, 1, 2)
        self.p.ui.pauseResumeBtn = QtWidgets.QPushButton(parent=self.p.ui.downloadWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.pauseResumeBtn.sizePolicy().hasHeightForWidth())
        self.p.ui.pauseResumeBtn.setSizePolicy(sizePolicy)
        self.p.ui.pauseResumeBtn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/main/Icons/play-pause.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.p.ui.pauseResumeBtn.setIcon(icon11)
        self.p.ui.pauseResumeBtn.setFlat(True)
        self.p.ui.pauseResumeBtn.setObjectName(f"{self.fileName}_pauseResumeBtn")
        self.p.ui.gridLayout_2.addWidget(self.p.ui.pauseResumeBtn, 3, 3, 1, 1)
        self.p.ui.downloadFileName = QtWidgets.QLabel(parent=self.p.ui.downloadWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.downloadFileName.sizePolicy().hasHeightForWidth())
        self.p.ui.downloadFileName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.p.ui.downloadFileName.setFont(font)
        self.p.ui.downloadFileName.setObjectName(f"{self.fileName}_downloadFileName")
        self.p.ui.gridLayout_2.addWidget(self.p.ui.downloadFileName, 0, 0, 1, 3)
        self.p.ui.cancelDownload = QtWidgets.QPushButton(parent=self.p.ui.downloadWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.cancelDownload.sizePolicy().hasHeightForWidth())
        self.p.ui.cancelDownload.setSizePolicy(sizePolicy)
        self.p.ui.cancelDownload.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/main/Icons/Close.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.p.ui.cancelDownload.setIcon(icon12)
        self.p.ui.cancelDownload.setFlat(True)
        self.p.ui.cancelDownload.setObjectName(f"{self.fileName}_cancelDownload")
        self.p.ui.gridLayout_2.addWidget(self.p.ui.cancelDownload, 3, 4, 1, 1)
        self.p.ui.downloadProgressLabel = QtWidgets.QLabel(parent=self.p.ui.downloadWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.downloadProgressLabel.sizePolicy().hasHeightForWidth())
        self.p.ui.downloadProgressLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p.ui.downloadProgressLabel.setFont(font)
        self.p.ui.downloadProgressLabel.setObjectName(f"{self.fileName}_downloadProgressLabel")
        self.p.ui.gridLayout_2.addWidget(self.p.ui.downloadProgressLabel, 3, 0, 1, 1)
        self.p.ui.downloadProgressBar = QtWidgets.QProgressBar(parent=self.p.ui.downloadWidget)
        self.p.ui.downloadProgressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.p.ui.downloadProgressBar.setMaximumSize(QtCore.QSize(16777215, 4))
        self.p.ui.downloadProgressBar.setProperty("value", 38)
        self.p.ui.downloadProgressBar.setTextVisible(False)
        self.p.ui.downloadProgressBar.setObjectName(f"{self.fileName}_downloadProgressBar")
        self.p.ui.gridLayout_2.addWidget(self.p.ui.downloadProgressBar, 3, 1, 1, 1)
        self.p.ui.downloadFileSize = QtWidgets.QLabel(parent=self.p.ui.downloadWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.downloadFileSize.sizePolicy().hasHeightForWidth())
        self.p.ui.downloadFileSize.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.p.ui.downloadFileSize.setFont(font)
        self.p.ui.downloadFileSize.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.p.ui.downloadFileSize.setObjectName(f"{self.fileName}_downloadFileSize")
        self.p.ui.gridLayout_2.addWidget(self.p.ui.downloadFileSize, 0, 3, 1, 2)
        self.p.ui.verticalLayout.addWidget(self.p.ui.downloadWidget)

        self.p.ui.cancelDownload.clicked.connect(lambda: self.stop()) # type: ignore
        self.p.ui.pauseResumeBtn.clicked.connect(lambda: self.pauseResume())

        _translate = QtCore.QCoreApplication.translate
        self.p.ui.downloadLink.setText(_translate("MainWindow", self.downloadLink))
        self.p.ui.downloadFileName.setText(_translate("MainWindow", self.fileName))
        self.p.ui.downloadProgressLabel.setText(_translate("MainWindow", ""))
        self.p.ui.downloadProgressBar.setFormat(_translate("MainWindow", "%p%"))
        self.p.ui.downloadFileSize.setText(_translate("MainWindow", f"{self.size:.2f}MB"))

class newHistory():
    def __init__(self, parent, name: str, size: int, link: str, filePath: str) -> None:
        super().__init__()
        self.p = parent
        self.s : int = size
        self.fileName : str = name
        self.fileSize : str = f"{size:.2f}MB"
        self.fileLink : str = link
        self.filePath : str = filePath

    def play(self):
        try:
            os.startfile(self.filePath)
        except Exception as e:
            print(e)

    def delete(self):
        try:
            os.remove(self.filePath)
            self.p.ui.historyWidget.deleteLater()
        except Exception as e:
            print(e)
    
    def redownloadFile(self):
        newDownload(self.p, self.fileLink, self.s).start()

    def constructHistoryWidget(self):
        self.p.ui.historyWidget = QtWidgets.QWidget(parent=self.p.ui.historyFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.historyWidget.sizePolicy().hasHeightForWidth())
        self.p.ui.historyWidget.setSizePolicy(sizePolicy)
        self.p.ui.historyWidget.setObjectName(f"{self.fileName}_historyWidget")
        self.p.ui.historyWidgetLayout = QtWidgets.QGridLayout(self.p.ui.historyWidget)
        self.p.ui.historyWidgetLayout.setContentsMargins(15, 10, 15, 7)
        self.p.ui.historyWidgetLayout.setSpacing(10)
        self.p.ui.historyWidgetLayout.setObjectName(f"{self.fileName}_historyWidgetLayout")
        self.p.ui.historyLink = QtWidgets.QLabel(parent=self.p.ui.historyWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.historyLink.sizePolicy().hasHeightForWidth())
        self.p.ui.historyLink.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.p.ui.historyLink.setFont(font)
        self.p.ui.historyLink.setObjectName(f"{self.fileName}_historyLink")
        self.p.ui.historyWidgetLayout.addWidget(self.p.ui.historyLink, 1, 0, 1, 3)
        self.p.ui.playDownloadedFileBtn = QtWidgets.QPushButton(parent=self.p.ui.historyWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.playDownloadedFileBtn.sizePolicy().hasHeightForWidth())
        self.p.ui.playDownloadedFileBtn.setSizePolicy(sizePolicy)
        self.p.ui.playDownloadedFileBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.p.ui.playDownloadedFileBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.p.ui.playDownloadedFileBtn.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/main/Icons/Music Single small.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.p.ui.playDownloadedFileBtn.setIcon(icon13)
        self.p.ui.playDownloadedFileBtn.setIconSize(QtCore.QSize(24, 24))
        self.p.ui.playDownloadedFileBtn.setFlat(True)
        self.p.ui.playDownloadedFileBtn.setObjectName(f"{self.fileName}_playDownloadedFileBtn")
        self.p.ui.historyWidgetLayout.addWidget(self.p.ui.playDownloadedFileBtn, 0, 0, 1, 1)
        self.p.ui.redownloadFileBtn = QtWidgets.QPushButton(parent=self.p.ui.historyWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.redownloadFileBtn.sizePolicy().hasHeightForWidth())
        self.p.ui.redownloadFileBtn.setSizePolicy(sizePolicy)
        self.p.ui.redownloadFileBtn.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/main/Icons/Restart.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.p.ui.redownloadFileBtn.setIcon(icon14)
        self.p.ui.redownloadFileBtn.setFlat(True)
        self.p.ui.redownloadFileBtn.setObjectName(f"{self.fileName}_redownloadFileBtn")
        self.p.ui.historyWidgetLayout.addWidget(self.p.ui.redownloadFileBtn, 0, 3, 1, 1)
        self.p.ui.historyFileName = QtWidgets.QLabel(parent=self.p.ui.historyWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.historyFileName.sizePolicy().hasHeightForWidth())
        self.p.ui.historyFileName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.p.ui.historyFileName.setFont(font)
        self.p.ui.historyFileName.setObjectName(f"{self.fileName}_historyFileName")
        self.p.ui.historyWidgetLayout.addWidget(self.p.ui.historyFileName, 0, 1, 1, 2)
        self.p.ui.deleteHistoryBtn = QtWidgets.QPushButton(parent=self.p.ui.historyWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.deleteHistoryBtn.sizePolicy().hasHeightForWidth())
        self.p.ui.deleteHistoryBtn.setSizePolicy(sizePolicy)
        self.p.ui.deleteHistoryBtn.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/main/Icons/Delete.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.p.ui.deleteHistoryBtn.setIcon(icon15)
        self.p.ui.deleteHistoryBtn.setFlat(True)
        self.p.ui.deleteHistoryBtn.setObjectName(f"{self.fileName}_deleteHistoryBtn")
        self.p.ui.historyWidgetLayout.addWidget(self.p.ui.deleteHistoryBtn, 0, 4, 1, 1)
        self.p.ui.historyFileSize = QtWidgets.QLabel(parent=self.p.ui.historyWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.historyFileSize.sizePolicy().hasHeightForWidth())
        self.p.ui.historyFileSize.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.p.ui.historyFileSize.setFont(font)
        self.p.ui.historyFileSize.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.p.ui.historyFileSize.setObjectName(f"{self.fileName}_historyFileSize")
        self.p.ui.historyWidgetLayout.addWidget(self.p.ui.historyFileSize, 1, 3, 1, 2)
        self.p.ui.historyFrameLayout.addWidget(self.p.ui.historyWidget)

        self.p.ui.playDownloadedFileBtn.clicked.connect(lambda: self.play())
        self.p.ui.redownloadFileBtn.clicked.connect(lambda: self.redownloadFile())
        self.p.ui.deleteHistoryBtn.clicked.connect(lambda: self.delete())

        _translate = QtCore.QCoreApplication.translate
        self.p.ui.historyLink.setText(_translate("MainWindow", self.fileLink))
        self.p.ui.playDownloadedFileBtn.setToolTip(_translate("MainWindow", "Play"))
        self.p.ui.redownloadFileBtn.setToolTip(_translate("MainWindow", "Download file again"))
        self.p.ui.deleteHistoryBtn.setToolTip(_translate("MainWindow", "Delete"))
        self.p.ui.historyFileName.setText(_translate("MainWindow", self.fileName))
        self.p.ui.historyFileSize.setText(_translate("MainWindow", self.fileSize))