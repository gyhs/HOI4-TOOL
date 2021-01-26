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
option_3 = 0
option_4 = 0

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setWindowTitle('HOI4 Localisation Adder')

        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setGeometry(QtCore.QRect(80, 10, 300, 35))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("HOI4 LOC Adder")
        self.title_label.setFont(QtGui.QFont("Ariel", 25))

        self.title_input = QtWidgets.QTextEdit(Dialog)
        self.title_input.setGeometry(QtCore.QRect(115, 65, 180, 25))
        self.title_input.setText("REPLACE")
        self.title_input.setFont(QtGui.QFont("Ariel", 10))

        self.gfx_label = QtWidgets.QLabel(Dialog)
        self.gfx_label.setGeometry(QtCore.QRect(300, 65, 180, 25))
        self.gfx_label.setText(".txt")
        self.gfx_label.setFont(QtGui.QFont("Ariel", 10))

        self.option_1 = QtWidgets.QRadioButton(Dialog)
        self.option_1.setGeometry(QtCore.QRect(130, 100, 180, 25))
        self.option_1.setText("Add Focus Loc")
        self.option_1.setChecked(True)
        self.option_1.setFont(QtGui.QFont("Ariel", 10))
        self.option_1.clicked.connect(self.change_value_1)

        self.option_2 = QtWidgets.QRadioButton(Dialog)
        self.option_2.setGeometry(QtCore.QRect(130, 125, 180, 25))
        self.option_2.setText("Add Idea Loc")
        self.option_2.setFont(QtGui.QFont("Ariel", 10))
        self.option_2.clicked.connect(self.change_value_2)

        self.option_3 = QtWidgets.QRadioButton(Dialog)
        self.option_3.setGeometry(QtCore.QRect(130, 150, 180, 25))
        self.option_3.setText("Add Decision Loc")
        self.option_3.setFont(QtGui.QFont("Ariel", 10))
        self.option_3.clicked.connect(self.change_value_3)

        self.option_4 = QtWidgets.QRadioButton(Dialog)
        self.option_4.setGeometry(QtCore.QRect(130, 175, 180, 25))
        self.option_4.setText("Add Event Loc")
        self.option_4.setFont(QtGui.QFont("Ariel", 10))
        self.option_4.clicked.connect(self.change_value_4)

        self.generate_button = QtWidgets.QPushButton(Dialog)
        self.generate_button.setGeometry(QtCore.QRect(150, 250, 100, 20))
        self.generate_button.setText("Generate")
        self.generate_button.setObjectName("Button")
        self.generate_button.clicked.connect(self.create_loc_list_window_command)

    def change_value_1(self):
        global option_1
        global option_2
        global option_3
        global option_4
        option_1 = 1
        option_2 = 0
        option_3 = 0
        option_4 = 0
    
    def change_value_2(self):
        global option_1
        global option_2
        global option_3
        global option_4
        option_1 = 0
        option_2 = 1
        option_3 = 0
        option_4 = 0
    
    def change_value_3(self):
        global option_1
        global option_2
        global option_3
        global option_4
        option_1 = 0
        option_2 = 0
        option_3 = 1
        option_4 = 0
    
    def change_value_4(self):
        global option_1
        global option_2
        global option_3
        global option_4
        option_1 = 0
        option_2 = 0
        option_3 = 0
        option_4 = 1

    def create_loc_list_window_command(self):
        global option_1
        global option_2
        global option_3
        global option_4
        filename_is = self.title_input.toPlainText()
        if option_1 == 1:
            print("Select Generate")
            self.input_gfx_file = QtWidgets.QFileDialog.getOpenFileName(Dialog, 'Open Directory', '', 'TXT File (*.txt);; All File (*.*)')
            print(self.input_gfx_file[0])
            selected_file = open(self.input_gfx_file[0], 'r')
            i_want_loc = open(filename_is + ".txt", 'w')
            i_want_loc.write('l_english:\n')
            lines = selected_file.read().splitlines()
            lines.reverse()
            test = lines.pop()
            search_position = "relative_position_id"
            search_id = "id ="
            while lines:
                test = lines.pop()
                if not test.find(search_position) >= 0 :
                    if test.find(search_id)>=0:
                        if not test.find("{")>=0:
                            text_1 = ''.join(test)
                            text_2 = text_1.replace('}', '').replace('{', '').replace('\t', '').replace('continue_if_invalid','').replace('= yes','').replace('= no','').replace('id = ','').replace(' ', '').replace('cancel_if_invalid', '')
                            print(text_2)
                            if text_2.find("") == True:
                                print("pass")
                            i_want_loc.write(text_2 + ':0 "REPLACE"\n')
                            i_want_loc.write(text_2 + '_desc:0 "REPLACE"\n')
            else:
                print("complete!")

            selected_file.close()
            i_want_loc.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())