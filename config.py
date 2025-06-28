STYLESHEET = """
    QWidget {
        background-color: #2E3440;
        color: #D8DEE9;
        font-size: 14px;
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    QMainWindow {
        background-color: #2E3440;
    }
    QTextEdit {
        background-color: #3B4252;
        border: 1px solid #4C566A;
        border-radius: 8px;
    }
    QLabel {
        font-weight: bold;
    }
    QLineEdit {
        background-color: #3B4252;
        border: 1px solid #4C566A;
        border-radius: 5px;
        padding: 5px;
        margin-left: 10px;
    }
    QPushButton {
        background-color: #5E81AC;
        color: #ECEFF4;
        border: none;
        padding: 10px 15px;
        border-radius: 8px;
        font-weight: bold;
        margin-left: 10px;
    }
    QPushButton:hover {
        background-color: #81A1C1;
    }
    #startbtn {
        background-color: #5E81AC;
        color: #ECEFF4;
        border: none;
        padding: 10px 15px;
        border-radius: 8px;
        font-weight: bold;
        margin-left: 0px;
    }
    #startbtn:hover {
        background-color: #81A1C1;
    }
    #stopbtn {
        background-color: #964252;
        color: #ECEFF4;
        border: none;
        padding: 10px 15px;
        border-radius: 8px;
        font-weight: bold;
        margin-left: 0px;
    }
    #stopbtn:hover {
        background-color: #803d4a;
    }
    QCheckBox {
    color: #33aaff;
    font-weight: bold;
    }
    QCheckBox::indicator {
        width: 20px;
        height: 20px;
    }
    QCheckBox::indicator:checked {
        background-color: #33aaff;
        border: 1px solid #0077cc;
    }
    QProgressBar {
        border: 1px solid #4C566A;
        border-radius: 8px;
        text-align: center;
        background-color: #3B4252;
        color: #D8DEE9;
    }
    QProgressBar::chunk {
        background-color: #A3BE8C;
        border-radius: 7px;
    }
"""

SETHTML = """ 
    <h2>Instructions on How to Use the Application</h2>
    <br>
    <ol style="font-size:14pt;" align="left">
        <li>Select the required checkboxes</li>
        <li>Set the page count (1 is the minimum value)</li>
        <li>Enter your output directory or browse for it</li>
        <li>Press the large Start button!</li>
    </ol>
    <br>
    <p style="font-size:14pt;">Find more information on the <a href='https://github.com/OleksandrShenhera1/alpha-coders-parser' style="color:#ffffff">GitHub profile</a>.</p>
"""