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
        Dialog.setWindowTitle('GFX Registration')

        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setGeometry(QtCore.QRect(60, 10, 300, 35))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("GFX Auto Register")
        self.title_label.setFont(QtGui.QFont("Ariel", 25))
        self.title_label.setWindowTitle('GFX Register')

        self.title_input = QtWidgets.QTextEdit(Dialog)
        self.title_input.setGeometry(QtCore.QRect(115, 65, 180, 25))
        self.title_input.setText("Watashiha_Bakadesu")
        self.title_input.setFont(QtGui.QFont("Ariel", 10))

        self.gfx_label = QtWidgets.QLabel(Dialog)
        self.gfx_label.setGeometry(QtCore.QRect(300, 65, 180, 25))
        self.gfx_label.setText(".gfx")
        self.gfx_label.setFont(QtGui.QFont("Ariel", 10))

        self.option_1 = QtWidgets.QRadioButton(Dialog)
        self.option_1.setGeometry(QtCore.QRect(130, 100, 180, 25))
        self.option_1.setText("Registration Other GFX")
        self.option_1.setChecked(True)
        self.option_1.setFont(QtGui.QFont("Ariel", 10))
        self.option_1.clicked.connect(self.change_value_1)

        #self.option_2 = QtWidgets.QRadioButton(Dialog)
        #self.option_2.setGeometry(QtCore.QRect(130, 125, 180, 25))
        #self.option_2.setText("Create focus file")
        #self.option_2.setFont(QtGui.QFont("Ariel", 10))
        #self.option_2.clicked.connect(self.change_value_2)

        self.generate_button = QtWidgets.QPushButton(Dialog)
        self.generate_button.setGeometry(QtCore.QRect(150, 250, 100, 20))
        self.generate_button.setText("Generate")
        self.generate_button.setObjectName("Button")
        self.generate_button.clicked.connect(self.create_gfx_list_window_command)

    def change_value_1(self):
        global option_1
        global option_2
        option_1 = 1
        option_2 = 0
    
    def change_value_2(self):
        global option_1
        global option_2
        option_1 = 0
        option_2 = 1

    def create_gfx_list_window_command(self):
        global option_1
        global option_2
        filename_is = self.title_input.toPlainText()
        if option_1 == 1:
            print("Select Generate")
            self.input_gfx_file = QtWidgets.QFileDialog.getExistingDirectory(Dialog, 'Open Directory', '')
            print(self.input_gfx_file)
            file_list = os.listdir(self.input_gfx_file)
            test = file_list.pop()
            del file_list[1]
            temp_1 = self.input_gfx_file
            temp_2 = temp_1.split('/')
            temp_3 = temp_2.index("gfx")
            del temp_2[0:temp_3]
            temp_4 = '/'.join(temp_2)
            text_1 = ''.join(test)
            text_2 = text_1.replace('.tga', '').replace('.dds', '').replace('.png', '')

            output = open(filename_is + ".gfx", 'w')
            output.write('spriteTypes = {\n')
            output.write('\tspriteType = {\n')
            output.write('\t\tname = "GFX_'+text_2+'"\n')
            output.write('\t\ttexturefile = "'+temp_4+'/'+test+'"\n')
            output.write('\t}\n')
            while file_list:
                test = file_list.pop()
                text_1 = ''.join(test)
                text_2 = text_1.replace('.tga', '').replace('.dds', '').replace('.png', '')
                output.write('\tspriteType = {\n')
                output.write('\t\tname = "GFX_'+text_2+'"\n')
                output.write('\t\ttexturefile = "'+temp_4+'/'+test+'"\n')
                output.write('\t}\n')
                print(text_2)
            else:
                output.write('}\n')
                print("complete")

                    

        elif option_2 == 1:
            print("Select Generate")
            self.input_gfx_file = QtWidgets.QFileDialog.getExistingDirectory(Dialog, 'Open Directory', '')
            print(self.input_gfx_file)
            file_list = os.listdir(self.input_gfx_file)
            test = file_list.pop()
            del file_list[1]
            temp_1 = self.input_gfx_file
            temp_2 = temp_1.split('/')
            temp_3 = temp_2.index("gfx")
            del temp_2[0:temp_3]
            temp_4 = '/'.join(temp_2)
            text_1 = ''.join(test)
            text_2 = text_1.replace('.tga', '').replace('.dds', '').replace('.png', '')

            output = open(filename_is + ".gfx", 'w')
            output.write('spriteTypes = {\n')
            output.write('\tspriteType = {\n')
            output.write('\t\tname = "GFX_'+text_2+'"\n')
            output.write('\t\ttexturefile = "gfx/'+temp_4+'/'+test+'"\n')
            output.write('\t}\n')
            while file_list:
                test = file_list.pop()
                text_1 = ''.join(test)
                text_2 = text_1.replace('.tga', '').replace('.dds', '').replace('.png', '')
                output.write('\tspriteType = {\n')
                output.write('\t\tname = "GFX_'+text_2+'"\n')
                output.write('\t\ttexturefile = "gfx/'+temp_4+'/'+test+'"\n')
                output.write('\t}\n')
                print(text_2)
            else:
                output.write('}\n')
                print("complete")
                foundname = None
                foundlocation = None
                filein = open(filename_is+".gfx", "r")
                fileout = open(filename_is + "_shine.gfx", "w")
                fileout.write('spriteTypes = {')
                for line in filein:
                    if line.lstrip()[:1] is not '#':
                        spritelist = line.split('"')
                        for index, item in enumerate(spritelist):
                            if 'name =' in item:
                                spritename = spritelist[(index + 1)]
                                foundname = True
                                print(spritename)
                            if 'texturefile =' in item:
                                spritelocation = spritelist[(index + 1)]
                                foundlocation = True
                            if foundname and foundlocation:
                                fileout.write('\tSpriteType = {\n')
                                fileout.write('\t\tname = "' + spritename + '_shine"\n')
                                fileout.write('\t\ttexturefile = "' + spritelocation + '"\n')
                                fileout.write('\t\teffectFile = "gfx/FX/buttonstate.lua"\n')
                                fileout.write('\t\tanimation = {\n')
                                fileout.write('\t\t\tanimationmaskfile = "' + spritelocation + '"\n')
                                fileout.write('\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"\n')
                                fileout.write('\t\t\tanimationrotation = -90.0\n')
                                fileout.write('\t\t\tanimationlooping = no\n')
                                fileout.write('\t\t\tanimationtime = 0.75\n')
                                fileout.write('\t\t\tanimationdelay = 0\n')
                                fileout.write('\t\t\tanimationblendmode = "add"\n')
                                fileout.write('\t\t\tanimationtype = "scrolling"\n')
                                fileout.write('\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }\n')
                                fileout.write('\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }\n')
                                fileout.write('\t\t}\n')
                                fileout.write('\n')
                                fileout.write('\t\tanimation = {\n')
                                fileout.write('\t\t\tanimationmaskfile = "' + spritelocation + '"\n')
                                fileout.write('\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"\n')
                                fileout.write('\t\t\tanimationrotation = 90.0\n')
                                fileout.write('\t\t\tanimationlooping = no\n')
                                fileout.write('\t\t\tanimationtime = 0.75\n')
                                fileout.write('\t\t\tanimationdelay = 0\n')
                                fileout.write('\t\t\tanimationblendmode = "add"\n')
                                fileout.write('\t\t\tanimationtype = "scrolling"\n')
                                fileout.write('\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }\n')
                                fileout.write('\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }\n')
                                fileout.write('\t\t}\n')
                                fileout.write('\t\tlegacy_lazy_load = no\n')
                                fileout.write('\t}\n')
                                fileout.write('\n')

                fileout.write('}')
                filein.close()
                fileout.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())