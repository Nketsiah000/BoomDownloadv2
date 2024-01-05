# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
import Resources_rc

from music import music
import framesToAdd
from settings import settings as s

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
#     pyside2-uic form.ui -o ui_form.py

from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        m = self
        self.music = music(m)

        # Setting focus to logo on start
        # self.ui.logoFrame.setFocus()
        
        # Constructing connections

        # Setting up initial Active tab as music
        self.previousTab : str = ""
        self.activeTab : str = ""
        self.setActiveTab("music")

        # Search bar actions
        self.ui.searchButton.clicked.connect(lambda: self.search())

        # Sorting tag Btn actions
        self.ui.addMusicSortingTagBtn.clicked.connect(lambda: framesToAdd.addMusicSortingTag(self, "A new sorting tag", "A new sorting label"))

        #Setting tab actions
        self.ui.musicIcon.clicked.connect(lambda: self.setActiveTab("music"))
        self.ui.videosIcon.clicked.connect(lambda: self.setActiveTab("videos"))
        self.ui.moviesIcon.clicked.connect(lambda: self.setActiveTab("movies"))
        self.ui.pdfIcon.clicked.connect(lambda: self.setActiveTab("pdf"))
        self.ui.settingsIcon.clicked.connect(lambda: self.setActiveTab("settings"))
        self.ui.downloadsBtn.clicked.connect(lambda: self.goDownloads())


    def search(self) :
        if self.ui.searchBar.text().__len__() > 2 :
            self.music.start_Search(self.ui.searchBar.text())


    def setActiveTab(self, tabName: str) :
        if not tabName in self.activeTab :
            # Resetting Tab colors
            self.ui.musicBtn.setStyleSheet("")
            self.ui.videosBtn.setStyleSheet("")
            self.ui.moviesBtn.setStyleSheet("")
            self.ui.pdfBtn.setStyleSheet("")
            self.ui.settingsBtn.setStyleSheet("")
            self.ui.downloadsBtn.setStyleSheet("")

            # Setting color for the chosen tab
            if "music" in tabName:
                self.ui.musicBtn.setStyleSheet(f"background-color: {s.colors.mainLightFlat}")
                self.ui.mainStackedWidget.setCurrentIndex(0)

            elif "videos" in tabName:
                self.ui.videosBtn.setStyleSheet(f"background-color: {s.colors.mainLightFlat}")
                self.ui.mainStackedWidget.setCurrentIndex(1)

            elif "movies" in tabName:
                self.ui.moviesBtn.setStyleSheet(f"background-color: {s.colors.mainLightFlat}")
                self.ui.mainStackedWidget.setCurrentIndex(2)

            elif "pdf" in tabName:
                self.ui.pdfBtn.setStyleSheet(f"background-color: {s.colors.mainLightFlat}")
                self.ui.mainStackedWidget.setCurrentIndex(3)
                
            elif "settings" in tabName:
                self.ui.settingsBtn.setStyleSheet(f"background-color: {s.colors.mainLightFlat}")
                self.ui.mainStackedWidget.setCurrentIndex(4)

            elif "downloads" in tabName:
                self.ui.downloadsBtn.setStyleSheet(f"background-color: {s.colors.mainLightFlat}")
                self.ui.mainStackedWidget.setCurrentIndex(5)
                
        self.previousTab = self.activeTab
        self.activeTab = tabName

    def goDownloads(self):
        if "downloads" in self.activeTab: self.setActiveTab(self.previousTab)
        else: self.setActiveTab("downloads") 


    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        widget = self.childAt(event.position().toPoint())
        if widget is not None and widget.objectName():
            print(event.button(), widget.objectName())

            if "musicLabel" in widget.objectName() or "musicBtn" in widget.objectName() :
                self.setActiveTab("music")
            elif "videosLabel" in widget.objectName() or "videosBtn" in widget.objectName() :
                self.setActiveTab("videos")
            elif "moviesLabel" in widget.objectName() or "moviesBtn" in widget.objectName() :
                self.setActiveTab("movies")
            elif "pdfLabel" in widget.objectName() or "pdfBtn" in widget.objectName() :
                self.setActiveTab("pdf")
            elif "settingsLabel" in widget.objectName() or "settingsBtn" in widget.objectName() :
                self.setActiveTab("settings")
            elif "addMusicSortingTagLabel" in widget.objectName() :
                framesToAdd.addMusicSortingTag(self, "A new sorting tag", "A new sorting label")

    def dd(self):
        self.music.stop_Google_search()
        app.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    widget = MainWindow()
    widget.show()
    sys.exit(widget.dd())
