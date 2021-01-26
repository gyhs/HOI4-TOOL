from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from playsound import playsound
import sys 
import os

print('Creating Log...')

category_icon_path = ''
category_picture_path = ''
mypath = os.path.realpath(__file__).split('\\')

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)

        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setGeometry(QtCore.QRect(70, 10, 300, 30))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("Decision Generator")
        self.title_label.setFont(QtGui.QFont("Ariel", 25))
        
        self.create_category_button = QtWidgets.QPushButton(Dialog)
        self.create_category_button.setGeometry(QtCore.QRect(80, 50, 250, 50))
        self.create_category_button.setText("Create Category")
        self.create_category_button.setObjectName("Button")
        self.create_category_button.clicked.connect(self.create_category_window_command)
        
        self.create_decision_button = QtWidgets.QPushButton(Dialog)
        self.create_decision_button.setGeometry(QtCore.QRect(80, 125, 250, 50))
        self.create_decision_button.setText("Create Decision")
        self.create_decision_button.setObjectName("Button")
        self.create_decision_button.clicked.connect(self.create_decision_window_command)
        
        self.help_button = QtWidgets.QPushButton(Dialog)
        self.help_button.setGeometry(QtCore.QRect(80, 200, 250, 50))
        self.help_button.setText("Help")
        self.help_button.setObjectName("Button")
        self.help_button.clicked.connect(self.command_help)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Decision Generator"))

    def command_help(self, help_container):
        print("Clicked Help Button")
        self.help_title_label = QtWidgets.QLabel()
        self.help_title_label.show()
        self.help_title_label.setGeometry(QtCore.QRect(900, 500, 500, 300))
        self.help_title_label.setObjectName("TITLE")
        self.help_title_label.setText("HOI4 Decision Generator, Made by NIKA\nfor The Sun Shining on the World mod\n\nWritten in Python 3.8.5\n\n------------------------------usage------------------------------")
        self.help_title_label.setFont(QtGui.QFont("Ariel", 10))
        self.help_title_label.setAlignment(QtCore.Qt.AlignHCenter)

    def create_category_window_command(self):
        print("Select Create Category")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.create_category_window = QtWidgets.QDialog()
        self.create_category_window.resize(400, 400)
        self.create_category_window.setWindowIcon(icon)
        self.create_category_window.setWindowTitle('Category Creator')

        self.category_title_label = QtWidgets.QLabel(self.create_category_window)
        self.category_title_label.setGeometry(QtCore.QRect(0, 10, 400, 30))
        self.category_title_label.setObjectName("TITLE")
        self.category_title_label.setText("Category Creator")
        self.category_title_label.setFont(QtGui.QFont("Ariel", 20))
        self.category_title_label.setAlignment(QtCore.Qt.AlignHCenter)

        self.tag_input = QtWidgets.QTextEdit(self.create_category_window)
        self.tag_input.setGeometry(QtCore.QRect(120, 75, 150, 25))
        self.tag_input.setText("SOV")
        self.tag_input.setFont(QtGui.QFont("Ariel", 10))

        self.tag_label = QtWidgets.QLabel(self.create_category_window)
        self.tag_label.setGeometry(QtCore.QRect(20, 83, 100, 20))
        self.tag_label.setObjectName("TITLE")
        self.tag_label.setText("TAG")
        self.tag_label.setFont(QtGui.QFont("Ariel", 10))
        self.tag_label.setAlignment(QtCore.Qt.AlignHCenter)

        self.category_title_input = QtWidgets.QTextEdit(self.create_category_window)
        self.category_title_input.setGeometry(QtCore.QRect(120, 115, 180, 25))
        self.category_title_input.setText("SOV_world_revolution")
        self.category_title_input.setFont(QtGui.QFont("Ariel", 10))

        self.category_title_label = QtWidgets.QLabel(self.create_category_window)
        self.category_title_label.setGeometry(QtCore.QRect(15, 123, 100, 20))
        self.category_title_label.setObjectName("TITLE")
        self.category_title_label.setText("Category Name")
        self.category_title_label.setFont(QtGui.QFont("Ariel", 10))
        self.category_title_label.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.select_icon_button = QtWidgets.QPushButton(self.create_category_window)
        self.select_icon_button.setGeometry(QtCore.QRect(20, 210, 100, 20))
        self.select_icon_button.setText("Select Icon")
        self.select_icon_button.setObjectName("Button")
        self.select_icon_button.clicked.connect(self.create_icon_list_window_command)

        self.category_icon_label = QtWidgets.QLabel(self.create_category_window)
        self.category_icon_label.setGeometry(QtCore.QRect(150, 175, 100, 100))
        self.category_icon_label.setObjectName("icon")
        
        self.select_picture_button = QtWidgets.QPushButton(self.create_category_window)
        self.select_picture_button.setGeometry(QtCore.QRect(20, 300, 100, 20))
        self.select_picture_button.setText("Select Picture")
        self.select_picture_button.setObjectName("Button")
        self.select_picture_button.clicked.connect(self.create_gfx_list_window_command)

        self.category_picture_label = QtWidgets.QLabel(self.create_category_window)
        self.category_picture_label.setGeometry(QtCore.QRect(150, 255, 120, 120))
        self.category_picture_label.setObjectName("icon")
        
        self.generate_button = QtWidgets.QPushButton(self.create_category_window)
        self.generate_button.setGeometry(QtCore.QRect(150, 370, 100, 20))
        self.generate_button.setText("Generate")
        self.generate_button.setObjectName("Button")
        self.generate_button.clicked.connect(self.generate_category)

        self.create_category_window.show()
    
    def create_icon_list_window_command(self):
        print("Select Icon List")
        global category_icon_path
        global icon_really
        qpixmapvar = QtGui.QPixmap()
        playsound("sound/click_sound.mp3")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.input_file = QtWidgets.QFileDialog.getOpenFileName(self.create_category_window, 'Open File', 'icon', 'PNG Files(*.png);; All Files(*)')
        qpixmapvar.load(self.input_file[0])
        self.category_icon_label.setPixmap(qpixmapvar)
        category_icon_path = self.input_file[0]
        icon_splited = category_icon_path.split('/')
        icon_last = icon_splited[-1:]
        icon_real = ''.join(icon_last)
        icon_really = icon_real.rstrip('.png')

    def create_gfx_list_window_command(self):
        print("Select Picture List")
        global category_picture_path
        global picture_really
        qpixmapvar_picture = QtGui.QPixmap()
        playsound("sound/click_sound.mp3")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.input_gfx_file = QtWidgets.QFileDialog.getOpenFileName(self.create_category_window, 'Open File', 'picture', 'PNG Files(*.png);; All Files(*)')
        qpixmapvar_picture.load(self.input_gfx_file[0])
        self.category_picture_label.setPixmap(qpixmapvar_picture)
        category_picture_path = self.input_gfx_file[0]
        picture_splited = category_picture_path.split('/')
        picture_last = picture_splited[-1:]
        picture_real = ''.join(picture_last)
        picture_really = picture_real.rstrip('.png')
    
    def generate_category(self):
        print("Select generate")
        playsound("sound/click_sound.mp3")
        global category_icon_path
        global category_picture_path
        country_tag = self.tag_input.toPlainText()
        category_name = self.category_title_input.toPlainText()
        category_output = open("category.txt", 'w')
        category_output.write(category_name+' = {')
        category_output.write('\n	picture = GFX_'+picture_really)
        category_output.write('\n	icon = GFX_'+icon_really)
        category_output.write('\n	')
        category_output.write('\n	allowed = {')
        category_output.write('\n		original_tag = '+country_tag)
        category_output.write('\n	}')
        category_output.write('\n}')

    def create_decision_window_command(self):
        print("Select Create Decision")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.create_decision_window = QtWidgets.QDialog()
        self.create_decision_window.resize(400, 400)
        self.create_decision_window.setWindowIcon(icon)
        self.create_decision_window.setWindowTitle('Decision Generator')

        self.create_decision_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())