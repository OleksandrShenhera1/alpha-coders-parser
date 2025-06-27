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

    
    def startbtn_parser(self):
        parse_best = self.cb_best.isChecked()
        parse_latest = self.cb_latest.isChecked()
        parse_popular = self.cb_popular.isChecked()
        parse_page_count_text = self.page_count.text().strip()
        errors = []

        if not (parse_best or parse_latest or parse_popular):
            errors.append("Select the required [checkboxes] before start.")

        if not parse_page_count_text:
            errors.append("Enter integer number to [page count] line.")
        else:
            try:
                parse_page_count = int(parse_page_count_text)
            except ValueError:
                errors.append("Enter integer number to [page count] line.")

        if errors:
            QMessageBox.warning(self, "Warning", "\n".join(errors))
            return

    def browse_file(self):
        directory = QFileDialog.getExistingDirectory(self, "Choose path")
        if directory:
            self.save_folder_line.setText(directory)

    
