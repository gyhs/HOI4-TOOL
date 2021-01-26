from PyQt5 import QtCore, QtGui, QtWidgets
from playsound import playsound
import functools
import sys 

print('Creating Log...')
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1092, 553)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowTitle("Division Designer")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/module_slot_icon_locked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/button_reset_123x34.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        support_unit_anti_air_icon = QtGui.QIcon()
        support_unit_anti_air_icon.addPixmap(QtGui.QPixmap("company/support_unit_anti_air_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1092, 553))
        self.label.setPixmap(QtGui.QPixmap("ui/division_designer_popup_bg.png"))
        self.label.setObjectName("label")

        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setGeometry(QtCore.QRect(430, 10, 250, 30))
        self.title_label.setObjectName("TITLE")
        self.title_label.setText("Division Designer")
        self.title_label.setFont(QtGui.QFont("Ariel", 20))
        self.title_label.setStyleSheet("Color : white")

        self.support_title_label = QtWidgets.QLabel(Dialog)
        self.support_title_label.setGeometry(QtCore.QRect(30, 190, 250, 30))
        self.support_title_label.setObjectName("SUPPORTTITLE")
        self.support_title_label.setText("Support")
        self.support_title_label.setFont(QtGui.QFont("Ariel", 10))
        self.support_title_label.setStyleSheet("Color : white")

        self.combat_title_label = QtWidgets.QLabel(Dialog)
        self.combat_title_label.setGeometry(QtCore.QRect(430, 190, 250, 30))
        self.combat_title_label.setObjectName("COMBATTTITLE")
        self.combat_title_label.setText("Combat")
        self.combat_title_label.setFont(QtGui.QFont("Ariel", 10))
        self.combat_title_label.setStyleSheet("Color : white")
        
        self.companies_button_1 = QtWidgets.QPushButton(Dialog)
        self.companies_button_1.setGeometry(QtCore.QRect(27, 250, 64, 53))
        self.companies_button_1.setIcon(support_unit_anti_air_icon)
        self.companies_button_1.setIconSize(QtCore.QSize(76, 42))
        self.companies_button_1.setStyleSheet("background-image:url(ui/div_subunit_item_bg.png);" "background-color: #10120D;" "border-style: solid")
        self.companies_button_1.setObjectName("Button")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())