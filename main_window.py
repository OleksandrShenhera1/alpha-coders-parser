from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt6.QtCore import QThread
from PyQt6.QtGui import QIcon
from config import STYLESHEET

from ui_components import create_main_widget
from parser_worker import ParserWorker

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wallpaper Scraper")
        self.setGeometry(100, 100, 700, 1000)
        
        self.worker = None
        
        main_widget = create_main_widget(self)
        self.setCentralWidget(main_widget)
        self.setStyleSheet(STYLESHEET)



    
    def startbtn_parser(self):
        best = self.cb_best.isChecked()
        latest = self.cb_latest.isChecked()
        popular = self.cb_popular.isChecked()
        pg_count_text = self.page_count.text().strip()
        output_dir = self.save_folder_line.text().strip()
        errors = []

        if not (best or latest or popular):
            errors.append("Select the required [checkboxes] before start.")

        if not pg_count_text:
            errors.append("Enter integer number to [page count] line.")
        if not output_dir:
            errors.append("Choose output directory.")
        else:
            try:
                pg_count = int(pg_count_text)
                if pg_count < 1:
                    errors.append("Enter integer number greater than 0 to [page count] line.")
            except ValueError:
                errors.append("Enter integer number to [page count] line.")

        if errors:
            QMessageBox.warning(self, "Warning", "\n".join(errors))
            return
        
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.progress_bar.setValue(0)
        self.console.clear()

        self.thread = QThread()
        self.worker = ParserWorker(best, latest, popular, pg_count, output_dir)
        self.worker.moveToThread(self.thread)
        
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        
        self.worker.log_message.connect(lambda msg: self.console.append(msg))
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.on_finished)
        self.thread.start()

    def stopbtn_event(self):
        self.stop_btn.setEnabled(False)
        self.start_btn.setEnabled(True)
        if self.worker is not None:
            self.worker.stop()
            QMessageBox.information(self, "info", "Downloading stopped")

    def on_finished(self):
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        QMessageBox.information(self, "success", "Files was saved successfully.")

    def browse_file(self):
        directory = QFileDialog.getExistingDirectory(self, "Choose path")
        if directory:
            self.save_folder_line.setText(directory)

    

