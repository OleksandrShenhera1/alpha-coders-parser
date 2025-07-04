from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QGroupBox,
    QComboBox, QLabel, QLineEdit, QProgressBar, QTextEdit, QCheckBox, QTextBrowser
)
from PyQt6.QtCore import pyqtSignal, Qt, QSize, QUrl
from PyQt6.QtGui import QDesktopServices

from config import SETHTML

def create_main_widget(parent_window):

    central_widget = QWidget()
    main_layout = QVBoxLayout(central_widget)

    # Settings section
    settings_group = QGroupBox("Settings (main)")
    settings_layout = QHBoxLayout(settings_group)

    # CheckBoxes left
    checkboxes_layout = QVBoxLayout()
    parent_window.cb_best = QCheckBox("Best wallpapers")
    parent_window.cb_latest = QCheckBox("Latest wallpapers")
    parent_window.cb_popular = QCheckBox("Popular wallpapers")
    # Add to layout
    checkboxes_layout.addWidget(parent_window.cb_best)
    checkboxes_layout.addWidget(parent_window.cb_latest)
    checkboxes_layout.addWidget(parent_window.cb_popular)
    # Add to section
    settings_layout.addLayout(checkboxes_layout)

    # Fields right
    fields_layout = QVBoxLayout()
    # Page count
    page_count_layout = QHBoxLayout()
    parent_window.page_count = QLineEdit()
    lbl_page_count = QLabel("page count")
    page_count_layout.addWidget(parent_window.page_count)
    page_count_layout.addWidget(lbl_page_count)
    fields_layout.addLayout(page_count_layout)
    # Save folder
    save_folder_layout = QVBoxLayout()
    parent_window.save_folder_line = QLineEdit()
    parent_window.save_folder_btn = QPushButton("Browse")
    parent_window.save_folder_btn.clicked.connect(parent_window.browse_file)
    save_folder_layout.addWidget(parent_window.save_folder_line)
    save_folder_layout.addWidget(parent_window.save_folder_btn)
    fields_layout.addLayout(save_folder_layout)
    # Add to settings
    settings_layout.addLayout(fields_layout)
    # Add to main
    main_layout.addWidget(settings_group)

    # Manual section
    manual_group = QGroupBox("Manual")
    manual_layout = QHBoxLayout(manual_group)
    # How to use 
    parent_window.info = QTextBrowser()
    parent_window.info.setReadOnly(True)
    parent_window.info.setHtml(SETHTML)
    parent_window.info.setOpenExternalLinks(True)
    manual_layout.addWidget(parent_window.info)
    main_layout.addWidget(manual_group)
    # Console section
    console_group = QGroupBox("Console")
    console_layout = QVBoxLayout(console_group)
    # Console
    parent_window.progress_bar = QProgressBar()
    parent_window.progress_bar.setValue(0)
    parent_window.start_btn = QPushButton("Start")
    parent_window.stop_btn = QPushButton("Stop")
    parent_window.stop_btn.setEnabled(False)
    parent_window.stop_btn.setObjectName("stopbtn")
    parent_window.start_btn.setObjectName("startbtn")
    parent_window.start_btn.clicked.connect(parent_window.startbtn_parser)
    parent_window.stop_btn.clicked.connect(parent_window.stopbtn_event)
    parent_window.console = QTextEdit()
    parent_window.console.setReadOnly(True)
    console_layout.addWidget(parent_window.progress_bar)
    console_layout.addWidget(parent_window.start_btn)
    console_layout.addWidget(parent_window.stop_btn)
    console_layout.addWidget(parent_window.console)
    main_layout.addWidget(console_group)

    return central_widget
