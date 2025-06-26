from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt6.QtCore import QThread
from PyQt6.QtGui import QIcon
from config import STYLESHEET
from ui_components import create_main_widget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wallpaper Scraper")
        self.setGeometry(100, 100, 700, 900)
        
        
        main_widget = create_main_widget(self)
        self.setCentralWidget(main_widget)
        self.setStyleSheet(STYLESHEET)

