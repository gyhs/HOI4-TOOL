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
        self.title_label.setText("ディシジョン作成機")
        self.title_label.setFont(QtGui.QFont("Meiryo", 25))
        
        self.create_category_button = QtWidgets.QPushButton(Dialog)
        self.create_category_button.setGeometry(QtCore.QRect(80, 50, 250, 50))
        self.create_category_button.setText("カテゴリー作成")
        self.create_category_button.setObjectName("Button")
        self.create_category_button.clicked.connect(self.create_category_window_command)
        
        self.create_decision_button = QtWidgets.QPushButton(Dialog)
        self.create_decision_button.setGeometry(QtCore.QRect(80, 125, 250, 50))
        self.create_decision_button.setText("デシジョン作成")
        self.create_decision_button.setObjectName("Button")
        self.create_decision_button.clicked.connect(self.create_decision_window_command)
        
        self.help_button = QtWidgets.QPushButton(Dialog)
        self.help_button.setGeometry(QtCore.QRect(80, 200, 250, 50))
        self.help_button.setText("ヘルプ")
        self.help_button.setObjectName("Button")
        self.help_button.clicked.connect(self.command_help)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ディシジョン作成機"))

    def command_help(self, help_container):
        print("Clicked Help Button")
        self.help_title_label = QtWidgets.QLabel()
        self.help_title_label.show()
        self.help_title_label.setGeometry(QtCore.QRect(900, 500, 500, 300))
        self.help_title_label.setObjectName("TITLE")
        self.help_title_label.setText("HOI4ディシジョン作成機\nMade by NIKA\nfor Modders\n\nWritten in Python 3.8.5\n\n------------------------------使い方------------------------------")
        self.help_title_label.setFont(QtGui.QFont("Ariel", 10))
        self.help_title_label.setAlignment(QtCore.Qt.AlignHCenter)

    def create_category_window_command(self):
        print("Select Create Category")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.create_category_window = QtWidgets.QDialog()
        self.create_category_window.resize(400, 400)
        self.create_category_window.setWindowIcon(icon)
        self.create_category_window.setWindowTitle('カテゴリー作成')
        self.create_category_window.setFont(QtGui.QFont("Meiryo", 20))

        self.category_title_label = QtWidgets.QLabel(self.create_category_window)
        self.category_title_label.setGeometry(QtCore.QRect(0, 10, 400, 30))
        self.category_title_label.setObjectName("TITLE")
        self.category_title_label.setText("カテゴリー作成")
        self.category_title_label.setFont(QtGui.QFont("Meiryo", 20))
        self.category_title_label.setAlignment(QtCore.Qt.AlignHCenter)

        self.tag_input = QtWidgets.QTextEdit(self.create_category_window)
        self.tag_input.setGeometry(QtCore.QRect(120, 75, 150, 25))
        self.tag_input.setText("SOV")
        self.tag_input.setFont(QtGui.QFont("Ariel", 10))

        self.tag_label = QtWidgets.QLabel(self.create_category_window)
        self.tag_label.setGeometry(QtCore.QRect(20, 83, 100, 20))
        self.tag_label.setObjectName("TITLE")
        self.tag_label.setText("国家タグ")
        self.tag_label.setFont(QtGui.QFont("Meiryo", 10))
        self.tag_label.setAlignment(QtCore.Qt.AlignHCenter)

        self.category_title_input = QtWidgets.QTextEdit(self.create_category_window)
        self.category_title_input.setGeometry(QtCore.QRect(120, 115, 180, 25))
        self.category_title_input.setText("SOV_world_revolution")
        self.category_title_input.setFont(QtGui.QFont("Ariel", 10))

        self.category_title_label = QtWidgets.QLabel(self.create_category_window)
        self.category_title_label.setGeometry(QtCore.QRect(15, 123, 100, 20))
        self.category_title_label.setObjectName("TITLE")
        self.category_title_label.setText("カテゴリーの名前")
        self.category_title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.category_title_label.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.select_icon_button = QtWidgets.QPushButton(self.create_category_window)
        self.select_icon_button.setGeometry(QtCore.QRect(20, 210, 150, 20))
        self.select_icon_button.setText("アイコン選択")
        self.select_icon_button.setObjectName("Button")
        self.select_icon_button.setFont(QtGui.QFont("Meiryo", 10))
        self.select_icon_button.clicked.connect(self.create_icon_list_window_command)

        self.category_icon_label = QtWidgets.QLabel(self.create_category_window)
        self.category_icon_label.setGeometry(QtCore.QRect(200, 175, 100, 100))
        self.category_icon_label.setObjectName("icon")
        
        self.select_picture_button = QtWidgets.QPushButton(self.create_category_window)
        self.select_picture_button.setGeometry(QtCore.QRect(20, 300, 150, 20))
        self.select_picture_button.setText("写真選択")
        self.select_picture_button.setObjectName("Button")
        self.select_picture_button.setFont(QtGui.QFont("Meiryo", 10))
        self.select_picture_button.clicked.connect(self.create_gfx_list_window_command)

        self.category_picture_label = QtWidgets.QLabel(self.create_category_window)
        self.category_picture_label.setGeometry(QtCore.QRect(200, 255, 120, 120))
        self.category_picture_label.setObjectName("icon")
        
        self.generate_button = QtWidgets.QPushButton(self.create_category_window)
        self.generate_button.setGeometry(QtCore.QRect(150, 370, 100, 20))
        self.generate_button.setText("作成")
        self.generate_button.setObjectName("Button")
        self.generate_button.setFont(QtGui.QFont("Meiryo", 10))
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
        self.input_file = QtWidgets.QFileDialog.getOpenFileName(self.create_category_window, 'Open File', '', 'TGA Files(*.tga);;All Files(*)')
        qpixmapvar.load(self.input_file[0])
        self.category_icon_label.setPixmap(qpixmapvar)
        category_icon_path = self.input_file[0]
        icon_splited = category_icon_path.split('/')
        icon_last = icon_splited[-1:]
        icon_real = ''.join(icon_last)
        icon_really = icon_real.rstrip('.tga')

    def create_gfx_list_window_command(self):
        print("Select Picture List")
        global category_picture_path
        global picture_really
        qpixmapvar_picture = QtGui.QPixmap()
        playsound("sound/click_sound.mp3")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.input_gfx_file = QtWidgets.QFileDialog.getOpenFileName(self.create_category_window, 'Open File', '', 'TGA Files(*.tga);; All Files(*)')
        qpixmapvar_picture.load(self.input_gfx_file[0])
        self.category_picture_label.setPixmap(qpixmapvar_picture)
        category_picture_path = self.input_gfx_file[0]
        picture_splited = category_picture_path.split('/')
        picture_last = picture_splited[-1:]
        picture_real = ''.join(picture_last)
        picture_really = picture_real.rstrip('.tga')
    
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
        category_output.write('\n		tag = '+country_tag)
        category_output.write('\n	}')
        category_output.write('\n}')

    def create_decision_window_command(self):
        print("Select Create Decision")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.create_decision_window = QtWidgets.QDialog()
        self.create_decision_window.resize(400, 350)
        self.create_decision_window.setWindowIcon(icon)
        self.create_decision_window.setWindowTitle('デシジョン作成')

        self.label = QtWidgets.QLabel(self.create_decision_window)
        self.label.setGeometry(QtCore.QRect(100, 10, 200, 40))
        self.label.setObjectName("TITLE")
        self.label.setText("デシジョン作成")
        self.label.setFont(QtGui.QFont("Meiryo", 20))
        self.label.setAlignment(QtCore.Qt.AlignHCenter)

        self.title_label = QtWidgets.QLabel(self.create_decision_window)
        self.title_label.setGeometry(QtCore.QRect(20, 83, 100, 20))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("デシジョンの名前")
        self.title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter)

        self.title_input = QtWidgets.QTextEdit(self.create_decision_window)
        self.title_input.setGeometry(QtCore.QRect(130, 80, 250, 25))
        self.title_input.setText("SOV_spread_revolution_in_germany")
        self.title_input.setFont(QtGui.QFont("Ariel", 10))

        self.title_label = QtWidgets.QLabel(self.create_decision_window)
        self.title_label.setGeometry(QtCore.QRect(20, 113, 100, 20))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("表示条件")
        self.title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.select_visible_button = QtWidgets.QPushButton(self.create_decision_window)
        self.select_visible_button.setGeometry(QtCore.QRect(130, 110, 250, 25))
        self.select_visible_button.setText("選択")
        self.select_visible_button.setObjectName("Button")
        self.select_visible_button.clicked.connect(self.select_visible_option)
        self.select_visible_button.setFont(QtGui.QFont("Meiryo", 10))

        self.title_label = QtWidgets.QLabel(self.create_decision_window)
        self.title_label.setGeometry(QtCore.QRect(20, 143, 100, 20))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("選択可能条件")
        self.title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.select_available_button = QtWidgets.QPushButton(self.create_decision_window)
        self.select_available_button.setGeometry(QtCore.QRect(130, 140, 250, 25))
        self.select_available_button.setText("選択")
        self.select_available_button.setObjectName("Button")
        self.select_available_button.setFont(QtGui.QFont("Meiryo", 10))

        self.title_label = QtWidgets.QLabel(self.create_decision_window)
        self.title_label.setGeometry(QtCore.QRect(20, 173, 100, 20))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("必要政治力")
        self.title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.select_cost_button = QtWidgets.QSpinBox(self.create_decision_window)
        self.select_cost_button.setGeometry(QtCore.QRect(130, 170, 250, 25))
        self.select_cost_button.setRange(-100, 100)
        self.select_cost_button.setObjectName("Button")

        self.title_label = QtWidgets.QLabel(self.create_decision_window)
        self.title_label.setGeometry(QtCore.QRect(20, 203, 100, 20))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("完了時の効果")
        self.title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.select_complete_button = QtWidgets.QPushButton(self.create_decision_window)
        self.select_complete_button.setGeometry(QtCore.QRect(130, 200, 250, 25))
        self.select_complete_button.setText("選択")
        self.select_complete_button.setObjectName("Button")
        self.select_complete_button.setFont(QtGui.QFont("Meiryo", 10))

        self.title_label = QtWidgets.QLabel(self.create_decision_window)
        self.title_label.setGeometry(QtCore.QRect(20, 233, 100, 20))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("消えるまでの時間")
        self.title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.select_remove_days_button = QtWidgets.QSpinBox(self.create_decision_window)
        self.select_remove_days_button.setGeometry(QtCore.QRect(130, 230, 250, 25))
        self.select_remove_days_button.setObjectName("Button")

        self.title_label = QtWidgets.QLabel(self.create_decision_window)
        self.title_label.setGeometry(QtCore.QRect(20, 263, 100, 20))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("消去時の効果")
        self.title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.select_remove_button = QtWidgets.QPushButton(self.create_decision_window)
        self.select_remove_button.setGeometry(QtCore.QRect(130, 260, 250, 25))
        self.select_remove_button.setText("選択")
        self.select_remove_button.setObjectName("Button")
        self.select_remove_button.setFont(QtGui.QFont("Meiryo", 10))

        self.title_label = QtWidgets.QLabel(self.create_decision_window)
        self.title_label.setGeometry(QtCore.QRect(20, 293, 100, 20))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("一度のみ実行")
        self.title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.select_remove_button = QtWidgets.QCheckBox(self.create_decision_window)
        self.select_remove_button.setGeometry(QtCore.QRect(130, 290, 250, 25))
        self.select_remove_button.setObjectName("Button")
        
        self.generate_decision_button = QtWidgets.QPushButton(self.create_decision_window)
        self.generate_decision_button.setGeometry(QtCore.QRect(75, 320, 250, 25))
        self.generate_decision_button.setText("作成")
        self.generate_decision_button.setObjectName("Button")
        self.generate_decision_button.setFont(QtGui.QFont("Meiryo", 10))

        self.create_decision_window.show()

    def select_visible_option(self):
        print("select visible")
        playsound("sound/click_sound.mp3")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_visible_window = QtWidgets.QDialog()
        self.select_visible_window.resize(350, 350)
        self.select_visible_window.setWindowIcon(icon)
        self.select_visible_window.setWindowTitle('条件選択')
        
        self.select_general_button = QtWidgets.QPushButton(self.select_visible_window)
        self.select_general_button.setGeometry(QtCore.QRect(10, 10, 100, 100))
        self.select_general_button.setText("一般")
        self.select_general_button.setFont(QtGui.QFont("Meiryo", 15))
        self.select_general_button.setObjectName("Button")
        
        self.select_politics_button = QtWidgets.QPushButton(self.select_visible_window)
        self.select_politics_button.setGeometry(QtCore.QRect(120, 10, 100, 100))
        self.select_politics_button.setText("政治")
        self.select_politics_button.setFont(QtGui.QFont("Meiryo", 15))
        self.select_politics_button.setObjectName("Button")
        
        self.select_building_button = QtWidgets.QPushButton(self.select_visible_window)
        self.select_building_button.setGeometry(QtCore.QRect(230, 10, 100, 100))
        self.select_building_button.setText("建設")
        self.select_building_button.setFont(QtGui.QFont("Meiryo", 15))
        self.select_building_button.setObjectName("Button")
        
        self.select_technology_button = QtWidgets.QPushButton(self.select_visible_window)
        self.select_technology_button.setGeometry(QtCore.QRect(10, 120, 100, 100))
        self.select_technology_button.setText("研究")
        self.select_technology_button.setFont(QtGui.QFont("Meiryo", 15))
        self.select_technology_button.setObjectName("Button")
        
        self.select_ideas_button = QtWidgets.QPushButton(self.select_visible_window)
        self.select_ideas_button.setGeometry(QtCore.QRect(120, 120, 100, 100))
        self.select_ideas_button.setText("国民精神")
        self.select_ideas_button.setFont(QtGui.QFont("Meiryo", 15))
        self.select_ideas_button.setObjectName("Button")
        
        self.select_diplomacy_button = QtWidgets.QPushButton(self.select_visible_window)
        self.select_diplomacy_button.setGeometry(QtCore.QRect(230, 120, 100, 100))
        self.select_diplomacy_button.setText("外交")
        self.select_diplomacy_button.setFont(QtGui.QFont("Meiryo", 15))
        self.select_diplomacy_button.setObjectName("Button")
        
        self.select_war_button = QtWidgets.QPushButton(self.select_visible_window)
        self.select_war_button.setGeometry(QtCore.QRect(10, 230, 100, 100))
        self.select_war_button.setText("戦争")
        self.select_war_button.setFont(QtGui.QFont("Meiryo", 15))
        self.select_war_button.setObjectName("Button")
        
        self.select_state_button = QtWidgets.QPushButton(self.select_visible_window)
        self.select_state_button.setGeometry(QtCore.QRect(120, 230, 100, 100))
        self.select_state_button.setText("州")
        self.select_state_button.setFont(QtGui.QFont("Meiryo", 15))
        self.select_state_button.setObjectName("Button")

        self.select_visible_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())