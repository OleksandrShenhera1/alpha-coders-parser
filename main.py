import sys
from PyQt6.QtWidgets import QApplication

from main_window import MainWindow

# Start program
def main():
    app = QApplication(sys.argv)


    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
