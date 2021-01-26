from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys 
import os
from difflib import context_diff

print('Creating Log...')

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setWindowTitle('HOI4 Localisation Compare')

        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setGeometry(QtCore.QRect(50, 10, 350, 35))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("HOI4 LOC Compare")
        self.title_label.setFont(QtGui.QFont("Ariel", 25))

        self.input_label = QtWidgets.QTextBrowser(Dialog)
        self.input_label.setGeometry(QtCore.QRect(0, 50, 400, 40))
        self.input_label.setObjectName("TITLE")
        self.input_label.setText("First")
        self.input_label.setFont(QtGui.QFont("Ariel", 10))
        self.input_label.setAlignment(QtCore.Qt.AlignCenter)

        self.title_input = QtWidgets.QTextBrowser(Dialog)
        self.title_input.setGeometry(QtCore.QRect(0, 130, 400, 40))
        self.title_input.setObjectName("TITLE")
        self.title_input.setText("Second")
        self.title_input.setFont(QtGui.QFont("Ariel", 10))
        self.title_input.setAlignment(QtCore.Qt.AlignCenter)

        self.generate_button = QtWidgets.QPushButton(Dialog)
        self.generate_button.setGeometry(QtCore.QRect(150, 100, 100, 20))
        self.generate_button.setText("Select First File")
        self.generate_button.setObjectName("Button")
        self.generate_button.clicked.connect(self.click_input_select_button)

        self.compare_button = QtWidgets.QPushButton(Dialog)
        self.compare_button.setGeometry(QtCore.QRect(125, 180, 150, 20))
        self.compare_button.setText("Select Second File")
        self.compare_button.setObjectName("Button")
        self.compare_button.clicked.connect(self.click_compare_select_button)

        self.start_button = QtWidgets.QPushButton(Dialog)
        self.start_button.setGeometry(QtCore.QRect(125, 210, 150, 20))
        self.start_button.setText("Start Compare")
        self.start_button.setObjectName("Button")
        self.start_button.clicked.connect(self.start_compare)

    def click_input_select_button(self):
        print("Click Select First")
        global input_path
        self.first_file = QtWidgets.QFileDialog.getOpenFileName(Dialog, 'Open File', '', 'Yaml File (*.yml);; All File (*.*)')
        input_path = self.first_file[0]
        self.input_label.setText(input_path)

    def click_compare_select_button(self):
        print("Click Select Second")
        global outpath
        self.second_file = QtWidgets.QFileDialog.getOpenFileName(Dialog, 'Open File', '', 'Yaml File (*.yml);; All File (*.*)')
        outpath = self.second_file[0]
        self.title_input.setText(outpath)

    def start_compare(self):
        print("Click Compare")
        with open(self.first_file[0], 'r',encoding ='utf-8-sig') as f1:
            with open(self.second_file[0],'r', encoding = 'utf-8-sig') as f2:
                f1_lines = [f1.readlines()]
                f2_lines = [f2.readlines()]
                temp3 = []
                temp3 = tuple(set(f1_lines) - set(f2_lines))
                print(temp3)

        f1.close()
        f2.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())