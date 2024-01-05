from threading import Thread
import requests
from bs4 import BeautifulSoup
from pytube import (YouTube, Search)

from PySide6 import QtCore, QtGui, QtWidgets
from newDownload import newDownload


class music(QtWidgets.QWidget) :
    downloadLinksSize : list = []
    downloadLinks : list = []

    threadList : list = []

    def __init__(self, parent) :
        super().__init__(parent)
        self.p = parent
        self.stop_signal = False

        # self.p.ui.searchBar.returnPressed.connect(lambda: )

    def start_Search(self, query) :
        self.newSearch : newSearch = newSearch(self.p, query)
        self.newSearch.start()

        self.threadList.append(self.newSearch)
        self.newSearch.index = self.threadList.__len__()-1

    def stop_Google_search (self) :
        for search in self.threadList :
            search.stop()

    def myAnimateProperty(self, uiElement: any, property:str, initialValue: any, endValue: any, duration: int):

        self.newAnimation = QtCore.QPropertyAnimation(uiElement, property)
        self.newAnimation.setDuration(duration)
        self.newAnimation.setStartValue(initialValue)
        self.newAnimation.setEndValue(endValue)
        self.newAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.newAnimation.start()

    def addMusicFrame(self, text: str = "", size: int = 0.00):
        self.p.ui.MusicResultFrame = QtWidgets.QFrame(parent=self.p.ui.musicResultsAreaLayout)
        self.p.ui.MusicResultFrame.setWindowOpacity(0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.MusicResultFrame.sizePolicy().hasHeightForWidth())
        self.p.ui.MusicResultFrame.setSizePolicy(sizePolicy)
        self.p.ui.MusicResultFrame.setMinimumSize(QtCore.QSize(0, 80))
        self.p.ui.MusicResultFrame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.p.ui.MusicResultFrame.setStyleSheet("")
        self.p.ui.MusicResultFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.p.ui.MusicResultFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.p.ui.MusicResultFrame.setObjectName("MusicResultFrame")
        self.p.ui.horizontalLayout = QtWidgets.QHBoxLayout(self.p.ui.MusicResultFrame)
        self.p.ui.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.p.ui.horizontalLayout.setContentsMargins(10, 10, 20, 10)
        self.p.ui.horizontalLayout.setSpacing(30)
        self.p.ui.horizontalLayout.setObjectName("horizontalLayout")
        self.p.ui.playButton = QtWidgets.QPushButton(parent=self.p.ui.MusicResultFrame)
        self.p.ui.playButton.setMinimumSize(QtCore.QSize(50, 50))
        self.p.ui.playButton.setMaximumSize(QtCore.QSize(50, 50))
        self.p.ui.playButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/main/Icons/Music Single small.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.p.ui.playButton.setIcon(icon11)
        self.p.ui.playButton.setIconSize(QtCore.QSize(36, 36))
        self.p.ui.playButton.setFlat(True)
        self.p.ui.playButton.setObjectName("playButton")
        self.p.ui.horizontalLayout.addWidget(self.p.ui.playButton)
        self.p.ui.musicResultname = QtWidgets.QLabel(parent=self.p.ui.MusicResultFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.musicResultname.sizePolicy().hasHeightForWidth())
        self.p.ui.musicResultname.setSizePolicy(sizePolicy)
        self.p.ui.musicResultname.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.p.ui.musicResultname.setFont(font)
        self.p.ui.musicResultname.setStyleSheet("background:none;")
        self.p.ui.musicResultname.setObjectName("musicResultname")
        self.p.ui.horizontalLayout.addWidget(self.p.ui.musicResultname)
        spacerItem3 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.p.ui.horizontalLayout.addItem(spacerItem3)
        self.p.ui.musicResultSize = QtWidgets.QLabel(parent=self.p.ui.MusicResultFrame)
        self.p.ui.musicResultSize.setStyleSheet("background:none;")
        self.p.ui.musicResultSize.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.p.ui.musicResultSize.setObjectName("musicResultSize")
        self.p.ui.horizontalLayout.addWidget(self.p.ui.musicResultSize)
        self.p.ui.musicResultType = QtWidgets.QLabel(parent=self.p.ui.MusicResultFrame)
        self.p.ui.musicResultType.setStyleSheet("background:none;")
        self.p.ui.musicResultType.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.p.ui.musicResultType.setObjectName("musicResultType")
        self.p.ui.horizontalLayout.addWidget(self.p.ui.musicResultType)
        self.p.ui.musicResultComment = QtWidgets.QLabel(parent=self.p.ui.MusicResultFrame)
        self.p.ui.musicResultComment.setStyleSheet("background:none;")
        self.p.ui.musicResultComment.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.p.ui.musicResultComment.setObjectName("musicResultComment")
        self.p.ui.horizontalLayout.addWidget(self.p.ui.musicResultComment)
        self.p.ui.downloadButton = QtWidgets.QPushButton(parent=self.p.ui.MusicResultFrame)
        self.p.ui.downloadButton.setMinimumSize(QtCore.QSize(50, 50))
        self.p.ui.downloadButton.setMaximumSize(QtCore.QSize(50, 50))
        self.p.ui.downloadButton.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/main/Icons/download.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.p.ui.downloadButton.setIcon(icon12)
        self.p.ui.downloadButton.setIconSize(QtCore.QSize(36, 36))
        self.p.ui.downloadButton.setFlat(True)
        self.p.ui.downloadButton.setObjectName("downloadButton")
        self.p.ui.horizontalLayout.addWidget(self.p.ui.downloadButton)
        self.p.ui.musicResultsAreaLayout_2.addWidget(self.p.ui.MusicResultFrame)
        
        _translate = QtCore.QCoreApplication.translate

        self.p.ui.playButton.setToolTip(_translate("MainWindow", "Play"))
        self.p.ui.musicResultname.setText(_translate("MainWindow", text))
        self.p.ui.musicResultname.setToolTip(text)
        self.p.ui.musicResultSize.setText(_translate("MainWindow", f"{size:.2f}MB"))
        self.p.ui.musicResultType.setText(_translate("MainWindow", "Type"))
        self.p.ui.musicResultComment.setText(_translate("MainWindow", "comment"))
        self.p.ui.downloadButton.setToolTip(_translate("MainWindow", "Download"))

        self.p.ui.downloadButton.clicked.connect(lambda: newDownload(self.p, text, size).start())
        # self.myAnimateProperty(self.p.ui.MusicResultFrame, b"windowOpacity", 0, 1, 400)



class newSearch(music):
    searchStart = QtCore.Signal()
    linkFound = QtCore.Signal()
    searchComplete = QtCore.Signal()

    def __init__(cls, parent, query):
        super().__init__(parent)
        cls.stop_signal = False
        cls.query :str = query
        index = 0
        
        cls.searchStart.connect(lambda: cls.whenSearchStart())
        cls.linkFound.connect(lambda: cls.whenLinkFound())
        cls.searchComplete.connect(lambda: cls.whenSearchComplete())

    def start(cls):
        cls.searchThread = Thread(target= cls.run)
        cls.searchThread.start()

    def run(cls) :
        base_url = "https://www.google.com/search"
        # base_url = "https://www.bing.com/search"
        numPages = 0
        print("Search Start")
        cls.searchStart.emit()

        for aPage in range(5) :
            if cls.stop_signal:
                break
            params = {"q": cls.query, "hl": "en", "start": numPages}
            # params = {"q": cls.query, "first": aPage}
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"}

            try : ## Pushing a request to google
                if not cls.stop_signal:
                    googleResponse = requests.get(base_url, params=params, headers=headers)

                if googleResponse.status_code == 200 : # Processing google's Response and get all result links
                    soup = BeautifulSoup(googleResponse.text, 'html.parser')
                    search_results = soup.find_all('div', class_='tF2Cxc')
                    # search_results = soup.find_all('div', class_='b_algo')

                    # if not cls.stop_signal:
                    for result in search_results: # Going through the pages for links
                        if cls.stop_signal:
                            break
                        link = result.find('a')['href']
                        pageLink = requests.get(link)
                        page = BeautifulSoup(pageLink.content, 'html.parser')

                        # if not cls.stop_signal:
                        for eLink in page.find_all('a'): # Checking all the links in page as Page link
                            if cls.stop_signal:
                                break
                            pageLink : str = str(eLink.get('href'))

                            if not cls.stop_signal and pageLink.endswith('.mp3') and pageLink.startswith('http'): # Find all links to mp3 files
                                selectedRequest = requests.head(pageLink)
                                size = float(selectedRequest.headers.get('content-length', 0))/(1024*1024)
                                        
                                if not cls.stop_signal and size > 0.2 : # Removing links with 0 size
                                    if cls.downloadLinks.count(pageLink) < 1: # Removing duplicate links
                                        cls.downloadLinks.append(pageLink)
                                        cls.downloadLinksSize.append(size)
                                        print("New Link found")
                                        cls.linkFound.emit()
                else:
                    if not cls.stop_signal: print("site not found")
            except Exception as e :
                print(e)

            numPages += 10

        if cls.stop_signal:
            print("search was stopped")
        else:
            print("Search Complete")
        cls.stop()
        cls.searchComplete.emit()

    def stop(cls):
        cls.stop_signal = True
        # cls.searchThread.join()
    def clearResults(self):
        """ :All: xmy life """
        for i in range(self.p.ui.musicSortingAreaLayout.children().__len__()):
            if "nResults" in self.p.ui.musicSortingAreaLayout.children()[i].objectName():
                self.p.ui.musicSortingAreaLayout.children()[i].deleteLater()

        print("Clearing search results")
        print(self.p.ui.musicResultsAreaLayout.children().__len__())

        self.downloadLinks.clear()
        self.downloadLinksSize.clear()
        self.threadList.clear()
        
        for i in range(1, self.p.ui.musicResultsAreaLayout.children().__len__()-1):
            self.p.ui.musicResultsAreaLayout.children()[-i].deleteLater()

        self.p.ui.musicPageLabel.setText("More search awaits you")
        self.myAnimateProperty(self.p.ui.musicPageLabel, b"minimumHeight", 110, 400, 400)

    def whenSearchStart(self) :
        # Adding additional tags Searching and results found
        self.p.ui.musicPageLabel.setText("Searching")
        self.addMusicSortingTag(f"Searching {self.p.ui.searchBar.text()}", "Cancel search", "searching")
        nResultsExist = False
        for i in range(self.p.ui.musicSortingAreaLayout.children().__len__()): # going through sorting tags
            if "nResults" in self.p.ui.musicSortingAreaLayout.children()[i].objectName(): nResultsExist = True # Checking if nResults sorting tag exist
        if not nResultsExist: self.addMusicSortingTag("0 links found", "Clear search results", "nResults")

    def whenLinkFound(self):
        self.addMusicFrame(self.downloadLinks[-1], self.downloadLinksSize[-1])
        for i in range(self.p.ui.musicSortingAreaLayout.children().__len__()):
            if "nResults" in self.p.ui.musicSortingAreaLayout.children()[i].objectName():
                self.p.ui.musicSortingAreaLayout.children()[i].children()[1].setText(f"{self.downloadLinks.__len__()} link(s) found")

        nResultsExist = False
        for i in range(self.p.ui.musicSortingAreaLayout.children().__len__()): # going through sorting tags
            if "nResults" in self.p.ui.musicSortingAreaLayout.children()[i].objectName(): nResultsExist = True # Checking if nResults sorting tag exist
        if not nResultsExist: self.addMusicSortingTag(f"{self.downloadLinks.__len__()} link(s) found", "Clear search results", "nResults")

    def whenSearchComplete(self) : #!Fix removing all searchTags when search complete
        self.p.ui.musicPageLabel.setText("Search complete")

        # Removing Searching tag
        for i in range(self.p.ui.musicSortingAreaLayout.children().__len__()):
            if "searching" in self.p.ui.musicSortingAreaLayout.children()[i].objectName():
                self.p.ui.musicSortingAreaLayout.children()[i].deleteLater()

    def addMusicSortingTag(self, text : str, tooltip : str, objectName : str = "musicSortingTag" ):
        self.p.ui.musicSortingTag = QtWidgets.QFrame(parent=self.p.ui.musicSortingAreaLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.musicSortingTag.sizePolicy().hasHeightForWidth())
        self.p.ui.musicSortingTag.setSizePolicy(sizePolicy)
        self.p.ui.musicSortingTag.setMinimumSize(QtCore.QSize(0, 35))
        self.p.ui.musicSortingTag.setMaximumSize(QtCore.QSize(16777215, 40))
        self.p.ui.musicSortingTag.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.p.ui.musicSortingTag.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.p.ui.musicSortingTag.setObjectName(objectName)
        self.p.ui.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.p.ui.musicSortingTag)
        self.p.ui.horizontalLayout_6.setContentsMargins(10, 3, 2, 3)
        self.p.ui.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.p.ui.musicSortingTagLabel = QtWidgets.QLabel(parent=self.p.ui.musicSortingTag)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.musicSortingTagLabel.sizePolicy().hasHeightForWidth())
        self.p.ui.musicSortingTagLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p.ui.musicSortingTagLabel.setFont(font)
        self.p.ui.musicSortingTagLabel.setObjectName("musicSortingTagLabel")
        self.p.ui.horizontalLayout_6.addWidget(self.p.ui.musicSortingTagLabel)
        self.p.ui.musicSortingTagBtn = QtWidgets.QPushButton(parent=self.p.ui.musicSortingTag)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p.ui.musicSortingTagBtn.sizePolicy().hasHeightForWidth())
        self.p.ui.musicSortingTagBtn.setSizePolicy(sizePolicy)
        self.p.ui.musicSortingTagBtn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/main/Icons/Cancel.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.p.ui.musicSortingTagBtn.setIcon(icon10)
        self.p.ui.musicSortingTagBtn.setIconSize(QtCore.QSize(26, 26))
        self.p.ui.musicSortingTagBtn.setFlat(True)
        self.p.ui.musicSortingTagBtn.setObjectName("musicSortingTagBtn")
        self.p.ui.horizontalLayout_6.addWidget(self.p.ui.musicSortingTagBtn, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.p.ui.musicSortingAreaLayout_2.addWidget(self.p.ui.musicSortingTag)

        # Helping nResults to SearchTags to stop threads
        if not "nResults" in objectName: self.p.ui.musicSortingTagBtn.clicked.connect(lambda: self.threadList[self.index].stop())
        elif "nResults" in objectName : self.p.ui.musicSortingTagBtn.clicked.connect(lambda: self.clearResults()) # type: ignore

        _translate = QtCore.QCoreApplication.translate

        self.p.ui.musicSortingTagLabel.setText(_translate("MainWindow", text))
        self.p.ui.musicSortingTagBtn.setToolTip(_translate("MainWindow", tooltip))


# class youtubeSearch():
#     def __init__(self):
#         super().__init__(self)

#         self.query = "Hello girl"
#         self.newSearch = Search(self.query)

#     def pp(self):
#         print(self.newSearch.__len__())