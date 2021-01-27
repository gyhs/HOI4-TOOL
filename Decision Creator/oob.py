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
        self.create_decision_button.setText("ディシジョン作成")
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
        self.create_decision_window.resize(900, 650)
        self.create_decision_window.setWindowIcon(icon)
        self.create_decision_window.setWindowTitle('ディシジョン作成')

        self.label = QtWidgets.QLabel(self.create_decision_window)
        self.label.setGeometry(QtCore.QRect(0, 10, 890, 40))
        self.label.setObjectName("TITLE")
        self.label.setText("ディシジョン作成")
        self.label.setFont(QtGui.QFont("Meiryo", 20))
        self.label.setAlignment(QtCore.Qt.AlignHCenter)

        self.title_label = QtWidgets.QLabel(self.create_decision_window)
        self.title_label.setGeometry(QtCore.QRect(20, 73, 100, 20))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("カテゴリーの名前")
        self.title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.select_category_name_button = QtWidgets.QPushButton(self.create_decision_window)
        self.select_category_name_button.setGeometry(QtCore.QRect(390, 70, 25, 20))
        self.select_category_name_button.setText("...")
        self.select_category_name_button.setObjectName("Button")
        self.select_category_name_button.clicked.connect(self.select_category_name_option)
        self.select_category_name_button.setFont(QtGui.QFont("Meiryo", 10))

        self.category_title_input = QtWidgets.QTextEdit(self.create_decision_window)
        self.category_title_input.setGeometry(QtCore.QRect(130, 70, 250, 25))
        self.category_title_input.setText("SOV_world_revolution")
        self.category_title_input.setFont(QtGui.QFont("Ariel", 10))

        self.title_label = QtWidgets.QLabel(self.create_decision_window)
        self.title_label.setGeometry(QtCore.QRect(-5, 103, 150, 20))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("ディシジョンの名前")
        self.title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter)

        self.title_input = QtWidgets.QTextEdit(self.create_decision_window)
        self.title_input.setGeometry(QtCore.QRect(130, 100, 250, 25))
        self.title_input.setText("SOV_spread_revolution_in_germany")
        self.title_input.setFont(QtGui.QFont("Ariel", 10))

        self.title_label = QtWidgets.QLabel(self.create_decision_window)
        self.title_label.setGeometry(QtCore.QRect(20, 130, 100, 200))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("表示条件")
        self.title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.select_visible_button = QtWidgets.QPushButton(self.create_decision_window)
        self.select_visible_button.setGeometry(QtCore.QRect(390, 130, 25, 200))
        self.select_visible_button.setText("選\n択")
        self.select_visible_button.setObjectName("Button")
        self.select_visible_button.clicked.connect(self.select_visible_option)
        self.select_visible_button.setFont(QtGui.QFont("Meiryo", 10))

        self.select_visible_input = QtWidgets.QTextEdit(self.create_decision_window)
        self.select_visible_input.setGeometry(QtCore.QRect(130, 130, 250, 200))
        self.select_visible_input.setText("")
        self.select_visible_input.setFont(QtGui.QFont("Ariel", 10))

        self.title_label = QtWidgets.QLabel(self.create_decision_window)
        self.title_label.setGeometry(QtCore.QRect(20, 350, 100, 200))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("選択可能条件")
        self.title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.select_available_button = QtWidgets.QPushButton(self.create_decision_window)
        self.select_available_button.setGeometry(QtCore.QRect(390, 350, 25, 200))
        self.select_available_button.setText("選\n択")
        self.select_available_button.setObjectName("Button")
        self.select_available_button.clicked.connect(self.select_visible_option)
        self.select_available_button.setFont(QtGui.QFont("Meiryo", 10))

        self.select_available_input = QtWidgets.QTextEdit(self.create_decision_window)
        self.select_available_input.setGeometry(QtCore.QRect(130, 350, 250, 200))
        self.select_available_input.setText("")
        self.select_available_input.setFont(QtGui.QFont("Ariel", 10))

        self.title_label = QtWidgets.QLabel(self.create_decision_window)
        self.title_label.setGeometry(QtCore.QRect(20, 573, 100, 20))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("必要政治力")
        self.title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.select_cost_button = QtWidgets.QSpinBox(self.create_decision_window)
        self.select_cost_button.setGeometry(QtCore.QRect(130, 570, 250, 25))
        self.select_cost_button.setRange(-200, 200)
        self.select_cost_button.setObjectName("Button")

        self.complete_title_label = QtWidgets.QLabel(self.create_decision_window)
        self.complete_title_label.setGeometry(QtCore.QRect(450, 73, 100, 200))
        self.complete_title_label.setObjectName("TITLE")
        self.complete_title_label.setText("完了時の効果")
        self.complete_title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.complete_title_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.select_complete_button = QtWidgets.QPushButton(self.create_decision_window)
        self.select_complete_button.setGeometry(QtCore.QRect(835, 70, 25, 200))
        self.select_complete_button.setText("選\n択")
        self.select_complete_button.setObjectName("Button")
        self.select_complete_button.clicked.connect(self.select_visible_option)
        self.select_complete_button.setFont(QtGui.QFont("Meiryo", 10))

        self.select_complete_input = QtWidgets.QTextEdit(self.create_decision_window)
        self.select_complete_input.setGeometry(QtCore.QRect(575, 70, 250, 200))
        self.select_complete_input.setText("")
        self.select_complete_input.setFont(QtGui.QFont("Ariel", 10))

        self.title_label = QtWidgets.QLabel(self.create_decision_window)
        self.title_label.setGeometry(QtCore.QRect(450, 293, 100, 20))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("消えるまでの時間")
        self.title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.select_remove_days_button = QtWidgets.QSpinBox(self.create_decision_window)
        self.select_remove_days_button.setGeometry(QtCore.QRect(575, 290, 250, 25))
        self.select_remove_days_button.setObjectName("Button")

        self.remove_effect_title_label = QtWidgets.QLabel(self.create_decision_window)
        self.remove_effect_title_label.setGeometry(QtCore.QRect(450, 338, 100, 200))
        self.remove_effect_title_label.setObjectName("TITLE")
        self.remove_effect_title_label.setText("消去時の効果")
        self.remove_effect_title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.remove_effect_title_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.remove_effect_button = QtWidgets.QPushButton(self.create_decision_window)
        self.remove_effect_button.setGeometry(QtCore.QRect(835, 335, 25, 200))
        self.remove_effect_button.setText("選\n択")
        self.remove_effect_button.setObjectName("Button")
        self.remove_effect_button.clicked.connect(self.select_visible_option)
        self.remove_effect_button.setFont(QtGui.QFont("Meiryo", 10))

        self.remove_effect_input = QtWidgets.QTextEdit(self.create_decision_window)
        self.remove_effect_input.setGeometry(QtCore.QRect(575, 335, 250, 200))
        self.remove_effect_input.setText("")
        self.remove_effect_input.setFont(QtGui.QFont("Ariel", 10))

        self.title_label = QtWidgets.QLabel(self.create_decision_window)
        self.title_label.setGeometry(QtCore.QRect(450, 548, 100, 20))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("一度のみ実行")
        self.title_label.setFont(QtGui.QFont("Meiryo", 10))
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.fire_only_once_button = QtWidgets.QCheckBox(self.create_decision_window)
        self.fire_only_once_button.setGeometry(QtCore.QRect(575, 545, 250, 25))
        self.fire_only_once_button.setObjectName("Button")
        
        self.generate_decision_button = QtWidgets.QPushButton(self.create_decision_window)
        self.generate_decision_button.setGeometry(QtCore.QRect(450, 580, 410, 25))
        self.generate_decision_button.setText("作成")
        self.generate_decision_button.setObjectName("Button")
        self.generate_decision_button.clicked.connect(self.select_visible_option)
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
        self.select_general_button.clicked.connect(self.select_general_option)
        
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

    def select_general_option(self):
        print("select General Option")
        playsound("sound/click_sound.mp3")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.general_option_window = QtWidgets.QDialog(self.select_visible_window)
        self.general_option_window.resize(300, 340)
        self.general_option_window.setWindowIcon(icon)
        self.general_option_window.setWindowTitle('条件選択')
        
        self.exist = QtWidgets.QPushButton(self.general_option_window)
        self.exist.setGeometry(QtCore.QRect(10, 10, 280, 25))
        self.exist.setText("exist")
        self.exist.setFont(QtGui.QFont("Meiryo", 10))
        self.exist.setObjectName("Button")
        self.exist.clicked.connect(self.select_exist)
        
        self.tag = QtWidgets.QPushButton(self.general_option_window)
        self.tag.setGeometry(QtCore.QRect(10, 40, 280, 25))
        self.tag.setText("tag")
        self.tag.setFont(QtGui.QFont("Meiryo", 10))
        self.tag.setObjectName("Button")
        self.tag.clicked.connect(self.select_tag)
        
        self.original_tag = QtWidgets.QPushButton(self.general_option_window)
        self.original_tag.setGeometry(QtCore.QRect(10, 70, 280, 25))
        self.original_tag.setText("original_tag")
        self.original_tag.setFont(QtGui.QFont("Meiryo", 10))
        self.original_tag.setObjectName("Button")
        self.original_tag.clicked.connect(self.select_original_tag)
        
        self.is_ai = QtWidgets.QPushButton(self.general_option_window)
        self.is_ai.setGeometry(QtCore.QRect(10, 100, 280, 25))
        self.is_ai.setText("is_ai")
        self.is_ai.setFont(QtGui.QFont("Meiryo", 10))
        self.is_ai.setObjectName("Button")
        self.is_ai.clicked.connect(self.select_is_ai)
        
        self.has_country_flag = QtWidgets.QPushButton(self.general_option_window)
        self.has_country_flag.setGeometry(QtCore.QRect(10, 130, 280, 25))
        self.has_country_flag.setText("has_country_flag")
        self.has_country_flag.setFont(QtGui.QFont("Meiryo", 10))
        self.has_country_flag.setObjectName("Button")
        self.has_country_flag.clicked.connect(self.select_has_country_flag)
        
        self.has_cosmetic_tag = QtWidgets.QPushButton(self.general_option_window)
        self.has_cosmetic_tag.setGeometry(QtCore.QRect(10, 160, 280, 25))
        self.has_cosmetic_tag.setText("has_cosmetic_tag")
        self.has_cosmetic_tag.setFont(QtGui.QFont("Meiryo", 10))
        self.has_cosmetic_tag.setObjectName("Button")
        self.has_cosmetic_tag.clicked.connect(self.select_has_cosmetic_tag)
        
        self.has_decision = QtWidgets.QPushButton(self.general_option_window)
        self.has_decision.setGeometry(QtCore.QRect(10, 190, 280, 25))
        self.has_decision.setText("has_decision")
        self.has_decision.setFont(QtGui.QFont("Meiryo", 10))
        self.has_decision.setObjectName("Button")
        self.has_decision.clicked.connect(self.select_has_decision)
        
        self.has_active_mission = QtWidgets.QPushButton(self.general_option_window)
        self.has_active_mission.setGeometry(QtCore.QRect(10, 220, 280, 25))
        self.has_active_mission.setText("has_active_mission")
        self.has_active_mission.setFont(QtGui.QFont("Meiryo", 10))
        self.has_active_mission.setObjectName("Button")
        self.has_active_mission.clicked.connect(self.select_has_active_mission)
        
        self.has_focus_tree = QtWidgets.QPushButton(self.general_option_window)
        self.has_focus_tree.setGeometry(QtCore.QRect(10, 250, 280, 25))
        self.has_focus_tree.setText("has_focus_tree")
        self.has_focus_tree.setFont(QtGui.QFont("Meiryo", 10))
        self.has_focus_tree.setObjectName("Button")
        self.has_focus_tree.clicked.connect(self.select_has_focus_tree)
        
        self.has_completed_focus = QtWidgets.QPushButton(self.general_option_window)
        self.has_completed_focus.setGeometry(QtCore.QRect(10, 280, 280, 25))
        self.has_completed_focus.setText("has_completed_focus")
        self.has_completed_focus.setFont(QtGui.QFont("Meiryo", 10))
        self.has_completed_focus.setObjectName("Button")
        self.has_completed_focus.clicked.connect(self.select_has_completed_focus)
        
        self.focus_progress = QtWidgets.QPushButton(self.general_option_window)
        self.focus_progress.setGeometry(QtCore.QRect(10, 310, 280, 25))
        self.focus_progress.setText("focus_progress")
        self.focus_progress.setFont(QtGui.QFont("Meiryo", 10))
        self.focus_progress.setObjectName("Button")
        self.focus_progress.clicked.connect(self.select_focus_progress)
        
        self.general_option_window.show()

    def select_exist(self):
        playsound("sound/click_sound.mp3")
        self.select_visible_input.setText("TAG = { exists = yes }")
        self.general_option_window.close()
        self.select_visible_window.close()

    def select_tag(self):
        playsound("sound/click_sound.mp3")
        self.select_visible_input.setText("tag = SOV")
        self.general_option_window.close()
        self.select_visible_window.close()

    def select_original_tag(self):
        playsound("sound/click_sound.mp3")
        self.select_visible_input.setText("original_tag = GER")
        self.general_option_window.close()
        self.select_visible_window.close()

    def select_is_ai(self):
        playsound("sound/click_sound.mp3")
        self.select_visible_input.setText("is_ai = yes")
        self.general_option_window.close()
        self.select_visible_window.close()

    def select_has_country_flag(self):
        playsound("sound/click_sound.mp3")
        self.select_visible_input.setText("has_country_flag = SOV_TEMP")
        self.general_option_window.close()
        self.select_visible_window.close()

    def select_has_cosmetic_tag(self):
        playsound("sound/click_sound.mp3")
        self.select_visible_input.setText("has_cosmetic_tag = SOV_TEMP")
        self.general_option_window.close()
        self.select_visible_window.close()

    def select_has_decision(self):
        playsound("sound/click_sound.mp3")
        self.select_visible_input.setText("has_decision = my_decision")
        self.general_option_window.close()
        self.select_visible_window.close()

    def select_has_active_mission(self):
        playsound("sound/click_sound.mp3")
        self.select_visible_input.setText("has_active_mission = my_mission")
        self.general_option_window.close()
        self.select_visible_window.close()

    def select_has_focus_tree(self):
        playsound("sound/click_sound.mp3")
        self.select_visible_input.setText("has_focus_tree = SOV_focus_tree")
        self.general_option_window.close()
        self.select_visible_window.close()

    def select_has_completed_focus(self):
        playsound("sound/click_sound.mp3")
        self.select_visible_input.setText("has_completed_focus = GER_focus")
        self.general_option_window.close()
        self.select_visible_window.close()

    def select_focus_progress(self):
        playsound("sound/click_sound.mp3")
        self.select_visible_input.setText("focus_progress = { \n\tfocus = GER_focus\n\tprogress < 0.5\n}")
        self.general_option_window.close()
        self.select_visible_window.close()

    def select_category_name_option(self):
        print("Select Category Name Button")
        playsound("sound/click_sound.mp3")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.input_category_file = QtWidgets.QFileDialog.getOpenFileName(self.create_decision_window, 'Open File', '', 'TEXT Files(*.txt);;All Files(*)')
        get_category_title = open(self.input_category_file[0], 'r')
        category_file_line = get_category_title.readlines()
        category_file_line.reverse()
        category_title_line = category_file_line.pop()
        comptete_category_title = category_title_line.rstrip(' = {\n')
        self.category_title_input.setText(comptete_category_title)

        get_category_title.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())