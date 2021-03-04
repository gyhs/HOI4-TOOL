from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from playsound import playsound
import sys 
import os

print('Creating Log...')
mypath = os.path.realpath(__file__).split('\\')
option_1 = 1
option_2 = 0

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowTitle('TEMP')

        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setGeometry(QtCore.QRect(60, 10, 300, 35))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("TEMP")
        self.title_label.setFont(QtGui.QFont("Ariel", 25))
        self.title_label.setWindowTitle('TEMP')

        self.generate_button = QtWidgets.QPushButton(Dialog)
        self.generate_button.setGeometry(QtCore.QRect(150, 250, 100, 20))
        self.generate_button.setText("Delete")
        self.generate_button.setObjectName("Button")
        self.generate_button.clicked.connect(self.create_gfx_list_window_command)

    def create_gfx_list_window_command(self):
        print("Select Generate")
        self.input_gfx_file = QtWidgets.QFileDialog.getExistingDirectory(Dialog, 'Open Directory', '')
        print(self.input_gfx_file)
        file_list = os.listdir(self.input_gfx_file)
        test = file_list.pop()
        print(test)
        for files in os.walk(test):
            for file in files:
                with open(file, 'r') as f:
                    f.read()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())