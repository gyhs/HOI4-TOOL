from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from playsound import playsound
import sys 
import os

print('Creating Log...')

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setGeometry(QtCore.QRect(70, 10, 300, 30))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("ディシジョン作成機")
        self.title_label.setFont(QtGui.QFont("Meiryo", 25))
        
        self.create_category_button = QtWidgets.QPushButton(Dialog)
        self.create_category_button.setGeometry(QtCore.QRect(80, 50, 250, 50))
        self.create_category_button.setText("カテゴリー作成")
        self.create_category_button.setObjectName("Button")
        
        self.create_decision_button = QtWidgets.QPushButton(Dialog)
        self.create_decision_button.setGeometry(QtCore.QRect(80, 125, 250, 50))
        self.create_decision_button.setText("ディシジョン作成")
        self.create_decision_button.setObjectName("Button")
        
        self.help_button = QtWidgets.QPushButton(Dialog)
        self.help_button.setGeometry(QtCore.QRect(80, 200, 250, 50))
        self.help_button.setText("ヘルプ")
        self.help_button.setObjectName("Button")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())