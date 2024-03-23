from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QLineEdit, QVBoxLayout)
from PyQt5.QtCore import Qt 

from baza import *

app = QApplication([])

window = QWidget()
window.resize(600, 500)
window.setWindowTitle("Authorize 0.1")

window1 = QWidget()
window1.resize(400, 300)
window1.setWindowTitle("Authorize 0.1")

name_lb = QLabel("")
line2 = QVBoxLayout()
line2.addWidget(name_lb)
window.setLayout(line2)

login_btn = QPushButton("Login")
login_lb = QLabel("Enter your login")
passw_lb = QLabel("Enter password")

login_line = QLineEdit()
passw_line = QLineEdit()
main_line1 = QVBoxLayout()
main_line1.addStretch(1)
main_line1.addWidget(login_lb, alignment=Qt.AlignCenter)
main_line1.addWidget(login_line, alignment=Qt.AlignCenter)
main_line1.addWidget(passw_lb, alignment=Qt.AlignCenter)
main_line1.addWidget(passw_line,alignment=Qt.AlignCenter)
main_line1.addWidget(login_btn, alignment=Qt.AlignCenter)
main_line1.addStretch(1)
window.setLayout(main_line1)

window.show()

def login():
    login_input = login_line.text()
    passw_input = passw_line.text()
    data = get_data(login_input)
    if data:
        if passw_input == data[0][1]:
            print(data)
            name_lb.set.Text(data[0][2])
            window.hide()
            
        else:
            print("Wrong Password")
    else:
        print("No such login found")
    #window.hide()
    #window1.show()

login_btn.clicked.connect(login)

app.exec()