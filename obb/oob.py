from PyQt5 import QtCore, QtGui, QtWidgets
from playsound import playsound
import functools
import sys 

print('Creating Log...')

company_1_current_icon = 1
company_2_current_icon = 1
company_3_current_icon = 1
company_4_current_icon = 1
company_5_current_icon = 1

battalion_1_current_icon = 1
battalion_2_current_icon = 1
battalion_3_current_icon = 1
battalion_4_current_icon = 1
battalion_5_current_icon = 1

battalion_11_current_icon = 1
battalion_12_current_icon = 1
battalion_13_current_icon = 1
battalion_14_current_icon = 1
battalion_15_current_icon = 1

battalion_21_current_icon = 1
battalion_22_current_icon = 1
battalion_23_current_icon = 1
battalion_24_current_icon = 1
battalion_25_current_icon = 1

battalion_31_current_icon = 1
battalion_32_current_icon = 1
battalion_33_current_icon = 1
battalion_34_current_icon = 1
battalion_35_current_icon = 1

battalion_41_current_icon = 1
battalion_42_current_icon = 1
battalion_43_current_icon = 1
battalion_44_current_icon = 1
battalion_45_current_icon = 1

battalion_51_current_icon = 1
battalion_52_current_icon = 1
battalion_53_current_icon = 1
battalion_54_current_icon = 1
battalion_55_current_icon = 1

priority = 1

max_speed = 0
hp = 0
organization = 0
recovery_rate = 0
reconnaissance = 0
suppression = 0
weight = 0
supply_use = 0
reliability = 0
tricleback = 0
exp_loss = 0

soft_attack = 0
hard_attack = 0
air_attack = 0
defence = 0
breakthrough = 0
armor = 0
piercing = 0
initiative = 0
entrenchment = 0
eq_capture_ratio = 0
combat_width = 0

manpower = 0
training_time = 0
fuel_capacity = 0
fuel_usage = 0
amtracs = 0
infantry_eq = 0

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1092, 553)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/module_slot_icon_locked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/button_reset_123x34.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

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

        self.base_stats_title_label = QtWidgets.QLabel(Dialog)
        self.base_stats_title_label.setGeometry(QtCore.QRect(550, 43, 250, 30))
        self.base_stats_title_label.setObjectName("BASE_TITLE")
        self.base_stats_title_label.setText("Base Stats")
        self.base_stats_title_label.setFont(QtGui.QFont("Ariel", 15))

        self.max_speed_stats_label = QtWidgets.QLabel(Dialog)
        self.max_speed_stats_label.setGeometry(QtCore.QRect(550, 75, 100, 15))
        self.max_speed_stats_label.setObjectName("base_stats")
        self.max_speed_stats_label.setText("Max Speed:")
        self.max_speed_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.max_speed_culculate_label = QtWidgets.QLabel(Dialog)
        self.max_speed_culculate_label.setGeometry(QtCore.QRect(610, 75, 100, 15))
        self.max_speed_culculate_label.setObjectName("combat_stats")
        self.max_speed_culculate_label.setText('%s km/h' %max_speed)
        self.max_speed_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.max_speed_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.hp_stats_label = QtWidgets.QLabel(Dialog)
        self.hp_stats_label.setGeometry(QtCore.QRect(550, 95, 100, 15))
        self.hp_stats_label.setObjectName("base_stats")
        self.hp_stats_label.setText("HP:")
        self.hp_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.hp_culculate_label = QtWidgets.QLabel(Dialog)
        self.hp_culculate_label.setGeometry(QtCore.QRect(610, 95, 100, 15))
        self.hp_culculate_label.setObjectName("combat_stats")
        self.hp_culculate_label.setText('%s' %hp)
        self.hp_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.hp_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.org_stats_label = QtWidgets.QLabel(Dialog)
        self.org_stats_label.setGeometry(QtCore.QRect(550, 115, 100, 15))
        self.org_stats_label.setObjectName("base_stats")
        self.org_stats_label.setText("Organization:")
        self.org_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.org_culculate_label = QtWidgets.QLabel(Dialog)
        self.org_culculate_label.setGeometry(QtCore.QRect(610, 115, 100, 15))
        self.org_culculate_label.setObjectName("combat_stats")
        self.org_culculate_label.setText('%s' %organization)
        self.org_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.org_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.recovery_stats_label = QtWidgets.QLabel(Dialog)
        self.recovery_stats_label.setGeometry(QtCore.QRect(550, 135, 100, 15))
        self.recovery_stats_label.setObjectName("base_stats")
        self.recovery_stats_label.setText("Recovery Rate:")
        self.recovery_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.recovery_culculate_label = QtWidgets.QLabel(Dialog)
        self.recovery_culculate_label.setGeometry(QtCore.QRect(610, 135, 100, 15))
        self.recovery_culculate_label.setObjectName("combat_stats")
        self.recovery_culculate_label.setText('%s' %recovery_rate)
        self.recovery_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.recovery_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.reconnaissance_stats_label = QtWidgets.QLabel(Dialog)
        self.reconnaissance_stats_label.setGeometry(QtCore.QRect(550, 155, 100, 15))
        self.reconnaissance_stats_label.setObjectName("base_stats")
        self.reconnaissance_stats_label.setText("Reconnaissance:")
        self.reconnaissance_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.reconnaissance_culculate_label = QtWidgets.QLabel(Dialog)
        self.reconnaissance_culculate_label.setGeometry(QtCore.QRect(610, 155, 100, 15))
        self.reconnaissance_culculate_label.setObjectName("combat_stats")
        self.reconnaissance_culculate_label.setText('%s' %reconnaissance)
        self.reconnaissance_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.reconnaissance_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.suppression_stats_label = QtWidgets.QLabel(Dialog)
        self.suppression_stats_label.setGeometry(QtCore.QRect(550, 175, 100, 15))
        self.suppression_stats_label.setObjectName("base_stats")
        self.suppression_stats_label.setText("Suppression:")
        self.suppression_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.suppression_culculate_label = QtWidgets.QLabel(Dialog)
        self.suppression_culculate_label.setGeometry(QtCore.QRect(610, 175, 100, 15))
        self.suppression_culculate_label.setObjectName("combat_stats")
        self.suppression_culculate_label.setText('%s' %suppression)
        self.suppression_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.suppression_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.weight_stats_label = QtWidgets.QLabel(Dialog)
        self.weight_stats_label.setGeometry(QtCore.QRect(550, 195, 100, 15))
        self.weight_stats_label.setObjectName("base_stats")
        self.weight_stats_label.setText("Weight:")
        self.weight_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.weight_culculate_label = QtWidgets.QLabel(Dialog)
        self.weight_culculate_label.setGeometry(QtCore.QRect(610, 195, 100, 15))
        self.weight_culculate_label.setObjectName("combat_stats")
        self.weight_culculate_label.setText('%s' %weight)
        self.weight_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.weight_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.supply_use_stats_label = QtWidgets.QLabel(Dialog)
        self.supply_use_stats_label.setGeometry(QtCore.QRect(550, 215, 100, 15))
        self.supply_use_stats_label.setObjectName("base_stats")
        self.supply_use_stats_label.setText("Supply use:")
        self.supply_use_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.supply_use_culculate_label = QtWidgets.QLabel(Dialog)
        self.supply_use_culculate_label.setGeometry(QtCore.QRect(610, 215, 100, 15))
        self.supply_use_culculate_label.setObjectName("combat_stats")
        self.supply_use_culculate_label.setText('%s' %supply_use)
        self.supply_use_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.supply_use_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.reliability_stats_label = QtWidgets.QLabel(Dialog)
        self.reliability_stats_label.setGeometry(QtCore.QRect(550, 235, 100, 15))
        self.reliability_stats_label.setObjectName("base_stats")
        self.reliability_stats_label.setText("Reliability:")
        self.reliability_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.reliability_culculate_label = QtWidgets.QLabel(Dialog)
        self.reliability_culculate_label.setGeometry(QtCore.QRect(610, 235, 100, 15))
        self.reliability_culculate_label.setObjectName("combat_stats")
        self.reliability_culculate_label.setText('%s' %reliability)
        self.reliability_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.reliability_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.trickleback_stats_label = QtWidgets.QLabel(Dialog)
        self.trickleback_stats_label.setGeometry(QtCore.QRect(550, 255, 100, 15))
        self.trickleback_stats_label.setObjectName("base_stats")
        self.trickleback_stats_label.setText("Trickleback:")
        self.trickleback_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.trickleback_culculate_label = QtWidgets.QLabel(Dialog)
        self.trickleback_culculate_label.setGeometry(QtCore.QRect(610, 255, 100, 15))
        self.trickleback_culculate_label.setObjectName("combat_stats")
        self.trickleback_culculate_label.setText('%s' %tricleback)
        self.trickleback_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.trickleback_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.exp_loss_stats_label = QtWidgets.QLabel(Dialog)
        self.exp_loss_stats_label.setGeometry(QtCore.QRect(550, 275, 100, 15))
        self.exp_loss_stats_label.setObjectName("base_stats")
        self.exp_loss_stats_label.setText("Exp. Loss:")
        self.exp_loss_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.exp_loss_culculate_label = QtWidgets.QLabel(Dialog)
        self.exp_loss_culculate_label.setGeometry(QtCore.QRect(610, 275, 100, 15))
        self.exp_loss_culculate_label.setObjectName("combat_stats")
        self.exp_loss_culculate_label.setText('%s' %exp_loss)
        self.exp_loss_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.exp_loss_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.combat_stats_title_label = QtWidgets.QLabel(Dialog)
        self.combat_stats_title_label.setGeometry(QtCore.QRect(725, 43, 250, 30))
        self.combat_stats_title_label.setObjectName("combat_stats_TITLE")
        self.combat_stats_title_label.setText("Base Stats")
        self.combat_stats_title_label.setFont(QtGui.QFont("Ariel", 15))

        self.soft_attack_stats_label = QtWidgets.QLabel(Dialog)
        self.soft_attack_stats_label.setGeometry(QtCore.QRect(720, 75, 100, 15))
        self.soft_attack_stats_label.setObjectName("combat_stats")
        self.soft_attack_stats_label.setText("Soft attack:")
        self.soft_attack_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.soft_attack_culculate_label = QtWidgets.QLabel(Dialog)
        self.soft_attack_culculate_label.setGeometry(QtCore.QRect(785, 75, 100, 15))
        self.soft_attack_culculate_label.setObjectName("combat_stats")
        self.soft_attack_culculate_label.setText('%s' %soft_attack)
        self.soft_attack_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.soft_attack_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.hard_attack_stats_label = QtWidgets.QLabel(Dialog)
        self.hard_attack_stats_label.setGeometry(QtCore.QRect(720, 95, 100, 15))
        self.hard_attack_stats_label.setObjectName("combat_stats")
        self.hard_attack_stats_label.setText("Hard attack:")
        self.hard_attack_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.hard_attack_culculate_label = QtWidgets.QLabel(Dialog)
        self.hard_attack_culculate_label.setGeometry(QtCore.QRect(785, 95, 100, 15))
        self.hard_attack_culculate_label.setObjectName("combat_stats")
        self.hard_attack_culculate_label.setText('%s' %hard_attack)
        self.hard_attack_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.hard_attack_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.air_attack_stats_label = QtWidgets.QLabel(Dialog)
        self.air_attack_stats_label.setGeometry(QtCore.QRect(720, 115, 100, 15))
        self.air_attack_stats_label.setObjectName("combat_stats")
        self.air_attack_stats_label.setText("Air attack:")
        self.air_attack_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.air_attack_culculate_label = QtWidgets.QLabel(Dialog)
        self.air_attack_culculate_label.setGeometry(QtCore.QRect(785, 115, 100, 15))
        self.air_attack_culculate_label.setObjectName("combat_stats")
        self.air_attack_culculate_label.setText('%s' %air_attack)
        self.air_attack_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.air_attack_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.defense_stats_label = QtWidgets.QLabel(Dialog)
        self.defense_stats_label.setGeometry(QtCore.QRect(720, 135, 100, 15))
        self.defense_stats_label.setObjectName("combat_stats")
        self.defense_stats_label.setText("Defense:")
        self.defense_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.defense_culculate_label = QtWidgets.QLabel(Dialog)
        self.defense_culculate_label.setGeometry(QtCore.QRect(785, 135, 100, 15))
        self.defense_culculate_label.setObjectName("combat_stats")
        self.defense_culculate_label.setText('%s' %defence)
        self.defense_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.defense_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.breakthrough_stats_label = QtWidgets.QLabel(Dialog)
        self.breakthrough_stats_label.setGeometry(QtCore.QRect(720, 155, 100, 15))
        self.breakthrough_stats_label.setObjectName("combat_stats")
        self.breakthrough_stats_label.setText("Breakthrough:")
        self.breakthrough_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.breakthrough_culculate_label = QtWidgets.QLabel(Dialog)
        self.breakthrough_culculate_label.setGeometry(QtCore.QRect(785, 155, 100, 15))
        self.breakthrough_culculate_label.setObjectName("combat_stats")
        self.breakthrough_culculate_label.setText('%s' %breakthrough)
        self.breakthrough_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.breakthrough_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.armor_stats_label = QtWidgets.QLabel(Dialog)
        self.armor_stats_label.setGeometry(QtCore.QRect(720, 175, 100, 15))
        self.armor_stats_label.setObjectName("combat_stats")
        self.armor_stats_label.setText("Armor:")
        self.armor_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.armor_culculate_label = QtWidgets.QLabel(Dialog)
        self.armor_culculate_label.setGeometry(QtCore.QRect(785, 175, 100, 15))
        self.armor_culculate_label.setObjectName("combat_stats")
        self.armor_culculate_label.setText('%s' %armor)
        self.armor_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.armor_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.piercing_stats_label = QtWidgets.QLabel(Dialog)
        self.piercing_stats_label.setGeometry(QtCore.QRect(720, 195, 100, 15))
        self.piercing_stats_label.setObjectName("combat_stats")
        self.piercing_stats_label.setText("Piercing:")
        self.piercing_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.piercing_culculate_label = QtWidgets.QLabel(Dialog)
        self.piercing_culculate_label.setGeometry(QtCore.QRect(785, 195, 100, 15))
        self.piercing_culculate_label.setObjectName("combat_stats")
        self.piercing_culculate_label.setText('%s' %piercing)
        self.piercing_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.piercing_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.initiative_stats_label = QtWidgets.QLabel(Dialog)
        self.initiative_stats_label.setGeometry(QtCore.QRect(720, 215, 100, 15))
        self.initiative_stats_label.setObjectName("combat_stats")
        self.initiative_stats_label.setText("Initiative:")
        self.initiative_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.initiative_culculate_label = QtWidgets.QLabel(Dialog)
        self.initiative_culculate_label.setGeometry(QtCore.QRect(785, 215, 100, 15))
        self.initiative_culculate_label.setObjectName("combat_stats")
        self.initiative_culculate_label.setText('%s' %initiative)
        self.initiative_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.initiative_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.entrenchment_stats_label = QtWidgets.QLabel(Dialog)
        self.entrenchment_stats_label.setGeometry(QtCore.QRect(720, 235, 100, 15))
        self.entrenchment_stats_label.setObjectName("combat_stats")
        self.entrenchment_stats_label.setText("Entrenchment:")
        self.entrenchment_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.entrenchment_culculate_label = QtWidgets.QLabel(Dialog)
        self.entrenchment_culculate_label.setGeometry(QtCore.QRect(785, 235, 100, 15))
        self.entrenchment_culculate_label.setObjectName("combat_stats")
        self.entrenchment_culculate_label.setText('%s' %entrenchment)
        self.entrenchment_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.entrenchment_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.eq_capture_stats_label = QtWidgets.QLabel(Dialog)
        self.eq_capture_stats_label.setGeometry(QtCore.QRect(720, 255, 110, 15))
        self.eq_capture_stats_label.setObjectName("combat_stats")
        self.eq_capture_stats_label.setText("Eq. Capture Ratio:")
        self.eq_capture_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.eq_capture_culculate_label = QtWidgets.QLabel(Dialog)
        self.eq_capture_culculate_label.setGeometry(QtCore.QRect(785, 255, 100, 15))
        self.eq_capture_culculate_label.setObjectName("combat_stats")
        self.eq_capture_culculate_label.setText('%s' %eq_capture_ratio)
        self.eq_capture_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.eq_capture_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.combat_width_stats_label = QtWidgets.QLabel(Dialog)
        self.combat_width_stats_label.setGeometry(QtCore.QRect(720, 275, 100, 15))
        self.combat_width_stats_label.setObjectName("combat_stats")
        self.combat_width_stats_label.setText("Combat width:")
        self.combat_width_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.combat_width_culculate_label = QtWidgets.QLabel(Dialog)
        self.combat_width_culculate_label.setGeometry(QtCore.QRect(785, 275, 100, 15))
        self.combat_width_culculate_label.setObjectName("combat_stats")
        self.combat_width_culculate_label.setText('%s' %combat_width)
        self.combat_width_culculate_label.setFont(QtGui.QFont("Ariel", 10))
        self.combat_width_culculate_label.setAlignment(QtCore.Qt.AlignRight)

        self.equipment_cost_title_label = QtWidgets.QLabel(Dialog)
        self.equipment_cost_title_label.setGeometry(QtCore.QRect(900, 43, 250, 30))
        self.equipment_cost_title_label.setObjectName("equipment_TITLE")
        self.equipment_cost_title_label.setText("Equipment Cost")
        self.equipment_cost_title_label.setFont(QtGui.QFont("Ariel", 15))

        self.manpower_stats_label = QtWidgets.QLabel(Dialog)
        self.manpower_stats_label.setGeometry(QtCore.QRect(895, 75, 100, 15))
        self.manpower_stats_label.setObjectName("equipment_stats")
        self.manpower_stats_label.setText("Manpower:")
        self.manpower_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.manpower_culculated_stats_label = QtWidgets.QLabel(Dialog)
        self.manpower_culculated_stats_label.setGeometry(QtCore.QRect(955, 75, 100, 15))
        self.manpower_culculated_stats_label.setObjectName("combat_stats")
        self.manpower_culculated_stats_label.setText('%s' %manpower)
        self.manpower_culculated_stats_label.setFont(QtGui.QFont("Ariel", 10))
        self.manpower_culculated_stats_label.setAlignment(QtCore.Qt.AlignRight)

        self.training_time_stats_label = QtWidgets.QLabel(Dialog)
        self.training_time_stats_label.setGeometry(QtCore.QRect(895, 95, 100, 15))
        self.training_time_stats_label.setObjectName("equipment_stats")
        self.training_time_stats_label.setText("Training time:")
        self.training_time_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.training_time_culculated_stats_label = QtWidgets.QLabel(Dialog)
        self.training_time_culculated_stats_label.setGeometry(QtCore.QRect(955, 95, 100, 15))
        self.training_time_culculated_stats_label.setObjectName("combat_stats")
        self.training_time_culculated_stats_label.setText('%s' %training_time)
        self.training_time_culculated_stats_label.setFont(QtGui.QFont("Ariel", 10))
        self.training_time_culculated_stats_label.setAlignment(QtCore.Qt.AlignRight)

        self.fuel_usage_stats_label = QtWidgets.QLabel(Dialog)
        self.fuel_usage_stats_label.setGeometry(QtCore.QRect(895, 115, 100, 15))
        self.fuel_usage_stats_label.setObjectName("equipment_stats")
        self.fuel_usage_stats_label.setText("Fuel Usage:")
        self.fuel_usage_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.fuel_usage_culculated_stats_label = QtWidgets.QLabel(Dialog)
        self.fuel_usage_culculated_stats_label.setGeometry(QtCore.QRect(955, 115, 100, 15))
        self.fuel_usage_culculated_stats_label.setObjectName("combat_stats")
        self.fuel_usage_culculated_stats_label.setText('%s' %fuel_usage)
        self.fuel_usage_culculated_stats_label.setFont(QtGui.QFont("Ariel", 10))
        self.fuel_usage_culculated_stats_label.setAlignment(QtCore.Qt.AlignRight)

        self.amtracs_stats_label = QtWidgets.QLabel(Dialog)
        self.amtracs_stats_label.setGeometry(QtCore.QRect(895, 135, 100, 15))
        self.amtracs_stats_label.setObjectName("equipment_stats")
        self.amtracs_stats_label.setText("Amtracs:")
        self.amtracs_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.amtracs_culculated_stats_label = QtWidgets.QLabel(Dialog)
        self.amtracs_culculated_stats_label.setGeometry(QtCore.QRect(955, 135, 100, 15))
        self.amtracs_culculated_stats_label.setObjectName("combat_stats")
        self.amtracs_culculated_stats_label.setText('%s' %amtracs)
        self.amtracs_culculated_stats_label.setFont(QtGui.QFont("Ariel", 10))
        self.amtracs_culculated_stats_label.setAlignment(QtCore.Qt.AlignRight)

        self.infantry_eq_stats_label = QtWidgets.QLabel(Dialog)
        self.infantry_eq_stats_label.setGeometry(QtCore.QRect(895, 155, 100, 15))
        self.infantry_eq_stats_label.setObjectName("equipment_stats")
        self.infantry_eq_stats_label.setText("Infantry Eq.:")
        self.infantry_eq_stats_label.setFont(QtGui.QFont("Ariel", 10))

        self.infantry_eq_culculated_stats_label = QtWidgets.QLabel(Dialog)
        self.infantry_eq_culculated_stats_label.setGeometry(QtCore.QRect(955, 155, 100, 15))
        self.infantry_eq_culculated_stats_label.setObjectName("combat_stats")
        self.infantry_eq_culculated_stats_label.setText('%s' %infantry_eq)
        self.infantry_eq_culculated_stats_label.setFont(QtGui.QFont("Ariel", 10))
        self.infantry_eq_culculated_stats_label.setAlignment(QtCore.Qt.AlignRight)

        self.texedit = QtWidgets.QTextEdit(Dialog)
        self.texedit.setGeometry(QtCore.QRect(195, 115, 150, 25))
        self.texedit.setText("Infantry Division")
        self.texedit.setFont(QtGui.QFont("Ariel", 10))
        self.texedit.setStyleSheet("Color : white;" "background-color: #10120D")
        
        self.companies_label_1 = QtWidgets.QLabel(Dialog)
        self.companies_label_1.setGeometry(QtCore.QRect(24, 202, 100, 100))
        self.companies_label_1.setPixmap(QtGui.QPixmap("ui/div_subunit_item_bg.png"))
        self.companies_label_1.setObjectName("label")

        self.companies_label_2 = QtWidgets.QLabel(Dialog)
        self.companies_label_2.setGeometry(QtCore.QRect(24, 252, 100, 100))
        self.companies_label_2.setPixmap(QtGui.QPixmap("ui/div_subunit_item_bg.png"))
        self.companies_label_2.setObjectName("label")

        self.companies_label_3 = QtWidgets.QLabel(Dialog)
        self.companies_label_3.setGeometry(QtCore.QRect(24, 302, 100, 100))
        self.companies_label_3.setPixmap(QtGui.QPixmap("ui/div_subunit_item_bg.png"))
        self.companies_label_3.setObjectName("label")

        self.companies_label_4 = QtWidgets.QLabel(Dialog)
        self.companies_label_4.setGeometry(QtCore.QRect(24, 352, 100, 100))
        self.companies_label_4.setPixmap(QtGui.QPixmap("ui/div_subunit_item_bg.png"))
        self.companies_label_4.setObjectName("label")

        self.companies_label_5 = QtWidgets.QLabel(Dialog)
        self.companies_label_5.setGeometry(QtCore.QRect(24, 402, 100, 100))
        self.companies_label_5.setPixmap(QtGui.QPixmap("ui/div_subunit_item_bg.png"))
        self.companies_label_5.setObjectName("label")
        
        self.companies_button_1 = QtWidgets.QPushButton(Dialog)
        self.companies_button_1.setGeometry(QtCore.QRect(27, 250, 58, 26))
        self.companies_button_1.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.companies_button_1.setObjectName("Button")
        self.companies_button_1.clicked.connect( lambda state, button=self.companies_button_1 : self.change_1_icon_companies(state, button))
        
        self.companies_button_2 = QtWidgets.QPushButton(Dialog)
        self.companies_button_2.setGeometry(QtCore.QRect(27, 300, 58, 26))
        self.companies_button_2.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.companies_button_2.setObjectName("Button")
        self.companies_button_2.clicked.connect( lambda state, button=self.companies_button_2 : self.change_2_icon_companies(state, button))
        
        self.companies_button_3 = QtWidgets.QPushButton(Dialog)
        self.companies_button_3.setGeometry(QtCore.QRect(27, 350, 58, 26))
        self.companies_button_3.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.companies_button_3.setObjectName("Button")
        self.companies_button_3.clicked.connect( lambda state, button=self.companies_button_3 : self.change_3_icon_companies(state, button))

        self.companies_button_4 = QtWidgets.QPushButton(Dialog)
        self.companies_button_4.setGeometry(QtCore.QRect(27, 400, 58, 26))
        self.companies_button_4.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.companies_button_4.setObjectName("Button")
        self.companies_button_4.clicked.connect( lambda state, button=self.companies_button_4 : self.change_4_icon_companies(state, button))
        
        self.companies_button_5 = QtWidgets.QPushButton(Dialog)
        self.companies_button_5.setGeometry(QtCore.QRect(27, 450, 58, 26))
        self.companies_button_5.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.companies_button_5.setObjectName("Button")
        self.companies_button_5.clicked.connect( lambda state, button=self.companies_button_5 : self.change_5_icon_companies(state, button))

        self.battalion_label_1 = QtWidgets.QLabel(Dialog)
        self.battalion_label_1.setGeometry(QtCore.QRect(114, 202, 100, 100))
        self.battalion_label_1.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_1.setObjectName("label")

        self.battalion_label_2 = QtWidgets.QLabel(Dialog)
        self.battalion_label_2.setGeometry(QtCore.QRect(114, 252, 100, 100))
        self.battalion_label_2.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_2.setObjectName("label")

        self.battalion_label_3 = QtWidgets.QLabel(Dialog)
        self.battalion_label_3.setGeometry(QtCore.QRect(114, 302, 100, 100))
        self.battalion_label_3.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_3.setObjectName("label")

        self.battalion_label_4 = QtWidgets.QLabel(Dialog)
        self.battalion_label_4.setGeometry(QtCore.QRect(114, 352, 100, 100))
        self.battalion_label_4.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_4.setObjectName("label")

        self.battalion_label_5 = QtWidgets.QLabel(Dialog)
        self.battalion_label_5.setGeometry(QtCore.QRect(114, 402, 100, 100))
        self.battalion_label_5.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_5.setObjectName("label")
        
        self.battalion_button_1 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_1.setGeometry(QtCore.QRect(118, 240, 68, 36))
        self.battalion_button_1.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_1.setObjectName("Button")
        self.battalion_button_1.clicked.connect( lambda state, button=self.battalion_button_1 : self.change_1_icon_battalion(state, button))
        
        self.battalion_button_2 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_2.setGeometry(QtCore.QRect(118, 290, 68, 36))
        self.battalion_button_2.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_2.setObjectName("Button")
        self.battalion_button_2.clicked.connect( lambda state, button=self.battalion_button_2 : self.change_2_icon_battalion(state, button))
        
        self.battalion_button_3 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_3.setGeometry(QtCore.QRect(118, 340, 68, 36))
        self.battalion_button_3.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_3.setObjectName("Button")
        self.battalion_button_3.clicked.connect( lambda state, button=self.battalion_button_3 : self.change_3_icon_battalion(state, button))
        
        self.battalion_button_4 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_4.setGeometry(QtCore.QRect(118, 390, 68, 36))
        self.battalion_button_4.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_4.setObjectName("Button")
        self.battalion_button_4.clicked.connect( lambda state, button=self.battalion_button_4 : self.change_4_icon_battalion(state, button))
        
        self.battalion_button_5 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_5.setGeometry(QtCore.QRect(118, 440, 68, 36))
        self.battalion_button_5.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_5.setObjectName("Button")
        self.battalion_button_5.clicked.connect( lambda state, button=self.battalion_button_5 : self.change_5_icon_battalion(state, button))

        self.battalion_label_11 = QtWidgets.QLabel(Dialog)
        self.battalion_label_11.setGeometry(QtCore.QRect(194, 202, 100, 100))
        self.battalion_label_11.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_11.setObjectName("label")
        
        self.battalion_label_12 = QtWidgets.QLabel(Dialog)
        self.battalion_label_12.setGeometry(QtCore.QRect(194, 252, 100, 100))
        self.battalion_label_12.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_12.setObjectName("label")

        self.battalion_label_13 = QtWidgets.QLabel(Dialog)
        self.battalion_label_13.setGeometry(QtCore.QRect(194, 302, 100, 100))
        self.battalion_label_13.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_13.setObjectName("label")

        self.battalion_label_14 = QtWidgets.QLabel(Dialog)
        self.battalion_label_14.setGeometry(QtCore.QRect(194, 352, 100, 100))
        self.battalion_label_14.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_14.setObjectName("label")

        self.battalion_label_15 = QtWidgets.QLabel(Dialog)
        self.battalion_label_15.setGeometry(QtCore.QRect(194, 402, 100, 100))
        self.battalion_label_15.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_15.setObjectName("label")
        
        self.battalion_button_11 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_11.setGeometry(QtCore.QRect(198, 240, 68, 36))
        self.battalion_button_11.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_11.setObjectName("Button")
        self.battalion_button_11.clicked.connect( lambda state, button=self.battalion_button_11 : self.change_11_icon_battalion(state, button))
        
        self.battalion_button_12 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_12.setGeometry(QtCore.QRect(198, 290, 68, 36))
        self.battalion_button_12.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_12.setObjectName("Button")
        self.battalion_button_12.clicked.connect( lambda state, button=self.battalion_button_12 : self.change_12_icon_battalion(state, button))
        
        self.battalion_button_13 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_13.setGeometry(QtCore.QRect(198, 340, 68, 36))
        self.battalion_button_13.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_13.setObjectName("Button")
        self.battalion_button_13.clicked.connect( lambda state, button=self.battalion_button_13 : self.change_13_icon_battalion(state, button))
        
        self.battalion_button_14 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_14.setGeometry(QtCore.QRect(198, 390, 68, 36))
        self.battalion_button_14.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_14.setObjectName("Button")
        self.battalion_button_14.clicked.connect( lambda state, button=self.battalion_button_14 : self.change_14_icon_battalion(state, button))
        
        self.battalion_button_15 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_15.setGeometry(QtCore.QRect(198, 440, 68, 36))
        self.battalion_button_15.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_15.setObjectName("Button")
        self.battalion_button_15.clicked.connect( lambda state, button=self.battalion_button_15 : self.change_15_icon_battalion(state, button))

        self.battalion_label_21 = QtWidgets.QLabel(Dialog)
        self.battalion_label_21.setGeometry(QtCore.QRect(274, 202, 100, 100))
        self.battalion_label_21.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_21.setObjectName("label")

        self.battalion_label_22 = QtWidgets.QLabel(Dialog)
        self.battalion_label_22.setGeometry(QtCore.QRect(274, 252, 100, 100))
        self.battalion_label_22.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_22.setObjectName("label")

        self.battalion_label_23 = QtWidgets.QLabel(Dialog)
        self.battalion_label_23.setGeometry(QtCore.QRect(274, 302, 100, 100))
        self.battalion_label_23.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_23.setObjectName("label")

        self.battalion_label_24 = QtWidgets.QLabel(Dialog)
        self.battalion_label_24.setGeometry(QtCore.QRect(274, 352, 100, 100))
        self.battalion_label_24.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_24.setObjectName("label")

        self.battalion_label_25 = QtWidgets.QLabel(Dialog)
        self.battalion_label_25.setGeometry(QtCore.QRect(274, 402, 100, 100))
        self.battalion_label_25.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_25.setObjectName("label")
        
        self.battalion_button_21 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_21.setGeometry(QtCore.QRect(278, 240, 68, 36))
        self.battalion_button_21.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_21.setObjectName("Button")
        self.battalion_button_21.clicked.connect( lambda state, button=self.battalion_button_21 : self.change_21_icon_battalion(state, button))
        
        self.battalion_button_22 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_22.setGeometry(QtCore.QRect(278, 290, 68, 36))
        self.battalion_button_22.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_22.setObjectName("Button")
        self.battalion_button_22.clicked.connect( lambda state, button=self.battalion_button_22 : self.change_22_icon_battalion(state, button))
        
        self.battalion_button_23 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_23.setGeometry(QtCore.QRect(278, 340, 68, 36))
        self.battalion_button_23.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_23.setObjectName("Button")
        self.battalion_button_23.clicked.connect( lambda state, button=self.battalion_button_23 : self.change_23_icon_battalion(state, button))
        
        self.battalion_button_24 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_24.setGeometry(QtCore.QRect(278, 390, 68, 36))
        self.battalion_button_24.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_24.setObjectName("Button")
        self.battalion_button_24.clicked.connect( lambda state, button=self.battalion_button_24 : self.change_24_icon_battalion(state, button))
        
        self.battalion_button_25 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_25.setGeometry(QtCore.QRect(278, 440, 68, 36))
        self.battalion_button_25.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_25.setObjectName("Button")
        self.battalion_button_25.clicked.connect( lambda state, button=self.battalion_button_25 : self.change_25_icon_battalion(state, button))

        self.battalion_label_31 = QtWidgets.QLabel(Dialog)
        self.battalion_label_31.setGeometry(QtCore.QRect(354, 202, 100, 100))
        self.battalion_label_31.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_31.setObjectName("label")

        self.battalion_label_32 = QtWidgets.QLabel(Dialog)
        self.battalion_label_32.setGeometry(QtCore.QRect(354, 252, 100, 100))
        self.battalion_label_32.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_32.setObjectName("label")

        self.battalion_label_33 = QtWidgets.QLabel(Dialog)
        self.battalion_label_33.setGeometry(QtCore.QRect(354, 302, 100, 100))
        self.battalion_label_33.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_33.setObjectName("label")

        self.battalion_label_34 = QtWidgets.QLabel(Dialog)
        self.battalion_label_34.setGeometry(QtCore.QRect(354, 352, 100, 100))
        self.battalion_label_34.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_34.setObjectName("label")

        self.battalion_label_35 = QtWidgets.QLabel(Dialog)
        self.battalion_label_35.setGeometry(QtCore.QRect(354, 402, 100, 100))
        self.battalion_label_35.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_35.setObjectName("label")

        self.battalion_button_31 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_31.setGeometry(QtCore.QRect(358, 240, 68, 36))
        self.battalion_button_31.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_31.setObjectName("Button")
        self.battalion_button_31.clicked.connect( lambda state, button=self.battalion_button_31 : self.change_31_icon_battalion(state, button))
        
        self.battalion_button_32 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_32.setGeometry(QtCore.QRect(358, 290, 68, 36))
        self.battalion_button_32.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_32.setObjectName("Button")
        self.battalion_button_32.clicked.connect( lambda state, button=self.battalion_button_32 : self.change_32_icon_battalion(state, button))
        
        self.battalion_button_33 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_33.setGeometry(QtCore.QRect(358, 340, 68, 36))
        self.battalion_button_33.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_33.setObjectName("Button")
        self.battalion_button_33.clicked.connect( lambda state, button=self.battalion_button_33 : self.change_33_icon_battalion(state, button))
        
        self.battalion_button_34 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_34.setGeometry(QtCore.QRect(358, 390, 68, 36))
        self.battalion_button_34.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_34.setObjectName("Button")
        self.battalion_button_34.clicked.connect( lambda state, button=self.battalion_button_34 : self.change_34_icon_battalion(state, button))
        
        self.battalion_button_35 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_35.setGeometry(QtCore.QRect(358, 440, 68, 36))
        self.battalion_button_35.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_35.setObjectName("Button")
        self.battalion_button_35.clicked.connect( lambda state, button=self.battalion_button_35 : self.change_35_icon_battalion(state, button))

        self.battalion_label_41 = QtWidgets.QLabel(Dialog)
        self.battalion_label_41.setGeometry(QtCore.QRect(434, 202, 100, 100))
        self.battalion_label_41.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_41.setObjectName("label")

        self.battalion_label_42 = QtWidgets.QLabel(Dialog)
        self.battalion_label_42.setGeometry(QtCore.QRect(434, 252, 100, 100))
        self.battalion_label_42.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_42.setObjectName("label")

        self.battalion_label_43 = QtWidgets.QLabel(Dialog)
        self.battalion_label_43.setGeometry(QtCore.QRect(434, 302, 100, 100))
        self.battalion_label_43.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_43.setObjectName("label")

        self.battalion_label_44 = QtWidgets.QLabel(Dialog)
        self.battalion_label_44.setGeometry(QtCore.QRect(434, 352, 100, 100))
        self.battalion_label_44.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_44.setObjectName("label")

        self.battalion_label_45 = QtWidgets.QLabel(Dialog)
        self.battalion_label_45.setGeometry(QtCore.QRect(434, 402, 100, 100))
        self.battalion_label_45.setPixmap(QtGui.QPixmap("ui/div_unit_item_bg.png"))
        self.battalion_label_45.setObjectName("label")
        
        self.battalion_button_41 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_41.setGeometry(QtCore.QRect(438, 240, 68, 36))
        self.battalion_button_41.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_41.setObjectName("Button")
        self.battalion_button_41.clicked.connect( lambda state, button=self.battalion_button_41 : self.change_41_icon_battalion(state, button))

        self.battalion_button_42 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_42.setGeometry(QtCore.QRect(438, 290, 68, 36))
        self.battalion_button_42.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_42.setObjectName("Button")
        self.battalion_button_42.clicked.connect( lambda state, button=self.battalion_button_42 : self.change_42_icon_battalion(state, button))
        
        self.battalion_button_43 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_43.setGeometry(QtCore.QRect(438, 340, 68, 36))
        self.battalion_button_43.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_43.setObjectName("Button")
        self.battalion_button_43.clicked.connect( lambda state, button=self.battalion_button_43 : self.change_43_icon_battalion(state, button))
        
        self.battalion_button_44 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_44.setGeometry(QtCore.QRect(438, 390, 68, 36))
        self.battalion_button_44.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_44.setObjectName("Button")
        self.battalion_button_44.clicked.connect( lambda state, button=self.battalion_button_44 : self.change_44_icon_battalion(state, button))
        
        self.battalion_button_45 = QtWidgets.QPushButton(Dialog)
        self.battalion_button_45.setGeometry(QtCore.QRect(438, 440, 68, 36))
        self.battalion_button_45.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
        self.battalion_button_45.setObjectName("Button")
        self.battalion_button_45.clicked.connect( lambda state, button=self.battalion_button_45 : self.change_45_icon_battalion(state, button))
        
        self.priority_button = QtWidgets.QPushButton(Dialog)
        self.priority_button.setGeometry(QtCore.QRect(395, 107, 127, 44))
        self.priority_button.setStyleSheet("image:url(ui/priority_3.png);" "background-color: #1B1A19")
        self.priority_button.setObjectName("Button")
        self.priority_button.clicked.connect( lambda state, button=self.priority_button : self.change_priority(state, button))
        
        self.reset_button = QtWidgets.QPushButton(Dialog)
        self.reset_button.setGeometry(QtCore.QRect(20, 503, 123, 36))
        self.reset_button.setStyleSheet("image:url(ui/button_reset_123x34.png);" "Color : white;" "background-color: #292825;" "border-style: dashed;" "border-width: 0px;")
        self.reset_button.setText("baka button")
        self.reset_button.setFont(QtGui.QFont("Ariel", 10))
        self.reset_button.setObjectName("Button")
        self.reset_button.clicked.connect( lambda state, button=self.reset_button : self.reset_all(state, button))
        
        self.save_button = QtWidgets.QPushButton(Dialog)
        self.save_button.setGeometry(QtCore.QRect(400, 503, 123, 36))
        self.save_button.setStyleSheet("image:url(ui/button_reset_123x34.png);" "Color : white;" "background-color: #292825;" "border-style: dashed;" "border-width: 0px;")
        self.save_button.setText("Save")
        self.save_button.setFont(QtGui.QFont("Ariel", 10))
        self.save_button.setObjectName("Button")
        self.save_button.clicked.connect( lambda state, button=self.save_button : self.savecommand(state, button))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def culculate_stats(self):
        global company_1_current_icon
        global max_speed
        global hp
        global organization
        global recovery_rate
        global reconnaissance
        global suppression
        global weight
        global supply_use
        global reliability
        global tricleback
        global exp_loss

        global soft_attack
        global hard_attack
        global air_attack
        global defence
        global breakthrough
        global armor
        global piercing
        global initiative
        global entrenchment
        global eq_capture_ratio
        global combat_width

        global manpower
        global training_time
        global fuel_capacity
        global fuel_usage
        global amtracs
        global infantry_eq

        if company_1_current_icon or company_2_current_icon or company_3_current_icon or company_4_current_icon or company_5_current_icon == 2:
            training_time = 120
            hp += 20
            manpower += 300
            weight += 10
            defence += -0.4
            soft_attack += -0.4
            hard_attack += -0.4
            air_attack += -0.2

        self.max_speed_culculate_label.setText('%.1f km/h' %max_speed)
        self.hp_culculate_label.setText('%.1f' %hp)
        self.org_culculate_label.setText('%.1f' %organization)
        self.recovery_culculate_label.setText('%.2f' %recovery_rate)
        self.reconnaissance_culculate_label.setText('%.1f' %reconnaissance)
        self.suppression_culculate_label.setText('%.1f' %suppression)
        self.weight_culculate_label.setText('%.1f' %weight)
        self.supply_use_culculate_label.setText('%.2f' %supply_use)
        self.reliability_culculate_label.setText('%.2f' %reliability)
        self.trickleback_culculate_label.setText('%.2f' %tricleback)
        self.exp_loss_culculate_label.setText('%.2f' %exp_loss)
        self.soft_attack_culculate_label.setText('%.1f' %soft_attack)
        self.hard_attack_culculate_label.setText('%.1f' %hard_attack)
        self.air_attack_culculate_label.setText('%.1f' %air_attack)
        self.defense_culculate_label.setText('%.1f' %defence)
        self.breakthrough_culculate_label.setText('%.1f' %breakthrough)
        self.armor_culculate_label.setText('%.1f' %armor)
        self.piercing_culculate_label.setText('%.1f' %piercing)
        self.initiative_culculate_label.setText('%.2f' %initiative)
        self.entrenchment_culculate_label.setText('%.1f' %entrenchment)
        self.eq_capture_culculate_label.setText('%.0f' %eq_capture_ratio)
        self.combat_width_culculate_label.setText('%.1f' %combat_width)
        self.manpower_culculated_stats_label.setText('%.0f' %manpower)
        self.training_time_culculated_stats_label.setText('%.0f' %training_time)
        self.fuel_usage_culculated_stats_label.setText('%.1f' %fuel_usage)
        self.amtracs_culculated_stats_label.setText('%.0f' %amtracs)
        self.infantry_eq_culculated_stats_label.setText('%.0f' %infantry_eq)

    def change_priority(self, state, button):
        global priority
        playsound("sound/click_checkbox.wav")
        if priority == 1:
            button.setStyleSheet("image:url(ui/priority_4.png);" "background-color: #1B1A19")
            priority = 2
        elif priority == 2:
            button.setStyleSheet("image:url(ui/priority_2.png);" "background-color: #1B1A19")
            priority = 3
        elif priority == 3:
            button.setStyleSheet("image:url(ui/priority_3.png);" "background-color: #1B1A19")
            priority = 1

    def change_1_icon_companies(self, state, button):
        global company_1_current_icon
        global max_speed
        global hp
        global organization
        global recovery_rate
        global reconnaissance
        global suppression
        global weight
        global supply_use
        global reliability
        global tricleback
        global exp_loss

        global soft_attack
        global hard_attack
        global air_attack
        global defence
        global breakthrough
        global armor
        global piercing
        global initiative
        global entrenchment
        global eq_capture_ratio
        global combat_width

        global manpower
        global training_time
        global fuel_capacity
        global fuel_usage
        global amtracs
        global infantry_eq

        playsound("sound/click_checkbox.wav")
        if company_1_current_icon == 1:
            button.setStyleSheet("image:url(company/support_unit_anti_air_icon.png);" "background-color: #10120D")
            company_1_current_icon = 2

        elif company_1_current_icon == 2:
            button.setStyleSheet("image:url(company/support_unit_armored_car_recon_icon.png);" "background-color: #10120D")
            company_1_current_icon = 3
        
        elif company_1_current_icon == 3:
            button.setStyleSheet("image:url(company/support_unit_armored_recon_icon.png);" "background-color: #10120D")
            company_1_current_icon = 4
        
        elif company_1_current_icon == 4:
            button.setStyleSheet("image:url(company/support_unit_art_icon.png);" "background-color: #10120D")
            company_1_current_icon = 5
        
        elif company_1_current_icon == 5:
            button.setStyleSheet("image:url(company/support_unit_at_icon.png);" "background-color: #10120D")
            company_1_current_icon = 6
        
        elif company_1_current_icon == 6:
            button.setStyleSheet("image:url(company/support_unit_field_hospital_icon.png);" "background-color: #10120D")
            company_1_current_icon = 7
        
        elif company_1_current_icon == 7:
            button.setStyleSheet("image:url(company/support_unit_logistics_company_icon.png);" "background-color: #10120D")
            company_1_current_icon = 8
        
        elif company_1_current_icon == 8:
            button.setStyleSheet("image:url(company/support_unit_maintenance_company_icon.png);" "background-color: #10120D")
            company_1_current_icon = 9
        
        elif company_1_current_icon == 9:
            button.setStyleSheet("image:url(company/support_unit_military_police_icon.png);" "background-color: #10120D")
            company_1_current_icon = 10
        
        elif company_1_current_icon == 10:
            button.setStyleSheet("image:url(company/support_unit_motorized_recon_icon.png);" "background-color: #10120D")
            company_1_current_icon = 11
        
        elif company_1_current_icon == 11:
            button.setStyleSheet("image:url(company/support_unit_rocket_art_icon.png);" "background-color: #10120D")
            company_1_current_icon = 12
        
        elif company_1_current_icon == 12:
            button.setStyleSheet("image:url(company/support_unit_signal_company_icon.png);" "background-color: #10120D")
            company_1_current_icon = 13
        
        elif company_1_current_icon == 13:
            button.setStyleSheet("image:url(company/unit_engineer_icon.png);" "background-color: #10120D")
            company_1_current_icon = 14
        
        elif company_1_current_icon == 14:
            button.setStyleSheet("image:url(company/unit_recon_icon.png);" "background-color: #10120D")
            company_1_current_icon = 0
        
        elif company_1_current_icon == 0:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            company_1_current_icon = 1   

        self.culculate_stats()

    def change_2_icon_companies(self, state, button):
        global company_2_current_icon

        playsound("sound/click_checkbox.wav")
        if company_2_current_icon == 1:
            button.setStyleSheet("image:url(company/support_unit_anti_air_icon.png);" "background-color: #10120D")
            company_2_current_icon = 2

        elif company_2_current_icon == 2:
            button.setStyleSheet("image:url(company/support_unit_armored_car_recon_icon.png);" "background-color: #10120D")
            company_2_current_icon = 3
        
        elif company_2_current_icon == 3:
            button.setStyleSheet("image:url(company/support_unit_armored_recon_icon.png);" "background-color: #10120D")
            company_2_current_icon = 4
        
        elif company_2_current_icon == 4:
            button.setStyleSheet("image:url(company/support_unit_art_icon.png);" "background-color: #10120D")
            company_2_current_icon = 5
        
        elif company_2_current_icon == 5:
            button.setStyleSheet("image:url(company/support_unit_at_icon.png);" "background-color: #10120D")
            company_2_current_icon = 6
        
        elif company_2_current_icon == 6:
            button.setStyleSheet("image:url(company/support_unit_field_hospital_icon.png);" "background-color: #10120D")
            company_2_current_icon = 7
        
        elif company_2_current_icon == 7:
            button.setStyleSheet("image:url(company/support_unit_logistics_company_icon.png);" "background-color: #10120D")
            company_2_current_icon = 8
        
        elif company_2_current_icon == 8:
            button.setStyleSheet("image:url(company/support_unit_maintenance_company_icon.png);" "background-color: #10120D")
            company_2_current_icon = 9
        
        elif company_2_current_icon == 9:
            button.setStyleSheet("image:url(company/support_unit_military_police_icon.png);" "background-color: #10120D")
            company_2_current_icon = 10
        
        elif company_2_current_icon == 10:
            button.setStyleSheet("image:url(company/support_unit_motorized_recon_icon.png);" "background-color: #10120D")
            company_2_current_icon = 11
        
        elif company_2_current_icon == 11:
            button.setStyleSheet("image:url(company/support_unit_rocket_art_icon.png);" "background-color: #10120D")
            company_2_current_icon = 12
        
        elif company_2_current_icon == 12:
            button.setStyleSheet("image:url(company/support_unit_signal_company_icon.png);" "background-color: #10120D")
            company_2_current_icon = 13
        
        elif company_2_current_icon == 13:
            button.setStyleSheet("image:url(company/unit_engineer_icon.png);" "background-color: #10120D")
            company_2_current_icon = 14
        
        elif company_2_current_icon == 14:
            button.setStyleSheet("image:url(company/unit_recon_icon.png);" "background-color: #10120D")
            company_2_current_icon = 0
        
        elif company_2_current_icon == 0:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            company_2_current_icon = 1

        self.culculate_stats()

    def change_3_icon_companies(self, state, button):
        global company_3_current_icon

        playsound("sound/click_checkbox.wav")
        if company_3_current_icon == 1:
            button.setStyleSheet("image:url(company/support_unit_anti_air_icon.png);" "background-color: #10120D")
            company_3_current_icon = 2

        elif company_3_current_icon == 2:
            button.setStyleSheet("image:url(company/support_unit_armored_car_recon_icon.png);" "background-color: #10120D")
            company_3_current_icon = 3
        
        elif company_3_current_icon == 3:
            button.setStyleSheet("image:url(company/support_unit_armored_recon_icon.png);" "background-color: #10120D")
            company_3_current_icon = 4
        
        elif company_3_current_icon == 4:
            button.setStyleSheet("image:url(company/support_unit_art_icon.png);" "background-color: #10120D")
            company_3_current_icon = 5
        
        elif company_3_current_icon == 5:
            button.setStyleSheet("image:url(company/support_unit_at_icon.png);" "background-color: #10120D")
            company_3_current_icon = 6
        
        elif company_3_current_icon == 6:
            button.setStyleSheet("image:url(company/support_unit_field_hospital_icon.png);" "background-color: #10120D")
            company_3_current_icon = 7
        
        elif company_3_current_icon == 7:
            button.setStyleSheet("image:url(company/support_unit_logistics_company_icon.png);" "background-color: #10120D")
            company_3_current_icon = 8
        
        elif company_3_current_icon == 8:
            button.setStyleSheet("image:url(company/support_unit_maintenance_company_icon.png);" "background-color: #10120D")
            company_3_current_icon = 9
        
        elif company_3_current_icon == 9:
            button.setStyleSheet("image:url(company/support_unit_military_police_icon.png);" "background-color: #10120D")
            company_3_current_icon = 10
        
        elif company_3_current_icon == 10:
            button.setStyleSheet("image:url(company/support_unit_motorized_recon_icon.png);" "background-color: #10120D")
            company_3_current_icon = 11
        
        elif company_3_current_icon == 11:
            button.setStyleSheet("image:url(company/support_unit_rocket_art_icon.png);" "background-color: #10120D")
            company_3_current_icon = 12
        
        elif company_3_current_icon == 12:
            button.setStyleSheet("image:url(company/support_unit_signal_company_icon.png);" "background-color: #10120D")
            company_3_current_icon = 13
        
        elif company_3_current_icon == 13:
            button.setStyleSheet("image:url(company/unit_engineer_icon.png);" "background-color: #10120D")
            company_3_current_icon = 14
        
        elif company_3_current_icon == 14:
            button.setStyleSheet("image:url(company/unit_recon_icon.png);" "background-color: #10120D")
            company_3_current_icon = 0
        
        elif company_3_current_icon == 0:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            company_3_current_icon = 1
            
        self.culculate_stats()

    def change_4_icon_companies(self, state, button):
        global company_4_current_icon

        playsound("sound/click_checkbox.wav")
        if company_4_current_icon == 1:
            button.setStyleSheet("image:url(company/support_unit_anti_air_icon.png);" "background-color: #10120D")
            company_4_current_icon = 2

        elif company_4_current_icon == 2:
            button.setStyleSheet("image:url(company/support_unit_armored_car_recon_icon.png);" "background-color: #10120D")
            company_4_current_icon = 3
        
        elif company_4_current_icon == 3:
            button.setStyleSheet("image:url(company/support_unit_armored_recon_icon.png);" "background-color: #10120D")
            company_4_current_icon = 4
        
        elif company_4_current_icon == 4:
            button.setStyleSheet("image:url(company/support_unit_art_icon.png);" "background-color: #10120D")
            company_4_current_icon = 5
        
        elif company_4_current_icon == 5:
            button.setStyleSheet("image:url(company/support_unit_at_icon.png);" "background-color: #10120D")
            company_4_current_icon = 6
        
        elif company_4_current_icon == 6:
            button.setStyleSheet("image:url(company/support_unit_field_hospital_icon.png);" "background-color: #10120D")
            company_4_current_icon = 7
        
        elif company_4_current_icon == 7:
            button.setStyleSheet("image:url(company/support_unit_logistics_company_icon.png);" "background-color: #10120D")
            company_4_current_icon = 8
        
        elif company_4_current_icon == 8:
            button.setStyleSheet("image:url(company/support_unit_maintenance_company_icon.png);" "background-color: #10120D")
            company_4_current_icon = 9
        
        elif company_4_current_icon == 9:
            button.setStyleSheet("image:url(company/support_unit_military_police_icon.png);" "background-color: #10120D")
            company_4_current_icon = 10
        
        elif company_4_current_icon == 10:
            button.setStyleSheet("image:url(company/support_unit_motorized_recon_icon.png);" "background-color: #10120D")
            company_4_current_icon = 11
        
        elif company_4_current_icon == 11:
            button.setStyleSheet("image:url(company/support_unit_rocket_art_icon.png);" "background-color: #10120D")
            company_4_current_icon = 12
        
        elif company_4_current_icon == 12:
            button.setStyleSheet("image:url(company/support_unit_signal_company_icon.png);" "background-color: #10120D")
            company_4_current_icon = 13
        
        elif company_4_current_icon == 13:
            button.setStyleSheet("image:url(company/unit_engineer_icon.png);" "background-color: #10120D")
            company_4_current_icon = 14
        
        elif company_4_current_icon == 14:
            button.setStyleSheet("image:url(company/unit_recon_icon.png);" "background-color: #10120D")
            company_4_current_icon = 0
        
        elif company_4_current_icon == 0:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            company_4_current_icon = 1
            
        self.culculate_stats()

    def change_5_icon_companies(self, state, button):
        global company_5_current_icon

        playsound("sound/click_checkbox.wav")
        if company_5_current_icon == 1:
            button.setStyleSheet("image:url(company/support_unit_anti_air_icon.png);" "background-color: #10120D")
            company_5_current_icon = 2

        elif company_5_current_icon == 2:
            button.setStyleSheet("image:url(company/support_unit_armored_car_recon_icon.png);" "background-color: #10120D")
            company_5_current_icon = 3
        
        elif company_5_current_icon == 3:
            button.setStyleSheet("image:url(company/support_unit_armored_recon_icon.png);" "background-color: #10120D")
            company_5_current_icon = 4
        
        elif company_5_current_icon == 4:
            button.setStyleSheet("image:url(company/support_unit_art_icon.png);" "background-color: #10120D")
            company_5_current_icon = 5
        
        elif company_5_current_icon == 5:
            button.setStyleSheet("image:url(company/support_unit_at_icon.png);" "background-color: #10120D")
            company_5_current_icon = 6
        
        elif company_5_current_icon == 6:
            button.setStyleSheet("image:url(company/support_unit_field_hospital_icon.png);" "background-color: #10120D")
            company_5_current_icon = 7
        
        elif company_5_current_icon == 7:
            button.setStyleSheet("image:url(company/support_unit_logistics_company_icon.png);" "background-color: #10120D")
            company_5_current_icon = 8
        
        elif company_5_current_icon == 8:
            button.setStyleSheet("image:url(company/support_unit_maintenance_company_icon.png);" "background-color: #10120D")
            company_5_current_icon = 9
        
        elif company_5_current_icon == 9:
            button.setStyleSheet("image:url(company/support_unit_military_police_icon.png);" "background-color: #10120D")
            company_5_current_icon = 10
        
        elif company_5_current_icon == 10:
            button.setStyleSheet("image:url(company/support_unit_motorized_recon_icon.png);" "background-color: #10120D")
            company_5_current_icon = 11
        
        elif company_5_current_icon == 11:
            button.setStyleSheet("image:url(company/support_unit_rocket_art_icon.png);" "background-color: #10120D")
            company_5_current_icon = 12
        
        elif company_5_current_icon == 12:
            button.setStyleSheet("image:url(company/support_unit_signal_company_icon.png);" "background-color: #10120D")
            company_5_current_icon = 13
        
        elif company_5_current_icon == 13:
            button.setStyleSheet("image:url(company/unit_engineer_icon.png);" "background-color: #10120D")
            company_5_current_icon = 14
        
        elif company_5_current_icon == 14:
            button.setStyleSheet("image:url(company/unit_recon_icon.png);" "background-color: #10120D")
            company_5_current_icon = 0
        
        elif company_5_current_icon == 0:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            company_5_current_icon = 1
            
        self.culculate_stats()

    def change_1_icon_battalion(self, state, button):
        global battalion_1_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_1_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 2

        elif battalion_1_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 3

        elif battalion_1_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 4

        elif battalion_1_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 5

        elif battalion_1_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 6

        elif battalion_1_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 7

        elif battalion_1_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 8

        elif battalion_1_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 9

        elif battalion_1_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 10

        elif battalion_1_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 11

        elif battalion_1_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 12

        elif battalion_1_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 13

        elif battalion_1_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 14

        elif battalion_1_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 15

        elif battalion_1_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 16

        elif battalion_1_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 17

        elif battalion_1_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 18

        elif battalion_1_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 19

        elif battalion_1_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 20

        elif battalion_1_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 21

        elif battalion_1_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 22

        elif battalion_1_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 23

        elif battalion_1_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 24

        elif battalion_1_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 25

        elif battalion_1_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 26

        elif battalion_1_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 27

        elif battalion_1_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 28

        elif battalion_1_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 29

        elif battalion_1_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 30

        elif battalion_1_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 31

        elif battalion_1_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 32

        elif battalion_1_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 33

        elif battalion_1_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 34

        elif battalion_1_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 35

        elif battalion_1_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 36

        elif battalion_1_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 37

        elif battalion_1_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 38

        elif battalion_1_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 39

        elif battalion_1_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 40

        elif battalion_1_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 41

        elif battalion_1_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 42

        elif battalion_1_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 43

        elif battalion_1_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_1_current_icon = 44

        elif battalion_1_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_1_current_icon = 1

    def change_2_icon_battalion(self, state, button):
        global battalion_2_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_2_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 2

        elif battalion_2_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 3

        elif battalion_2_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 4

        elif battalion_2_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 5

        elif battalion_2_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 6

        elif battalion_2_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 7

        elif battalion_2_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 8

        elif battalion_2_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 9

        elif battalion_2_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 10

        elif battalion_2_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 11

        elif battalion_2_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 12

        elif battalion_2_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 13

        elif battalion_2_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 14

        elif battalion_2_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 15

        elif battalion_2_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 16

        elif battalion_2_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 17

        elif battalion_2_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 18

        elif battalion_2_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 19

        elif battalion_2_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 20

        elif battalion_2_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 21

        elif battalion_2_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 22

        elif battalion_2_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 23

        elif battalion_2_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 24

        elif battalion_2_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 25

        elif battalion_2_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 26

        elif battalion_2_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 27

        elif battalion_2_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 28

        elif battalion_2_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 29

        elif battalion_2_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 30

        elif battalion_2_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 31

        elif battalion_2_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 32

        elif battalion_2_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 33

        elif battalion_2_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 34

        elif battalion_2_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 35

        elif battalion_2_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 36

        elif battalion_2_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 37

        elif battalion_2_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 38

        elif battalion_2_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 39

        elif battalion_2_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 40

        elif battalion_2_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 41

        elif battalion_2_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 42

        elif battalion_2_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 43

        elif battalion_2_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_2_current_icon = 44

        elif battalion_2_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_2_current_icon = 1

    def change_3_icon_battalion(self, state, button):
        global battalion_3_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_3_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 2

        elif battalion_3_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 3

        elif battalion_3_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 4

        elif battalion_3_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 5

        elif battalion_3_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 6

        elif battalion_3_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 7

        elif battalion_3_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 8

        elif battalion_3_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 9

        elif battalion_3_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 10

        elif battalion_3_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 11

        elif battalion_3_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 12

        elif battalion_3_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 13

        elif battalion_3_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 14

        elif battalion_3_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 15

        elif battalion_3_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 16

        elif battalion_3_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 17

        elif battalion_3_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 18

        elif battalion_3_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 19

        elif battalion_3_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 20

        elif battalion_3_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 21

        elif battalion_3_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 22

        elif battalion_3_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 23

        elif battalion_3_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 24

        elif battalion_3_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 25

        elif battalion_3_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 26

        elif battalion_3_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 27

        elif battalion_3_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 28

        elif battalion_3_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 29

        elif battalion_3_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 30

        elif battalion_3_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 31

        elif battalion_3_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 32

        elif battalion_3_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 33

        elif battalion_3_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 34

        elif battalion_3_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 35

        elif battalion_3_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 36

        elif battalion_3_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 37

        elif battalion_3_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 38

        elif battalion_3_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 39

        elif battalion_3_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 40

        elif battalion_3_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 41

        elif battalion_3_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 42

        elif battalion_3_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 43

        elif battalion_3_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_3_current_icon = 44

        elif battalion_3_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_3_current_icon = 1

    def change_4_icon_battalion(self, state, button):
        global battalion_4_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_4_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 2

        elif battalion_4_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 3

        elif battalion_4_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 4

        elif battalion_4_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 5

        elif battalion_4_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 6

        elif battalion_4_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 7

        elif battalion_4_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 8

        elif battalion_4_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 9

        elif battalion_4_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 10

        elif battalion_4_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 11

        elif battalion_4_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 12

        elif battalion_4_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 13

        elif battalion_4_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 14

        elif battalion_4_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 15

        elif battalion_4_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 16

        elif battalion_4_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 17

        elif battalion_4_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 18

        elif battalion_4_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 19

        elif battalion_4_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 20

        elif battalion_4_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 21

        elif battalion_4_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 22

        elif battalion_4_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 23

        elif battalion_4_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 24

        elif battalion_4_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 25

        elif battalion_4_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 26

        elif battalion_4_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 27

        elif battalion_4_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 28

        elif battalion_4_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 29

        elif battalion_4_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 30

        elif battalion_4_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 31

        elif battalion_4_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 32

        elif battalion_4_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 33

        elif battalion_4_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 34

        elif battalion_4_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 35

        elif battalion_4_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 36

        elif battalion_4_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 37

        elif battalion_4_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 38

        elif battalion_4_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 39

        elif battalion_4_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 40

        elif battalion_4_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 41

        elif battalion_4_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 42

        elif battalion_4_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 43

        elif battalion_4_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_4_current_icon = 44

        elif battalion_4_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_4_current_icon = 1

    def change_5_icon_battalion(self, state, button):
        global battalion_5_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_5_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 2

        elif battalion_5_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 3

        elif battalion_5_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 4

        elif battalion_5_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 5

        elif battalion_5_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 6

        elif battalion_5_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 7

        elif battalion_5_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 8

        elif battalion_5_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 9

        elif battalion_5_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 10

        elif battalion_5_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 11

        elif battalion_5_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 12

        elif battalion_5_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 13

        elif battalion_5_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 14

        elif battalion_5_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 15

        elif battalion_5_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 16

        elif battalion_5_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 17

        elif battalion_5_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 18

        elif battalion_5_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 19

        elif battalion_5_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 20

        elif battalion_5_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 21

        elif battalion_5_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 22

        elif battalion_5_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 23

        elif battalion_5_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 24

        elif battalion_5_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 25

        elif battalion_5_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 26

        elif battalion_5_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 27

        elif battalion_5_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 28

        elif battalion_5_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 29

        elif battalion_5_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 30

        elif battalion_5_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 31

        elif battalion_5_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 32

        elif battalion_5_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 33

        elif battalion_5_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 34

        elif battalion_5_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 35

        elif battalion_5_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 36

        elif battalion_5_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 37

        elif battalion_5_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 38

        elif battalion_5_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 39

        elif battalion_5_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 40

        elif battalion_5_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 41

        elif battalion_5_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 42

        elif battalion_5_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 43

        elif battalion_5_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_5_current_icon = 44

        elif battalion_5_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_5_current_icon = 1

    def change_11_icon_battalion(self, state, button):
        global battalion_11_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_11_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 2

        elif battalion_11_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 3

        elif battalion_11_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 4

        elif battalion_11_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 5

        elif battalion_11_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 6

        elif battalion_11_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 7

        elif battalion_11_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 8

        elif battalion_11_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 9

        elif battalion_11_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 10

        elif battalion_11_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 11

        elif battalion_11_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 12

        elif battalion_11_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 13

        elif battalion_11_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 14

        elif battalion_11_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 15

        elif battalion_11_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 16

        elif battalion_11_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 17

        elif battalion_11_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 18

        elif battalion_11_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 19

        elif battalion_11_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 20

        elif battalion_11_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 21

        elif battalion_11_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 22

        elif battalion_11_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 23

        elif battalion_11_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 24

        elif battalion_11_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 25

        elif battalion_11_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 26

        elif battalion_11_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 27

        elif battalion_11_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 28

        elif battalion_11_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 29

        elif battalion_11_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 30

        elif battalion_11_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 31

        elif battalion_11_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 32

        elif battalion_11_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 33

        elif battalion_11_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 34

        elif battalion_11_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 35

        elif battalion_11_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 36

        elif battalion_11_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 37

        elif battalion_11_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 38

        elif battalion_11_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 39

        elif battalion_11_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 40

        elif battalion_11_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 41

        elif battalion_11_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 42

        elif battalion_11_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 43

        elif battalion_11_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_11_current_icon = 44

        elif battalion_11_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_11_current_icon = 1

    def change_12_icon_battalion(self, state, button):
        global battalion_12_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_12_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 2

        elif battalion_12_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 3

        elif battalion_12_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 4

        elif battalion_12_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 5

        elif battalion_12_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 6

        elif battalion_12_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 7

        elif battalion_12_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 8

        elif battalion_12_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 9

        elif battalion_12_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 10

        elif battalion_12_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 11

        elif battalion_12_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 12

        elif battalion_12_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 13

        elif battalion_12_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 14

        elif battalion_12_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 15

        elif battalion_12_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 16

        elif battalion_12_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 17

        elif battalion_12_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 18

        elif battalion_12_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 19

        elif battalion_12_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 20

        elif battalion_12_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 21

        elif battalion_12_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 22

        elif battalion_12_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 23

        elif battalion_12_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 24

        elif battalion_12_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 25

        elif battalion_12_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 26

        elif battalion_12_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 27

        elif battalion_12_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 28

        elif battalion_12_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 29

        elif battalion_12_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 30

        elif battalion_12_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 31

        elif battalion_12_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 32

        elif battalion_12_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 33

        elif battalion_12_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 34

        elif battalion_12_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 35

        elif battalion_12_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 36

        elif battalion_12_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 37

        elif battalion_12_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 38

        elif battalion_12_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 39

        elif battalion_12_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 40

        elif battalion_12_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 41

        elif battalion_12_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 42

        elif battalion_12_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 43

        elif battalion_12_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_12_current_icon = 44

        elif battalion_12_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_12_current_icon = 1

    def change_13_icon_battalion(self, state, button):
        global battalion_13_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_13_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 2

        elif battalion_13_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 3

        elif battalion_13_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 4

        elif battalion_13_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 5

        elif battalion_13_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 6

        elif battalion_13_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 7

        elif battalion_13_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 8

        elif battalion_13_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 9

        elif battalion_13_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 10

        elif battalion_13_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 11

        elif battalion_13_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 12

        elif battalion_13_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 13

        elif battalion_13_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 14

        elif battalion_13_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 15

        elif battalion_13_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 16

        elif battalion_13_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 17

        elif battalion_13_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 18

        elif battalion_13_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 19

        elif battalion_13_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 20

        elif battalion_13_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 21

        elif battalion_13_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 22

        elif battalion_13_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 23

        elif battalion_13_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 24

        elif battalion_13_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 25

        elif battalion_13_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 26

        elif battalion_13_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 27

        elif battalion_13_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 28

        elif battalion_13_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 29

        elif battalion_13_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 30

        elif battalion_13_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 31

        elif battalion_13_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 32

        elif battalion_13_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 33

        elif battalion_13_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 34

        elif battalion_13_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 35

        elif battalion_13_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 36

        elif battalion_13_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 37

        elif battalion_13_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 38

        elif battalion_13_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 39

        elif battalion_13_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 40

        elif battalion_13_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 41

        elif battalion_13_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 42

        elif battalion_13_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 43

        elif battalion_13_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_13_current_icon = 44

        elif battalion_13_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_13_current_icon = 1

    def change_14_icon_battalion(self, state, button):
        global battalion_14_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_14_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 2

        elif battalion_14_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 3

        elif battalion_14_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 4

        elif battalion_14_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 5

        elif battalion_14_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 6

        elif battalion_14_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 7

        elif battalion_14_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 8

        elif battalion_14_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 9

        elif battalion_14_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 10

        elif battalion_14_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 11

        elif battalion_14_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 12

        elif battalion_14_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 13

        elif battalion_14_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 14

        elif battalion_14_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 15

        elif battalion_14_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 16

        elif battalion_14_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 17

        elif battalion_14_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 18

        elif battalion_14_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 19

        elif battalion_14_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 20

        elif battalion_14_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 21

        elif battalion_14_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 22

        elif battalion_14_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 23

        elif battalion_14_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 24

        elif battalion_14_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 25

        elif battalion_14_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 26

        elif battalion_14_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 27

        elif battalion_14_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 28

        elif battalion_14_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 29

        elif battalion_14_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 30

        elif battalion_14_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 31

        elif battalion_14_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 32

        elif battalion_14_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 33

        elif battalion_14_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 34

        elif battalion_14_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 35

        elif battalion_14_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 36

        elif battalion_14_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 37

        elif battalion_14_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 38

        elif battalion_14_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 39

        elif battalion_14_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 40

        elif battalion_14_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 41

        elif battalion_14_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 42

        elif battalion_14_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 43

        elif battalion_14_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 44

        elif battalion_14_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_14_current_icon = 1

    def change_15_icon_battalion(self, state, button):
        global battalion_15_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_15_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 2

        elif battalion_15_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 3

        elif battalion_15_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 4

        elif battalion_15_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 5

        elif battalion_15_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 6

        elif battalion_15_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 7

        elif battalion_15_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 8

        elif battalion_15_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 9

        elif battalion_15_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 10

        elif battalion_15_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 11

        elif battalion_15_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 12

        elif battalion_15_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 13

        elif battalion_15_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 14

        elif battalion_15_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 15

        elif battalion_15_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 16

        elif battalion_15_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 17

        elif battalion_15_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 18

        elif battalion_15_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 19

        elif battalion_15_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 20

        elif battalion_15_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 21

        elif battalion_15_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 22

        elif battalion_15_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 23

        elif battalion_15_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 24

        elif battalion_15_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 25

        elif battalion_15_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 26

        elif battalion_15_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 27

        elif battalion_15_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 28

        elif battalion_15_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 29

        elif battalion_15_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 30

        elif battalion_15_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 31

        elif battalion_15_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 32

        elif battalion_15_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 33

        elif battalion_15_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 34

        elif battalion_15_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 35

        elif battalion_15_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 36

        elif battalion_15_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 37

        elif battalion_15_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 38

        elif battalion_15_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 39

        elif battalion_15_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 40

        elif battalion_15_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 41

        elif battalion_15_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 42

        elif battalion_15_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 43

        elif battalion_15_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_15_current_icon = 44

        elif battalion_15_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_15_current_icon = 1

    def change_21_icon_battalion(self, state, button):
        global battalion_21_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_21_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 2

        elif battalion_21_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 3

        elif battalion_21_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 4

        elif battalion_21_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 5

        elif battalion_21_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 6

        elif battalion_21_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 7

        elif battalion_21_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 8

        elif battalion_21_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 9

        elif battalion_21_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 10

        elif battalion_21_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 11

        elif battalion_21_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 12

        elif battalion_21_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 13

        elif battalion_21_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 14

        elif battalion_21_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 15

        elif battalion_21_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 16

        elif battalion_21_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 17

        elif battalion_21_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 18

        elif battalion_21_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 19

        elif battalion_21_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 20

        elif battalion_21_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 21

        elif battalion_21_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 22

        elif battalion_21_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 23

        elif battalion_21_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 24

        elif battalion_21_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 25

        elif battalion_21_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 26

        elif battalion_21_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 27

        elif battalion_21_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 28

        elif battalion_21_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 29

        elif battalion_21_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 30

        elif battalion_21_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 31

        elif battalion_21_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 32

        elif battalion_21_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 33

        elif battalion_21_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 34

        elif battalion_21_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 35

        elif battalion_21_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 36

        elif battalion_21_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 37

        elif battalion_21_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 38

        elif battalion_21_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 39

        elif battalion_21_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 40

        elif battalion_21_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 41

        elif battalion_21_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 42

        elif battalion_21_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 43

        elif battalion_21_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_21_current_icon = 44

        elif battalion_21_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_21_current_icon = 1

    def change_22_icon_battalion(self, state, button):
        global battalion_22_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_22_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 2

        elif battalion_22_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 3

        elif battalion_22_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 4

        elif battalion_22_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 5

        elif battalion_22_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 6

        elif battalion_22_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 7

        elif battalion_22_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 8

        elif battalion_22_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 9

        elif battalion_22_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 10

        elif battalion_22_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 11

        elif battalion_22_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 12

        elif battalion_22_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 13

        elif battalion_22_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 14

        elif battalion_22_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 15

        elif battalion_22_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 16

        elif battalion_22_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 17

        elif battalion_22_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 18

        elif battalion_22_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 19

        elif battalion_22_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 20

        elif battalion_22_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 21

        elif battalion_22_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 22

        elif battalion_22_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 23

        elif battalion_22_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 24

        elif battalion_22_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 25

        elif battalion_22_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 26

        elif battalion_22_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 27

        elif battalion_22_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 28

        elif battalion_22_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 29

        elif battalion_22_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 30

        elif battalion_22_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 31

        elif battalion_22_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 32

        elif battalion_22_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 33

        elif battalion_22_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 34

        elif battalion_22_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 35

        elif battalion_22_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 36

        elif battalion_22_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 37

        elif battalion_22_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 38

        elif battalion_22_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 39

        elif battalion_22_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 40

        elif battalion_22_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 41

        elif battalion_22_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 42

        elif battalion_22_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 43

        elif battalion_22_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_22_current_icon = 44

        elif battalion_22_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_22_current_icon = 1

    def change_23_icon_battalion(self, state, button):
        global battalion_23_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_23_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 2

        elif battalion_23_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 3

        elif battalion_23_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 4

        elif battalion_23_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 5

        elif battalion_23_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 6

        elif battalion_23_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 7

        elif battalion_23_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 8

        elif battalion_23_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 9

        elif battalion_23_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 10

        elif battalion_23_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 11

        elif battalion_23_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 12

        elif battalion_23_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 13

        elif battalion_23_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 14

        elif battalion_23_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 15

        elif battalion_23_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 16

        elif battalion_23_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 17

        elif battalion_23_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 18

        elif battalion_23_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 19

        elif battalion_23_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 20

        elif battalion_23_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 21

        elif battalion_23_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 22

        elif battalion_23_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 23

        elif battalion_23_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 24

        elif battalion_23_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 25

        elif battalion_23_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 26

        elif battalion_23_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 27

        elif battalion_23_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 28

        elif battalion_23_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 29

        elif battalion_23_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 30

        elif battalion_23_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 31

        elif battalion_23_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 32

        elif battalion_23_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 33

        elif battalion_23_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 34

        elif battalion_23_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 35

        elif battalion_23_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 36

        elif battalion_23_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 37

        elif battalion_23_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 38

        elif battalion_23_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 39

        elif battalion_23_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 40

        elif battalion_23_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 41

        elif battalion_23_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 42

        elif battalion_23_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 43

        elif battalion_23_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_23_current_icon = 44

        elif battalion_23_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_23_current_icon = 1

    def change_24_icon_battalion(self, state, button):
        global battalion_24_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_24_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 2

        elif battalion_24_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 3

        elif battalion_24_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 4

        elif battalion_24_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 5

        elif battalion_24_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 6

        elif battalion_24_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 7

        elif battalion_24_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 8

        elif battalion_24_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 9

        elif battalion_24_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 10

        elif battalion_24_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 11

        elif battalion_24_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 12

        elif battalion_24_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 13

        elif battalion_24_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 14

        elif battalion_24_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 15

        elif battalion_24_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 16

        elif battalion_24_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 17

        elif battalion_24_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 18

        elif battalion_24_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 19

        elif battalion_24_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 20

        elif battalion_24_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 21

        elif battalion_24_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 22

        elif battalion_24_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 23

        elif battalion_24_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 24

        elif battalion_24_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 25

        elif battalion_24_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 26

        elif battalion_24_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 27

        elif battalion_24_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 28

        elif battalion_24_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 29

        elif battalion_24_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 30

        elif battalion_24_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 31

        elif battalion_24_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 32

        elif battalion_24_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 33

        elif battalion_24_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 34

        elif battalion_24_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 35

        elif battalion_24_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 36

        elif battalion_24_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 37

        elif battalion_24_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 38

        elif battalion_24_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 39

        elif battalion_24_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 40

        elif battalion_24_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 41

        elif battalion_24_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 42

        elif battalion_24_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 43

        elif battalion_24_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_24_current_icon = 44

        elif battalion_24_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_24_current_icon = 1

    def change_25_icon_battalion(self, state, button):
        global battalion_25_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_25_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 2

        elif battalion_25_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 3

        elif battalion_25_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 4

        elif battalion_25_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 5

        elif battalion_25_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 6

        elif battalion_25_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 7

        elif battalion_25_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 8

        elif battalion_25_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 9

        elif battalion_25_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 10

        elif battalion_25_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 11

        elif battalion_25_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 12

        elif battalion_25_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 13

        elif battalion_25_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 14

        elif battalion_25_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 15

        elif battalion_25_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 16

        elif battalion_25_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 17

        elif battalion_25_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 18

        elif battalion_25_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 19

        elif battalion_25_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 20

        elif battalion_25_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 21

        elif battalion_25_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 22

        elif battalion_25_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 23

        elif battalion_25_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 24

        elif battalion_25_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 25

        elif battalion_25_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 26

        elif battalion_25_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 27

        elif battalion_25_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 28

        elif battalion_25_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 29

        elif battalion_25_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 30

        elif battalion_25_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 31

        elif battalion_25_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 32

        elif battalion_25_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 33

        elif battalion_25_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 34

        elif battalion_25_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 35

        elif battalion_25_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 36

        elif battalion_25_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 37

        elif battalion_25_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 38

        elif battalion_25_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 39

        elif battalion_25_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 40

        elif battalion_25_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 41

        elif battalion_25_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 42

        elif battalion_25_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 43

        elif battalion_25_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_25_current_icon = 44

        elif battalion_25_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_25_current_icon = 1

    def change_31_icon_battalion(self, state, button):
        global battalion_31_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_31_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 2

        elif battalion_31_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 3

        elif battalion_31_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 4

        elif battalion_31_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 5

        elif battalion_31_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 6

        elif battalion_31_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 7

        elif battalion_31_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 8

        elif battalion_31_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 9

        elif battalion_31_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 10

        elif battalion_31_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 11

        elif battalion_31_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 12

        elif battalion_31_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 13

        elif battalion_31_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 14

        elif battalion_31_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 15

        elif battalion_31_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 16

        elif battalion_31_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 17

        elif battalion_31_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 18

        elif battalion_31_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 19

        elif battalion_31_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 20

        elif battalion_31_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 21

        elif battalion_31_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 22

        elif battalion_31_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 23

        elif battalion_31_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 24

        elif battalion_31_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 25

        elif battalion_31_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 26

        elif battalion_31_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 27

        elif battalion_31_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 28

        elif battalion_31_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 29

        elif battalion_31_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 30

        elif battalion_31_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 31

        elif battalion_31_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 32

        elif battalion_31_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 33

        elif battalion_31_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 34

        elif battalion_31_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 35

        elif battalion_31_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 36

        elif battalion_31_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 37

        elif battalion_31_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 38

        elif battalion_31_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 39

        elif battalion_31_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 40

        elif battalion_31_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 41

        elif battalion_31_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 42

        elif battalion_31_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 43

        elif battalion_31_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_31_current_icon = 44

        elif battalion_31_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_31_current_icon = 1

    def change_32_icon_battalion(self, state, button):
        global battalion_32_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_32_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 2

        elif battalion_32_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 3

        elif battalion_32_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 4

        elif battalion_32_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 5

        elif battalion_32_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 6

        elif battalion_32_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 7

        elif battalion_32_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 8

        elif battalion_32_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 9

        elif battalion_32_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 10

        elif battalion_32_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 11

        elif battalion_32_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 12

        elif battalion_32_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 13

        elif battalion_32_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 14

        elif battalion_32_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 15

        elif battalion_32_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 16

        elif battalion_32_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 17

        elif battalion_32_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 18

        elif battalion_32_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 19

        elif battalion_32_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 20

        elif battalion_32_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 21

        elif battalion_32_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 22

        elif battalion_32_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 23

        elif battalion_32_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 24

        elif battalion_32_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 25

        elif battalion_32_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 26

        elif battalion_32_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 27

        elif battalion_32_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 28

        elif battalion_32_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 29

        elif battalion_32_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 30

        elif battalion_32_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 31

        elif battalion_32_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 32

        elif battalion_32_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 33

        elif battalion_32_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 34

        elif battalion_32_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 35

        elif battalion_32_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 36

        elif battalion_32_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 37

        elif battalion_32_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 38

        elif battalion_32_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 39

        elif battalion_32_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 40

        elif battalion_32_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 41

        elif battalion_32_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 42

        elif battalion_32_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 43

        elif battalion_32_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_32_current_icon = 44

        elif battalion_32_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_32_current_icon = 1

    def change_33_icon_battalion(self, state, button):
        global battalion_33_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_33_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 2

        elif battalion_33_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 3

        elif battalion_33_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 4

        elif battalion_33_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 5

        elif battalion_33_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 6

        elif battalion_33_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 7

        elif battalion_33_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 8

        elif battalion_33_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 9

        elif battalion_33_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 10

        elif battalion_33_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 11

        elif battalion_33_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 12

        elif battalion_33_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 13

        elif battalion_33_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 14

        elif battalion_33_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 15

        elif battalion_33_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 16

        elif battalion_33_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 17

        elif battalion_33_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 18

        elif battalion_33_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 19

        elif battalion_33_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 20

        elif battalion_33_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 21

        elif battalion_33_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 22

        elif battalion_33_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 23

        elif battalion_33_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 24

        elif battalion_33_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 25

        elif battalion_33_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 26

        elif battalion_33_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 27

        elif battalion_33_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 28

        elif battalion_33_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 29

        elif battalion_33_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 30

        elif battalion_33_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 31

        elif battalion_33_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 32

        elif battalion_33_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 33

        elif battalion_33_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 34

        elif battalion_33_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 35

        elif battalion_33_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 36

        elif battalion_33_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 37

        elif battalion_33_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 38

        elif battalion_33_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 39

        elif battalion_33_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 40

        elif battalion_33_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 41

        elif battalion_33_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 42

        elif battalion_33_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 43

        elif battalion_33_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_33_current_icon = 44

        elif battalion_33_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_33_current_icon = 1

    def change_34_icon_battalion(self, state, button):
        global battalion_34_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_34_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 2

        elif battalion_34_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 3

        elif battalion_34_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 4

        elif battalion_34_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 5

        elif battalion_34_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 6

        elif battalion_34_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 7

        elif battalion_34_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 8

        elif battalion_34_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 9

        elif battalion_34_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 10

        elif battalion_34_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 11

        elif battalion_34_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 12

        elif battalion_34_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 13

        elif battalion_34_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 14

        elif battalion_34_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 15

        elif battalion_34_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 16

        elif battalion_34_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 17

        elif battalion_34_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 18

        elif battalion_34_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 19

        elif battalion_34_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 20

        elif battalion_34_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 21

        elif battalion_34_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 22

        elif battalion_34_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 23

        elif battalion_34_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 24

        elif battalion_34_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 25

        elif battalion_34_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 26

        elif battalion_34_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 27

        elif battalion_34_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 28

        elif battalion_34_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 29

        elif battalion_34_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 30

        elif battalion_34_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 31

        elif battalion_34_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 32

        elif battalion_34_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 33

        elif battalion_34_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 34

        elif battalion_34_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 35

        elif battalion_34_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 36

        elif battalion_34_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 37

        elif battalion_34_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 38

        elif battalion_34_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 39

        elif battalion_34_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 40

        elif battalion_34_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 41

        elif battalion_34_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 42

        elif battalion_34_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 43

        elif battalion_34_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_34_current_icon = 44

        elif battalion_34_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_34_current_icon = 1

    def change_35_icon_battalion(self, state, button):
        global battalion_35_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_35_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 2

        elif battalion_35_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 3

        elif battalion_35_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 4

        elif battalion_35_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 5

        elif battalion_35_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 6

        elif battalion_35_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 7

        elif battalion_35_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 8

        elif battalion_35_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 9

        elif battalion_35_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 10

        elif battalion_35_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 11

        elif battalion_35_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 12

        elif battalion_35_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 13

        elif battalion_35_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 14

        elif battalion_35_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 15

        elif battalion_35_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 16

        elif battalion_35_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 17

        elif battalion_35_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 18

        elif battalion_35_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 19

        elif battalion_35_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 20

        elif battalion_35_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 21

        elif battalion_35_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 22

        elif battalion_35_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 23

        elif battalion_35_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 24

        elif battalion_35_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 25

        elif battalion_35_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 26

        elif battalion_35_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 27

        elif battalion_35_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 28

        elif battalion_35_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 29

        elif battalion_35_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 30

        elif battalion_35_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 31

        elif battalion_35_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 32

        elif battalion_35_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 33

        elif battalion_35_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 34

        elif battalion_35_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 35

        elif battalion_35_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 36

        elif battalion_35_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 37

        elif battalion_35_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 38

        elif battalion_35_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 39

        elif battalion_35_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 40

        elif battalion_35_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 41

        elif battalion_35_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 42

        elif battalion_35_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 43

        elif battalion_35_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_35_current_icon = 44

        elif battalion_35_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_35_current_icon = 1

    def change_41_icon_battalion(self, state, button):
        global battalion_41_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_41_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 2

        elif battalion_41_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 3

        elif battalion_41_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 4

        elif battalion_41_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 5

        elif battalion_41_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 6

        elif battalion_41_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 7

        elif battalion_41_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 8

        elif battalion_41_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 9

        elif battalion_41_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 10

        elif battalion_41_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 11

        elif battalion_41_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 12

        elif battalion_41_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 13

        elif battalion_41_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 14

        elif battalion_41_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 15

        elif battalion_41_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 16

        elif battalion_41_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 17

        elif battalion_41_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 18

        elif battalion_41_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 19

        elif battalion_41_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 20

        elif battalion_41_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 21

        elif battalion_41_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 22

        elif battalion_41_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 23

        elif battalion_41_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 24

        elif battalion_41_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 25

        elif battalion_41_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 26

        elif battalion_41_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 27

        elif battalion_41_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 28

        elif battalion_41_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 29

        elif battalion_41_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 30

        elif battalion_41_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 31

        elif battalion_41_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 32

        elif battalion_41_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 33

        elif battalion_41_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 34

        elif battalion_41_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 35

        elif battalion_41_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 36

        elif battalion_41_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 37

        elif battalion_41_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 38

        elif battalion_41_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 39

        elif battalion_41_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 40

        elif battalion_41_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 41

        elif battalion_41_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 42

        elif battalion_41_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 43

        elif battalion_41_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_41_current_icon = 44

        elif battalion_41_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_41_current_icon = 1

    def change_42_icon_battalion(self, state, button):
        global battalion_42_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_42_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 2

        elif battalion_42_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 3

        elif battalion_42_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 4

        elif battalion_42_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 5

        elif battalion_42_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 6

        elif battalion_42_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 7

        elif battalion_42_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 8

        elif battalion_42_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 9

        elif battalion_42_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 10

        elif battalion_42_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 11

        elif battalion_42_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 12

        elif battalion_42_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 13

        elif battalion_42_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 14

        elif battalion_42_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 15

        elif battalion_42_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 16

        elif battalion_42_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 17

        elif battalion_42_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 18

        elif battalion_42_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 19

        elif battalion_42_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 20

        elif battalion_42_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 21

        elif battalion_42_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 22

        elif battalion_42_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 23

        elif battalion_42_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 24

        elif battalion_42_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 25

        elif battalion_42_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 26

        elif battalion_42_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 27

        elif battalion_42_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 28

        elif battalion_42_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 29

        elif battalion_42_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 30

        elif battalion_42_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 31

        elif battalion_42_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 32

        elif battalion_42_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 33

        elif battalion_42_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 34

        elif battalion_42_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 35

        elif battalion_42_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 36

        elif battalion_42_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 37

        elif battalion_42_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 38

        elif battalion_42_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 39

        elif battalion_42_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 40

        elif battalion_42_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 41

        elif battalion_42_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 42

        elif battalion_42_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 43

        elif battalion_42_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_42_current_icon = 44

        elif battalion_42_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_42_current_icon = 1

    def change_43_icon_battalion(self, state, button):
        global battalion_43_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_43_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 2

        elif battalion_43_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 3

        elif battalion_43_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 4

        elif battalion_43_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 5

        elif battalion_43_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 6

        elif battalion_43_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 7

        elif battalion_43_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 8

        elif battalion_43_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 9

        elif battalion_43_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 10

        elif battalion_43_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 11

        elif battalion_43_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 12

        elif battalion_43_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 13

        elif battalion_43_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 14

        elif battalion_43_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 15

        elif battalion_43_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 16

        elif battalion_43_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 17

        elif battalion_43_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 18

        elif battalion_43_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 19

        elif battalion_43_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 20

        elif battalion_43_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 21

        elif battalion_43_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 22

        elif battalion_43_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 23

        elif battalion_43_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 24

        elif battalion_43_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 25

        elif battalion_43_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 26

        elif battalion_43_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 27

        elif battalion_43_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 28

        elif battalion_43_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 29

        elif battalion_43_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 30

        elif battalion_43_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 31

        elif battalion_43_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 32

        elif battalion_43_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 33

        elif battalion_43_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 34

        elif battalion_43_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 35

        elif battalion_43_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 36

        elif battalion_43_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 37

        elif battalion_43_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 38

        elif battalion_43_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 39

        elif battalion_43_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 40

        elif battalion_43_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 41

        elif battalion_43_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 42

        elif battalion_43_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 43

        elif battalion_43_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_43_current_icon = 44

        elif battalion_43_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_43_current_icon = 1

    def change_44_icon_battalion(self, state, button):
        global battalion_14_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_14_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 2

        elif battalion_14_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 3

        elif battalion_14_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 4

        elif battalion_14_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 5

        elif battalion_14_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 6

        elif battalion_14_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 7

        elif battalion_14_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 8

        elif battalion_14_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 9

        elif battalion_14_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 10

        elif battalion_14_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 11

        elif battalion_14_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 12

        elif battalion_14_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 13

        elif battalion_14_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 14

        elif battalion_14_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 15

        elif battalion_14_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 16

        elif battalion_14_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 17

        elif battalion_14_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 18

        elif battalion_14_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 19

        elif battalion_14_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 20

        elif battalion_14_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 21

        elif battalion_14_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 22

        elif battalion_14_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 23

        elif battalion_14_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 24

        elif battalion_14_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 25

        elif battalion_14_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 26

        elif battalion_14_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 27

        elif battalion_14_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 28

        elif battalion_14_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 29

        elif battalion_14_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 30

        elif battalion_14_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 31

        elif battalion_14_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 32

        elif battalion_14_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 33

        elif battalion_14_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 34

        elif battalion_14_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 35

        elif battalion_14_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 36

        elif battalion_14_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 37

        elif battalion_14_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 38

        elif battalion_14_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 39

        elif battalion_14_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 40

        elif battalion_14_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 41

        elif battalion_14_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 42

        elif battalion_14_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 43

        elif battalion_14_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_14_current_icon = 44

        elif battalion_14_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_14_current_icon = 1

    def change_45_icon_battalion(self, state, button):
        global battalion_45_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_45_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 2

        elif battalion_45_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 3

        elif battalion_45_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 4

        elif battalion_45_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 5

        elif battalion_45_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 6

        elif battalion_45_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 7

        elif battalion_45_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 8

        elif battalion_45_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 9

        elif battalion_45_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 10

        elif battalion_45_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 11

        elif battalion_45_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 12

        elif battalion_45_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 13

        elif battalion_45_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 14

        elif battalion_45_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 15

        elif battalion_45_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 16

        elif battalion_45_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 17

        elif battalion_45_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 18

        elif battalion_45_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 19

        elif battalion_45_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 20

        elif battalion_45_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 21

        elif battalion_45_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 22

        elif battalion_45_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 23

        elif battalion_45_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 24

        elif battalion_45_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 25

        elif battalion_45_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 26

        elif battalion_45_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 27

        elif battalion_45_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 28

        elif battalion_45_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 29

        elif battalion_45_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 30

        elif battalion_45_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 31

        elif battalion_45_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 32

        elif battalion_45_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 33

        elif battalion_45_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 34

        elif battalion_45_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 35

        elif battalion_45_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 36

        elif battalion_45_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 37

        elif battalion_45_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 38

        elif battalion_45_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 39

        elif battalion_45_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 40

        elif battalion_45_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 41

        elif battalion_45_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 42

        elif battalion_45_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 43

        elif battalion_45_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_45_current_icon = 44

        elif battalion_45_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_45_current_icon = 1

    def change_51_icon_battalion(self, state, button):
        global battalion_51_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_51_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 2

        elif battalion_51_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 3

        elif battalion_51_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 4

        elif battalion_51_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 5

        elif battalion_51_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 6

        elif battalion_51_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 7

        elif battalion_51_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 8

        elif battalion_51_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 9

        elif battalion_51_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 10

        elif battalion_51_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 11

        elif battalion_51_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 12

        elif battalion_51_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 13

        elif battalion_51_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 14

        elif battalion_51_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 15

        elif battalion_51_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 16

        elif battalion_51_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 17

        elif battalion_51_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 18

        elif battalion_51_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 19

        elif battalion_51_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 20

        elif battalion_51_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 21

        elif battalion_51_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 22

        elif battalion_51_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 23

        elif battalion_51_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 24

        elif battalion_51_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 25

        elif battalion_51_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 26

        elif battalion_51_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 27

        elif battalion_51_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 28

        elif battalion_51_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 29

        elif battalion_51_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 30

        elif battalion_51_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 31

        elif battalion_51_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 32

        elif battalion_51_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 33

        elif battalion_51_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 34

        elif battalion_51_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 35

        elif battalion_51_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 36

        elif battalion_51_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 37

        elif battalion_51_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 38

        elif battalion_51_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 39

        elif battalion_51_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 40

        elif battalion_51_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 41

        elif battalion_51_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 42

        elif battalion_51_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 43

        elif battalion_51_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_51_current_icon = 44

        elif battalion_51_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_51_current_icon = 1

    def change_52_icon_battalion(self, state, button):
        global battalion_52_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_52_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 2

        elif battalion_52_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 3

        elif battalion_52_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 4

        elif battalion_52_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 5

        elif battalion_52_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 6

        elif battalion_52_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 7

        elif battalion_52_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 8

        elif battalion_52_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 9

        elif battalion_52_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 10

        elif battalion_52_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 11

        elif battalion_52_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 12

        elif battalion_52_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 13

        elif battalion_52_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 14

        elif battalion_52_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 15

        elif battalion_52_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 16

        elif battalion_52_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 17

        elif battalion_52_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 18

        elif battalion_52_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 19

        elif battalion_52_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 20

        elif battalion_52_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 21

        elif battalion_52_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 22

        elif battalion_52_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 23

        elif battalion_52_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 24

        elif battalion_52_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 25

        elif battalion_52_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 26

        elif battalion_52_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 27

        elif battalion_52_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 28

        elif battalion_52_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 29

        elif battalion_52_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 30

        elif battalion_52_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 31

        elif battalion_52_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 32

        elif battalion_52_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 33

        elif battalion_52_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 34

        elif battalion_52_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 35

        elif battalion_52_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 36

        elif battalion_52_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 37

        elif battalion_52_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 38

        elif battalion_52_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 39

        elif battalion_52_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 40

        elif battalion_52_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 41

        elif battalion_52_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 42

        elif battalion_52_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 43

        elif battalion_52_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_52_current_icon = 44

        elif battalion_52_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_52_current_icon = 1

    def change_53_icon_battalion(self, state, button):
        global battalion_53_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_53_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 2

        elif battalion_53_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 3

        elif battalion_53_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 4

        elif battalion_53_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 5

        elif battalion_53_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 6

        elif battalion_53_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 7

        elif battalion_53_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 8

        elif battalion_53_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 9

        elif battalion_53_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 10

        elif battalion_53_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 11

        elif battalion_53_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 12

        elif battalion_53_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 13

        elif battalion_53_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 14

        elif battalion_53_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 15

        elif battalion_53_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 16

        elif battalion_53_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 17

        elif battalion_53_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 18

        elif battalion_53_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 19

        elif battalion_53_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 20

        elif battalion_53_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 21

        elif battalion_53_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 22

        elif battalion_53_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 23

        elif battalion_53_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 24

        elif battalion_53_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 25

        elif battalion_53_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 26

        elif battalion_53_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 27

        elif battalion_53_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 28

        elif battalion_53_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 29

        elif battalion_53_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 30

        elif battalion_53_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 31

        elif battalion_53_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 32

        elif battalion_53_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 33

        elif battalion_53_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 34

        elif battalion_53_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 35

        elif battalion_53_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 36

        elif battalion_53_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 37

        elif battalion_53_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 38

        elif battalion_53_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 39

        elif battalion_53_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 40

        elif battalion_53_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 41

        elif battalion_53_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 42

        elif battalion_53_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 43

        elif battalion_53_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_53_current_icon = 44

        elif battalion_53_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_53_current_icon = 1

    def change_54_icon_battalion(self, state, button):
        global battalion_54_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_54_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 2

        elif battalion_54_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 3

        elif battalion_54_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 4

        elif battalion_54_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 5

        elif battalion_54_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 6

        elif battalion_54_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 7

        elif battalion_54_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 8

        elif battalion_54_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 9

        elif battalion_54_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 10

        elif battalion_54_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 11

        elif battalion_54_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 12

        elif battalion_54_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 13

        elif battalion_54_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 14

        elif battalion_54_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 15

        elif battalion_54_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 16

        elif battalion_54_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 17

        elif battalion_54_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 18

        elif battalion_54_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 19

        elif battalion_54_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 20

        elif battalion_54_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 21

        elif battalion_54_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 22

        elif battalion_54_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 23

        elif battalion_54_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 24

        elif battalion_54_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 25

        elif battalion_54_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 26

        elif battalion_54_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 27

        elif battalion_54_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 28

        elif battalion_54_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 29

        elif battalion_54_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 30

        elif battalion_54_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 31

        elif battalion_54_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 32

        elif battalion_54_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 33

        elif battalion_54_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 34

        elif battalion_54_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 35

        elif battalion_54_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 36

        elif battalion_54_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 37

        elif battalion_54_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 38

        elif battalion_54_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 39

        elif battalion_54_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 40

        elif battalion_54_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 41

        elif battalion_54_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 42

        elif battalion_54_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 43

        elif battalion_54_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_54_current_icon = 44

        elif battalion_54_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_54_current_icon = 1

    def change_55_icon_battalion(self, state, button):
        global battalion_55_current_icon

        playsound("sound/click_checkbox.wav")
        if battalion_55_current_icon == 1:
            button.setStyleSheet("image:url(combat/unit_amphibious_mechanized_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 2

        elif battalion_55_current_icon == 2:
            button.setStyleSheet("image:url(combat/unit_amphibious_tank_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 3

        elif battalion_55_current_icon == 3:
            button.setStyleSheet("image:url(combat/unit_anti_air_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 4

        elif battalion_55_current_icon == 4:
            button.setStyleSheet("image:url(combat/unit_armored_car_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 5

        elif battalion_55_current_icon == 5:
            button.setStyleSheet("image:url(combat/unit_art_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 6

        elif battalion_55_current_icon == 6:
            button.setStyleSheet("image:url(combat/unit_at_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 7

        elif battalion_55_current_icon == 7:
            button.setStyleSheet("image:url(combat/unit_bicycle_battalion_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 8

        elif battalion_55_current_icon == 8:
            button.setStyleSheet("image:url(combat/unit_bicycle_infantry_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 9

        elif battalion_55_current_icon == 9:
            button.setStyleSheet("image:url(combat/unit_camelry_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 10

        elif battalion_55_current_icon == 10:
            button.setStyleSheet("image:url(combat/unit_cavalry_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 11

        elif battalion_55_current_icon == 11:
            button.setStyleSheet("image:url(combat/unit_fake_intel_unit_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 12

        elif battalion_55_current_icon == 12:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 13

        elif battalion_55_current_icon == 13:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 14

        elif battalion_55_current_icon == 14:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 15

        elif battalion_55_current_icon == 15:
            button.setStyleSheet("image:url(combat/unit_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 16

        elif battalion_55_current_icon == 16:
            button.setStyleSheet("image:url(combat/unit_infantry_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 17

        elif battalion_55_current_icon == 17:
            button.setStyleSheet("image:url(combat/unit_light_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 18

        elif battalion_55_current_icon == 18:
            button.setStyleSheet("image:url(combat/unit_light_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 19

        elif battalion_55_current_icon == 19:
            button.setStyleSheet("image:url(combat/unit_light_tank_at_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 20

        elif battalion_55_current_icon == 20:
            button.setStyleSheet("image:url(combat/unit_light_tank_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 21

        elif battalion_55_current_icon == 21:
            button.setStyleSheet("image:url(combat/unit_marine_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 22

        elif battalion_55_current_icon == 22:
            button.setStyleSheet("image:url(combat/unit_mechanized_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 23

        elif battalion_55_current_icon == 23:
            button.setStyleSheet("image:url(combat/unit_medium_tank_antiair_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 24

        elif battalion_55_current_icon == 24:
            button.setStyleSheet("image:url(combat/unit_medium_tank_artillery_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 25

        elif battalion_55_current_icon == 25:
            button.setStyleSheet("image:url(combat/unit_medium_tank_at_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 26

        elif battalion_55_current_icon == 26:
            button.setStyleSheet("image:url(combat/unit_medium_tank_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 27

        elif battalion_55_current_icon == 27:
            button.setStyleSheet("image:url(combat/unit_modern_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 28

        elif battalion_55_current_icon == 28:
            button.setStyleSheet("image:url(combat/unit_modern_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 29

        elif battalion_55_current_icon == 29:
            button.setStyleSheet("image:url(combat/unit_modern_armor_at_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 30

        elif battalion_55_current_icon == 30:
            button.setStyleSheet("image:url(combat/unit_modern_armor_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 31

        elif battalion_55_current_icon == 31:
            button.setStyleSheet("image:url(combat/unit_mot_anti_air_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 32

        elif battalion_55_current_icon == 32:
            button.setStyleSheet("image:url(combat/unit_mot_art_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 33

        elif battalion_55_current_icon == 33:
            button.setStyleSheet("image:url(combat/unit_mot_at_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 34

        elif battalion_55_current_icon == 34:
            button.setStyleSheet("image:url(combat/unit_mot_rocket_art_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 35

        elif battalion_55_current_icon == 35:
            button.setStyleSheet("image:url(combat/unit_motorized_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 36

        elif battalion_55_current_icon == 36:
            button.setStyleSheet("image:url(combat/unit_motorized_rocket_brigade_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 37

        elif battalion_55_current_icon == 37:
            button.setStyleSheet("image:url(combat/unit_mountain_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 38

        elif battalion_55_current_icon == 38:
            button.setStyleSheet("image:url(combat/unit_paratroop_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 39

        elif battalion_55_current_icon == 39:
            button.setStyleSheet("image:url(combat/unit_rocket_art_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 40

        elif battalion_55_current_icon == 40:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_antiair_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 41

        elif battalion_55_current_icon == 41:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_artillery_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 42

        elif battalion_55_current_icon == 42:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_at_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 43

        elif battalion_55_current_icon == 43:
            button.setStyleSheet("image:url(combat/unit_super_heavy_armor_icon.png);" "background-color: #10120D")
            battalion_55_current_icon = 44

        elif battalion_55_current_icon == 44:
            button.setStyleSheet("image:url(ui/module_slot_icon_locked.png);" "background-color: #10120D")
            battalion_55_current_icon = 1

    def reset_all(self, state, button):
        playsound("sound/click_checkbox.wav")
        global company_1_current_icon
        global company_2_current_icon
        global company_3_current_icon
        global company_4_current_icon
        global company_5_current_icon

        global battalion_1_current_icon
        global battalion_2_current_icon
        global battalion_3_current_icon
        global battalion_4_current_icon
        global battalion_5_current_icon

        global battalion_11_current_icon
        global battalion_12_current_icon
        global battalion_13_current_icon
        global battalion_14_current_icon
        global battalion_15_current_icon

        global battalion_21_current_icon
        global battalion_22_current_icon
        global battalion_23_current_icon
        global battalion_24_current_icon
        global battalion_25_current_icon

        global battalion_31_current_icon
        global battalion_32_current_icon
        global battalion_33_current_icon
        global battalion_34_current_icon
        global battalion_35_current_icon

        global battalion_41_current_icon
        global battalion_42_current_icon
        global battalion_43_current_icon
        global battalion_44_current_icon
        global battalion_45_current_icon

        global battalion_51_current_icon
        global battalion_52_current_icon
        global battalion_53_current_icon
        global battalion_54_current_icon
        global battalion_55_current_icon

        company_1_current_icon = 0
        company_2_current_icon = 0
        company_3_current_icon = 0
        company_4_current_icon = 0
        company_5_current_icon = 0

        battalion_1_current_icon = 0
        battalion_2_current_icon = 0
        battalion_3_current_icon = 0
        battalion_4_current_icon = 0
        battalion_5_current_icon = 0

        battalion_11_current_icon = 0
        battalion_12_current_icon = 0
        battalion_13_current_icon = 0
        battalion_14_current_icon = 0
        battalion_15_current_icon = 0

        battalion_21_current_icon = 0
        battalion_22_current_icon = 0
        battalion_23_current_icon = 0
        battalion_24_current_icon = 0
        battalion_25_current_icon = 0

        battalion_31_current_icon = 0
        battalion_32_current_icon = 0
        battalion_33_current_icon = 0
        battalion_34_current_icon = 0
        battalion_35_current_icon = 0

        battalion_41_current_icon = 0
        battalion_42_current_icon = 0
        battalion_43_current_icon = 0
        battalion_44_current_icon = 0
        battalion_45_current_icon = 0

        battalion_51_current_icon = 0
        battalion_52_current_icon = 0
        battalion_53_current_icon = 0
        battalion_54_current_icon = 0
        battalion_55_current_icon = 0

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "OOB Creator"))

    def savecommand(self, state, button):
        playsound("sound/click_sound.mp3")
        division_name = self.texedit.toPlainText()
        output = open("oob.txt", 'w')
        output.write('division_template = {')
        output.write('\n	name = "'+division_name+'"' )
        output.write('\n')
        output.write('\n	regiments = {')

        if battalion_1_current_icon == 1:
            output.write('')
        elif battalion_1_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 4:
            output.write('\n		anti_air = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 5:
            output.write('\n		armored_car = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 6:
            output.write('\n		art = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 7:
            output.write('\n		at = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 8:
            output.write('\n		infantry = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 10:
            output.write('\n		camelry = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 11:
            output.write('\n		cavalry = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 12:
            output.write('\n')
        elif battalion_1_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 16:
            output.write('\n		heavy_armor = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 17:
            output.write('\n		infantry = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 20:
            output.write('\n		light_tank_at = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 21:
            output.write('\n		light_tank = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 22:
            output.write('\n		mechanized = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 26:
            output.write('\n		medium_tank = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 30:
            output.write('\n		modern_armor = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 33:
            output.write('\n		mot_at = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 35:
            output.write('\n		motorized = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 37:
            output.write('\n		mountain = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 38:
            output.write('\n		paratroop = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 39:
            output.write('\n		rocket_art = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 0 y = 0 }')
        elif battalion_1_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 0 y = 0 }')

        if battalion_2_current_icon == 1:
            output.write('')
        elif battalion_2_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 4:
            output.write('\n		anti_air = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 5:
            output.write('\n		armored_car = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 6:
            output.write('\n		art = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 7:
            output.write('\n		at = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 8:
            output.write('\n		infantry = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 10:
            output.write('\n		camelry = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 11:
            output.write('\n		cavalry = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 12:
            output.write('\n')
        elif battalion_2_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 16:
            output.write('\n		heavy_armor = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 17:
            output.write('\n		infantry = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 20:
            output.write('\n		light_tank_at = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 21:
            output.write('\n		light_tank = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 22:
            output.write('\n		mechanized = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 26:
            output.write('\n		medium_tank = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 30:
            output.write('\n		modern_armor = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 33:
            output.write('\n		mot_at = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 35:
            output.write('\n		motorized = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 37:
            output.write('\n		mountain = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 38:
            output.write('\n		paratroop = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 39:
            output.write('\n		rocket_art = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 0 y = 1 }')
        elif battalion_2_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 0 y = 1 }')
        
        if battalion_3_current_icon == 1:
            output.write('')
        elif battalion_3_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 4:
            output.write('\n		anti_air = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 5:
            output.write('\n		armored_car = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 6:
            output.write('\n		art = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 7:
            output.write('\n		at = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 8:
            output.write('\n		infantry = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 10:
            output.write('\n		camelry = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 11:
            output.write('\n		cavalry = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 12:
            output.write('\n')
        elif battalion_3_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 16:
            output.write('\n		heavy_armor = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 17:
            output.write('\n		infantry = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 20:
            output.write('\n		light_tank_at = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 21:
            output.write('\n		light_tank = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 22:
            output.write('\n		mechanized = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 26:
            output.write('\n		medium_tank = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 30:
            output.write('\n		modern_armor = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 33:
            output.write('\n		mot_at = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 35:
            output.write('\n		motorized = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 37:
            output.write('\n		mountain = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 38:
            output.write('\n		paratroop = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 39:
            output.write('\n		rocket_art = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 0 y = 2 }')
        elif battalion_3_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 0 y = 2 }')
        
        if battalion_4_current_icon == 1:
            output.write('')
        elif battalion_4_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 4:
            output.write('\n		anti_air = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 5:
            output.write('\n		armored_car = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 6:
            output.write('\n		art = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 7:
            output.write('\n		at = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 8:
            output.write('\n		infantry = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 10:
            output.write('\n		camelry = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 11:
            output.write('\n		cavalry = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 12:
            output.write('\n')
        elif battalion_4_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 16:
            output.write('\n		heavy_armor = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 17:
            output.write('\n		infantry = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 20:
            output.write('\n		light_tank_at = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 21:
            output.write('\n		light_tank = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 22:
            output.write('\n		mechanized = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 26:
            output.write('\n		medium_tank = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 30:
            output.write('\n		modern_armor = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 33:
            output.write('\n		mot_at = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 35:
            output.write('\n		motorized = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 37:
            output.write('\n		mountain = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 38:
            output.write('\n		paratroop = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 39:
            output.write('\n		rocket_art = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 0 y = 3 }')
        elif battalion_4_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 0 y = 3 }')
        
        if battalion_5_current_icon == 1:
            output.write('')
        elif battalion_5_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 4:
            output.write('\n		anti_air = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 5:
            output.write('\n		armored_car = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 6:
            output.write('\n		art = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 7:
            output.write('\n		at = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 8:
            output.write('\n		infantry = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 10:
            output.write('\n		camelry = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 11:
            output.write('\n		cavalry = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 12:
            output.write('\n')
        elif battalion_5_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 16:
            output.write('\n		heavy_armor = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 17:
            output.write('\n		infantry = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 20:
            output.write('\n		light_tank_at = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 21:
            output.write('\n		light_tank = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 22:
            output.write('\n		mechanized = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 26:
            output.write('\n		medium_tank = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 30:
            output.write('\n		modern_armor = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 33:
            output.write('\n		mot_at = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 35:
            output.write('\n		motorized = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 37:
            output.write('\n		mountain = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 38:
            output.write('\n		paratroop = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 39:
            output.write('\n		rocket_art = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 0 y = 4 }')
        elif battalion_5_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 0 y = 4 }')
        
        if battalion_11_current_icon == 1:
            output.write('')
        elif battalion_11_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 4:
            output.write('\n		anti_air = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 5:
            output.write('\n		armored_car = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 6:
            output.write('\n		art = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 7:
            output.write('\n		at = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 8:
            output.write('\n		infantry = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 10:
            output.write('\n		camelry = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 11:
            output.write('\n		cavalry = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 12:
            output.write('\n')
        elif battalion_11_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 16:
            output.write('\n		heavy_armor = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 17:
            output.write('\n		infantry = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 20:
            output.write('\n		light_tank_at = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 21:
            output.write('\n		light_tank = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 22:
            output.write('\n		mechanized = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 26:
            output.write('\n		medium_tank = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 30:
            output.write('\n		modern_armor = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 33:
            output.write('\n		mot_at = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 35:
            output.write('\n		motorized = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 37:
            output.write('\n		mountain = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 38:
            output.write('\n		paratroop = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 39:
            output.write('\n		rocket_art = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 1 y = 0 }')
        elif battalion_11_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 1 y = 0 }')

        if battalion_12_current_icon == 1:
            output.write('')
        elif battalion_12_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 4:
            output.write('\n		anti_air = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 5:
            output.write('\n		armored_car = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 6:
            output.write('\n		art = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 7:
            output.write('\n		at = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 8:
            output.write('\n		infantry = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 10:
            output.write('\n		camelry = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 11:
            output.write('\n		cavalry = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 12:
            output.write('\n')
        elif battalion_12_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 16:
            output.write('\n		heavy_armor = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 17:
            output.write('\n		infantry = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 20:
            output.write('\n		light_tank_at = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 21:
            output.write('\n		light_tank = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 22:
            output.write('\n		mechanized = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 26:
            output.write('\n		medium_tank = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 30:
            output.write('\n		modern_armor = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 33:
            output.write('\n		mot_at = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 35:
            output.write('\n		motorized = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 37:
            output.write('\n		mountain = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 38:
            output.write('\n		paratroop = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 39:
            output.write('\n		rocket_art = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 1 y = 1 }')
        elif battalion_12_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 1 y = 1 }')
        
        if battalion_13_current_icon == 1:
            output.write('')
        elif battalion_13_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 4:
            output.write('\n		anti_air = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 5:
            output.write('\n		armored_car = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 6:
            output.write('\n		art = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 7:
            output.write('\n		at = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 8:
            output.write('\n		infantry = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 10:
            output.write('\n		camelry = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 11:
            output.write('\n		cavalry = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 12:
            output.write('\n')
        elif battalion_13_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 16:
            output.write('\n		heavy_armor = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 17:
            output.write('\n		infantry = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 20:
            output.write('\n		light_tank_at = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 21:
            output.write('\n		light_tank = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 22:
            output.write('\n		mechanized = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 26:
            output.write('\n		medium_tank = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 30:
            output.write('\n		modern_armor = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 33:
            output.write('\n		mot_at = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 35:
            output.write('\n		motorized = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 37:
            output.write('\n		mountain = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 38:
            output.write('\n		paratroop = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 39:
            output.write('\n		rocket_art = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 1 y = 2 }')
        elif battalion_13_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 1 y = 2 }')
        
        if battalion_14_current_icon == 1:
            output.write('')
        elif battalion_14_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 4:
            output.write('\n		anti_air = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 5:
            output.write('\n		armored_car = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 6:
            output.write('\n		art = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 7:
            output.write('\n		at = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 8:
            output.write('\n		infantry = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 10:
            output.write('\n		camelry = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 11:
            output.write('\n		cavalry = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 12:
            output.write('\n')
        elif battalion_14_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 16:
            output.write('\n		heavy_armor = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 17:
            output.write('\n		infantry = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 20:
            output.write('\n		light_tank_at = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 21:
            output.write('\n		light_tank = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 22:
            output.write('\n		mechanized = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 26:
            output.write('\n		medium_tank = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 30:
            output.write('\n		modern_armor = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 33:
            output.write('\n		mot_at = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 35:
            output.write('\n		motorized = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 37:
            output.write('\n		mountain = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 38:
            output.write('\n		paratroop = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 39:
            output.write('\n		rocket_art = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 1 y = 3 }')
        elif battalion_14_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 1 y = 3 }')
        
        if battalion_15_current_icon == 1:
            output.write('')
        elif battalion_15_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 4:
            output.write('\n		anti_air = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 5:
            output.write('\n		armored_car = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 6:
            output.write('\n		art = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 7:
            output.write('\n		at = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 8:
            output.write('\n		infantry = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 10:
            output.write('\n		camelry = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 11:
            output.write('\n		cavalry = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 12:
            output.write('\n')
        elif battalion_15_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 16:
            output.write('\n		heavy_armor = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 17:
            output.write('\n		infantry = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 20:
            output.write('\n		light_tank_at = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 21:
            output.write('\n		light_tank = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 22:
            output.write('\n		mechanized = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 26:
            output.write('\n		medium_tank = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 30:
            output.write('\n		modern_armor = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 33:
            output.write('\n		mot_at = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 35:
            output.write('\n		motorized = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 37:
            output.write('\n		mountain = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 38:
            output.write('\n		paratroop = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 39:
            output.write('\n		rocket_art = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 1 y = 4 }')
        elif battalion_15_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 1 y = 4 }')
        
        if battalion_21_current_icon == 1:
            output.write('')
        elif battalion_21_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 4:
            output.write('\n		anti_air = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 5:
            output.write('\n		armored_car = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 6:
            output.write('\n		art = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 7:
            output.write('\n		at = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 8:
            output.write('\n		infantry = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 10:
            output.write('\n		camelry = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 11:
            output.write('\n		cavalry = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 12:
            output.write('\n')
        elif battalion_21_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 16:
            output.write('\n		heavy_armor = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 17:
            output.write('\n		infantry = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 20:
            output.write('\n		light_tank_at = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 21:
            output.write('\n		light_tank = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 22:
            output.write('\n		mechanized = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 26:
            output.write('\n		medium_tank = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 30:
            output.write('\n		modern_armor = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 33:
            output.write('\n		mot_at = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 35:
            output.write('\n		motorized = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 37:
            output.write('\n		mountain = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 38:
            output.write('\n		paratroop = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 39:
            output.write('\n		rocket_art = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 1 y = 0 }')
        elif battalion_21_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 1 y = 0 }')

        if battalion_22_current_icon == 1:
            output.write('')
        elif battalion_22_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 4:
            output.write('\n		anti_air = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 5:
            output.write('\n		armored_car = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 6:
            output.write('\n		art = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 7:
            output.write('\n		at = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 8:
            output.write('\n		infantry = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 10:
            output.write('\n		camelry = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 11:
            output.write('\n		cavalry = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 12:
            output.write('\n')
        elif battalion_22_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 16:
            output.write('\n		heavy_armor = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 17:
            output.write('\n		infantry = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 20:
            output.write('\n		light_tank_at = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 21:
            output.write('\n		light_tank = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 22:
            output.write('\n		mechanized = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 26:
            output.write('\n		medium_tank = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 30:
            output.write('\n		modern_armor = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 33:
            output.write('\n		mot_at = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 35:
            output.write('\n		motorized = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 37:
            output.write('\n		mountain = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 38:
            output.write('\n		paratroop = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 39:
            output.write('\n		rocket_art = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 2 y = 1 }')
        elif battalion_22_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 2 y = 1 }')
        
        if battalion_23_current_icon == 1:
            output.write('')
        elif battalion_23_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 4:
            output.write('\n		anti_air = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 5:
            output.write('\n		armored_car = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 6:
            output.write('\n		art = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 7:
            output.write('\n		at = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 8:
            output.write('\n		infantry = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 10:
            output.write('\n		camelry = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 11:
            output.write('\n		cavalry = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 12:
            output.write('\n')
        elif battalion_23_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 16:
            output.write('\n		heavy_armor = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 17:
            output.write('\n		infantry = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 20:
            output.write('\n		light_tank_at = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 21:
            output.write('\n		light_tank = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 22:
            output.write('\n		mechanized = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 26:
            output.write('\n		medium_tank = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 30:
            output.write('\n		modern_armor = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 33:
            output.write('\n		mot_at = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 35:
            output.write('\n		motorized = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 37:
            output.write('\n		mountain = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 38:
            output.write('\n		paratroop = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 39:
            output.write('\n		rocket_art = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 2 y = 2 }')
        elif battalion_23_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 2 y = 2 }')
        
        if battalion_24_current_icon == 1:
            output.write('')
        elif battalion_24_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 4:
            output.write('\n		anti_air = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 5:
            output.write('\n		armored_car = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 6:
            output.write('\n		art = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 7:
            output.write('\n		at = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 8:
            output.write('\n		infantry = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 10:
            output.write('\n		camelry = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 11:
            output.write('\n		cavalry = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 12:
            output.write('\n')
        elif battalion_24_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 16:
            output.write('\n		heavy_armor = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 17:
            output.write('\n		infantry = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 20:
            output.write('\n		light_tank_at = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 21:
            output.write('\n		light_tank = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 22:
            output.write('\n		mechanized = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 26:
            output.write('\n		medium_tank = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 30:
            output.write('\n		modern_armor = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 33:
            output.write('\n		mot_at = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 35:
            output.write('\n		motorized = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 37:
            output.write('\n		mountain = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 38:
            output.write('\n		paratroop = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 39:
            output.write('\n		rocket_art = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 2 y = 3 }')
        elif battalion_24_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 2 y = 3 }')
        
        if battalion_25_current_icon == 1:
            output.write('')
        elif battalion_25_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 4:
            output.write('\n		anti_air = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 5:
            output.write('\n		armored_car = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 6:
            output.write('\n		art = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 7:
            output.write('\n		at = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 8:
            output.write('\n		infantry = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 10:
            output.write('\n		camelry = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 11:
            output.write('\n		cavalry = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 12:
            output.write('\n')
        elif battalion_25_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 16:
            output.write('\n		heavy_armor = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 17:
            output.write('\n		infantry = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 20:
            output.write('\n		light_tank_at = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 21:
            output.write('\n		light_tank = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 22:
            output.write('\n		mechanized = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 26:
            output.write('\n		medium_tank = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 30:
            output.write('\n		modern_armor = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 33:
            output.write('\n		mot_at = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 35:
            output.write('\n		motorized = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 37:
            output.write('\n		mountain = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 38:
            output.write('\n		paratroop = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 39:
            output.write('\n		rocket_art = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 2 y = 4 }')
        elif battalion_25_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 2 y = 4 }')
        
        if battalion_31_current_icon == 1:
            output.write('')
        elif battalion_31_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 4:
            output.write('\n		anti_air = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 5:
            output.write('\n		armored_car = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 6:
            output.write('\n		art = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 7:
            output.write('\n		at = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 8:
            output.write('\n		infantry = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 10:
            output.write('\n		camelry = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 11:
            output.write('\n		cavalry = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 12:
            output.write('\n')
        elif battalion_31_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 16:
            output.write('\n		heavy_armor = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 17:
            output.write('\n		infantry = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 20:
            output.write('\n		light_tank_at = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 21:
            output.write('\n		light_tank = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 22:
            output.write('\n		mechanized = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 26:
            output.write('\n		medium_tank = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 30:
            output.write('\n		modern_armor = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 33:
            output.write('\n		mot_at = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 35:
            output.write('\n		motorized = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 37:
            output.write('\n		mountain = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 38:
            output.write('\n		paratroop = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 39:
            output.write('\n		rocket_art = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 3 y = 0 }')
        elif battalion_31_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 3 y = 0 }')

        if battalion_32_current_icon == 1:
            output.write('')
        elif battalion_32_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 4:
            output.write('\n		anti_air = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 5:
            output.write('\n		armored_car = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 6:
            output.write('\n		art = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 7:
            output.write('\n		at = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 8:
            output.write('\n		infantry = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 10:
            output.write('\n		camelry = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 11:
            output.write('\n		cavalry = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 12:
            output.write('\n')
        elif battalion_32_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 16:
            output.write('\n		heavy_armor = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 17:
            output.write('\n		infantry = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 20:
            output.write('\n		light_tank_at = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 21:
            output.write('\n		light_tank = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 22:
            output.write('\n		mechanized = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 26:
            output.write('\n		medium_tank = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 30:
            output.write('\n		modern_armor = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 33:
            output.write('\n		mot_at = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 35:
            output.write('\n		motorized = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 37:
            output.write('\n		mountain = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 38:
            output.write('\n		paratroop = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 39:
            output.write('\n		rocket_art = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 3 y = 1 }')
        elif battalion_32_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 3 y = 1 }')
        
        if battalion_33_current_icon == 1:
            output.write('')
        elif battalion_33_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 4:
            output.write('\n		anti_air = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 5:
            output.write('\n		armored_car = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 6:
            output.write('\n		art = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 7:
            output.write('\n		at = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 8:
            output.write('\n		infantry = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 10:
            output.write('\n		camelry = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 11:
            output.write('\n		cavalry = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 12:
            output.write('\n')
        elif battalion_33_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 16:
            output.write('\n		heavy_armor = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 17:
            output.write('\n		infantry = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 20:
            output.write('\n		light_tank_at = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 21:
            output.write('\n		light_tank = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 22:
            output.write('\n		mechanized = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 26:
            output.write('\n		medium_tank = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 30:
            output.write('\n		modern_armor = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 33:
            output.write('\n		mot_at = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 35:
            output.write('\n		motorized = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 37:
            output.write('\n		mountain = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 38:
            output.write('\n		paratroop = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 39:
            output.write('\n		rocket_art = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 3 y = 2 }')
        elif battalion_33_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 3 y = 2 }')
        
        if battalion_34_current_icon == 1:
            output.write('')
        elif battalion_34_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 4:
            output.write('\n		anti_air = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 5:
            output.write('\n		armored_car = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 6:
            output.write('\n		art = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 7:
            output.write('\n		at = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 8:
            output.write('\n		infantry = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 10:
            output.write('\n		camelry = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 11:
            output.write('\n		cavalry = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 12:
            output.write('\n')
        elif battalion_34_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 16:
            output.write('\n		heavy_armor = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 17:
            output.write('\n		infantry = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 20:
            output.write('\n		light_tank_at = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 21:
            output.write('\n		light_tank = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 22:
            output.write('\n		mechanized = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 26:
            output.write('\n		medium_tank = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 30:
            output.write('\n		modern_armor = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 33:
            output.write('\n		mot_at = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 35:
            output.write('\n		motorized = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 37:
            output.write('\n		mountain = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 38:
            output.write('\n		paratroop = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 39:
            output.write('\n		rocket_art = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 3 y = 3 }')
        elif battalion_34_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 3 y = 3 }')
        
        if battalion_35_current_icon == 1:
            output.write('')
        elif battalion_35_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 4:
            output.write('\n		anti_air = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 5:
            output.write('\n		armored_car = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 6:
            output.write('\n		art = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 7:
            output.write('\n		at = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 8:
            output.write('\n		infantry = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 10:
            output.write('\n		camelry = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 11:
            output.write('\n		cavalry = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 12:
            output.write('\n')
        elif battalion_35_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 16:
            output.write('\n		heavy_armor = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 17:
            output.write('\n		infantry = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 20:
            output.write('\n		light_tank_at = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 21:
            output.write('\n		light_tank = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 22:
            output.write('\n		mechanized = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 26:
            output.write('\n		medium_tank = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 30:
            output.write('\n		modern_armor = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 33:
            output.write('\n		mot_at = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 35:
            output.write('\n		motorized = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 37:
            output.write('\n		mountain = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 38:
            output.write('\n		paratroop = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 39:
            output.write('\n		rocket_art = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 3 y = 4 }')
        elif battalion_35_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 3 y = 4 }')
        
        if battalion_41_current_icon == 1:
            output.write('')
        elif battalion_41_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 4:
            output.write('\n		anti_air = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 5:
            output.write('\n		armored_car = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 6:
            output.write('\n		art = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 7:
            output.write('\n		at = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 8:
            output.write('\n		infantry = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 10:
            output.write('\n		camelry = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 11:
            output.write('\n		cavalry = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 12:
            output.write('\n')
        elif battalion_41_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 16:
            output.write('\n		heavy_armor = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 17:
            output.write('\n		infantry = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 20:
            output.write('\n		light_tank_at = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 21:
            output.write('\n		light_tank = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 22:
            output.write('\n		mechanized = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 26:
            output.write('\n		medium_tank = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 30:
            output.write('\n		modern_armor = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 33:
            output.write('\n		mot_at = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 35:
            output.write('\n		motorized = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 37:
            output.write('\n		mountain = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 38:
            output.write('\n		paratroop = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 39:
            output.write('\n		rocket_art = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 4 y = 0 }')
        elif battalion_41_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 4 y = 0 }')

        if battalion_42_current_icon == 1:
            output.write('')
        elif battalion_42_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 4:
            output.write('\n		anti_air = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 5:
            output.write('\n		armored_car = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 6:
            output.write('\n		art = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 7:
            output.write('\n		at = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 8:
            output.write('\n		infantry = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 10:
            output.write('\n		camelry = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 11:
            output.write('\n		cavalry = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 12:
            output.write('\n')
        elif battalion_42_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 16:
            output.write('\n		heavy_armor = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 17:
            output.write('\n		infantry = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 20:
            output.write('\n		light_tank_at = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 21:
            output.write('\n		light_tank = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 22:
            output.write('\n		mechanized = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 26:
            output.write('\n		medium_tank = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 30:
            output.write('\n		modern_armor = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 33:
            output.write('\n		mot_at = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 35:
            output.write('\n		motorized = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 37:
            output.write('\n		mountain = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 38:
            output.write('\n		paratroop = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 39:
            output.write('\n		rocket_art = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 4 y = 1 }')
        elif battalion_42_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 4 y = 1 }')
        
        if battalion_43_current_icon == 1:
            output.write('')
        elif battalion_43_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 4:
            output.write('\n		anti_air = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 5:
            output.write('\n		armored_car = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 6:
            output.write('\n		art = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 7:
            output.write('\n		at = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 8:
            output.write('\n		infantry = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 10:
            output.write('\n		camelry = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 11:
            output.write('\n		cavalry = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 12:
            output.write('\n')
        elif battalion_43_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 16:
            output.write('\n		heavy_armor = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 17:
            output.write('\n		infantry = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 20:
            output.write('\n		light_tank_at = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 21:
            output.write('\n		light_tank = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 22:
            output.write('\n		mechanized = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 26:
            output.write('\n		medium_tank = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 30:
            output.write('\n		modern_armor = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 33:
            output.write('\n		mot_at = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 35:
            output.write('\n		motorized = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 37:
            output.write('\n		mountain = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 38:
            output.write('\n		paratroop = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 39:
            output.write('\n		rocket_art = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 4 y = 2 }')
        elif battalion_43_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 4 y = 2 }')
        
        if battalion_44_current_icon == 1:
            output.write('')
        elif battalion_44_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 4:
            output.write('\n		anti_air = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 5:
            output.write('\n		armored_car = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 6:
            output.write('\n		art = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 7:
            output.write('\n		at = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 8:
            output.write('\n		infantry = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 10:
            output.write('\n		camelry = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 11:
            output.write('\n		cavalry = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 12:
            output.write('\n')
        elif battalion_44_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 16:
            output.write('\n		heavy_armor = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 17:
            output.write('\n		infantry = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 20:
            output.write('\n		light_tank_at = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 21:
            output.write('\n		light_tank = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 22:
            output.write('\n		mechanized = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 26:
            output.write('\n		medium_tank = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 30:
            output.write('\n		modern_armor = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 33:
            output.write('\n		mot_at = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 35:
            output.write('\n		motorized = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 37:
            output.write('\n		mountain = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 38:
            output.write('\n		paratroop = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 39:
            output.write('\n		rocket_art = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 4 y = 3 }')
        elif battalion_44_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 4 y = 3 }')
        
        if battalion_45_current_icon == 1:
            output.write('')
        elif battalion_45_current_icon == 2:
            output.write('\n		amphibious_mechanized = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 3:
            output.write('\n		amphibious_tank = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 4:
            output.write('\n		anti_air = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 5:
            output.write('\n		armored_car = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 6:
            output.write('\n		art = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 7:
            output.write('\n		at = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 8:
            output.write('\n		infantry = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 9:
            output.write('\n		bicycle_batallion = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 10:
            output.write('\n		camelry = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 11:
            output.write('\n		cavalry = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 12:
            output.write('\n')
        elif battalion_45_current_icon == 13:
            output.write('\n		heavy_armor_antiair = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 14:
            output.write('\n		heavy_armor_artillery = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 15:
            output.write('\n		heavy_armor_at = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 16:
            output.write('\n		heavy_armor = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 17:
            output.write('\n		infantry = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 18:
            output.write('\n		light_tank_antiair = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 19:
            output.write('\n		light_tank_artillery = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 20:
            output.write('\n		light_tank_at = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 21:
            output.write('\n		light_tank = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 22:
            output.write('\n		mechanized = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 23:
            output.write('\n		medium_tank_antiair = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 24:
            output.write('\n		medium_tank_artillery = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 25:
            output.write('\n		medium_tank_at = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 26:
            output.write('\n		medium_tank = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 27:
            output.write('\n		modern_armor_antiair = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 28:
            output.write('\n		modern_armor_artillery = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 29:
            output.write('\n		modern_armor_at = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 30:
            output.write('\n		modern_armor = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 31:
            output.write('\n		mot_anti_air = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 32:
            output.write('\n		mot_art_icon = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 33:
            output.write('\n		mot_at = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 34:
            output.write('\n		mot_rocket_art = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 35:
            output.write('\n		motorized = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 36:
            output.write('\n		motorized_rocket_brigade = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 37:
            output.write('\n		mountain = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 38:
            output.write('\n		paratroop = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 39:
            output.write('\n		rocket_art = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 40:
            output.write('\n		super_heavy_armor_antiair = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 41:
            output.write('\n		super_heavy_armor_artillery = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 42:
            output.write('\n		super_heavy_armor_at = { x = 4 y = 4 }')
        elif battalion_45_current_icon == 43:
            output.write('\n		super_heavy_armor = { x = 4 y = 4 }')
        output.write('\n	}')
        output.write('\n    support = {')

        if company_1_current_icon == 1:
            output.write('')
        elif company_1_current_icon == 2:
            output.write('\n		anti_air = { x = 0 y = 0 }')
        elif company_1_current_icon == 3:
            output.write('\n		armored_car_recon = { x = 0 y = 0 }')
        elif company_1_current_icon == 4:
            output.write('\n		armored_recon = { x = 0 y = 0 }')
        elif company_1_current_icon == 5:
            output.write('\n		art = { x = 0 y = 0 }')
        elif company_1_current_icon == 6:
            output.write('\n		at = { x = 0 y = 0 }')
        elif company_1_current_icon == 7:
            output.write('\n		field_hospital = { x = 0 y = 0 }')
        elif company_1_current_icon == 8:
            output.write('\n		logistics_company = { x = 0 y = 0 }')
        elif company_1_current_icon == 9:
            output.write('\n		maintenance_company = { x = 0 y = 0 }')
        elif company_1_current_icon == 10:
            output.write('\n		military_police = { x = 0 y = 0 }')
        elif company_1_current_icon == 8:
            output.write('\n		motorized_recon = { x = 0 y = 0 }')
        elif company_1_current_icon == 9:
            output.write('\n		rocket_art = { x = 0 y = 0 }')
        elif company_1_current_icon == 10:
            output.write('\n		signal_company = { x = 0 y = 0 }')
        elif company_1_current_icon == 9:
            output.write('\n		engineer = { x = 0 y = 0 }')
        elif company_1_current_icon == 10:
            output.write('\n		recon = { x = 0 y = 0 }')
        
        if company_2_current_icon == 1:
            output.write('')
        elif company_2_current_icon == 2:
            output.write('\n		anti_air = { x = 0 y = 1 }')
        elif company_2_current_icon == 3:
            output.write('\n		armored_car_recon = { x = 0 y = 1 }')
        elif company_2_current_icon == 4:
            output.write('\n		armored_recon = { x = 0 y = 1 }')
        elif company_2_current_icon == 5:
            output.write('\n		art = { x = 0 y = 1 }')
        elif company_2_current_icon == 6:
            output.write('\n		at = { x = 0 y = 1 }')
        elif company_2_current_icon == 7:
            output.write('\n		field_hospital = { x = 0 y = 1 }')
        elif company_2_current_icon == 8:
            output.write('\n		logistics_company = { x = 0 y = 1 }')
        elif company_2_current_icon == 9:
            output.write('\n		maintenance_company = { x = 0 y = 1 }')
        elif company_2_current_icon == 10:
            output.write('\n		military_police = { x = 0 y = 1 }')
        elif company_2_current_icon == 8:
            output.write('\n		motorized_recon = { x = 0 y = 1 }')
        elif company_2_current_icon == 9:
            output.write('\n		rocket_art = { x = 0 y = 1 }')
        elif company_2_current_icon == 10:
            output.write('\n		signal_company = { x = 0 y = 1 }')
        elif company_2_current_icon == 9:
            output.write('\n		engineer = { x = 0 y = 1 }')
        elif company_2_current_icon == 10:
            output.write('\n		recon = { x = 0 y = 1 }')
        
        if company_3_current_icon == 1:
            output.write('')
        elif company_3_current_icon == 2:
            output.write('\n		anti_air = { x = 0 y = 2 }')
        elif company_3_current_icon == 3:
            output.write('\n		armored_car_recon = { x = 0 y = 2 }')
        elif company_3_current_icon == 4:
            output.write('\n		armored_recon = { x = 0 y = 2 }')
        elif company_3_current_icon == 5:
            output.write('\n		art = { x = 0 y = 2 }')
        elif company_3_current_icon == 6:
            output.write('\n		at = { x = 0 y = 2 }')
        elif company_3_current_icon == 7:
            output.write('\n		field_hospital = { x = 0 y = 2 }')
        elif company_3_current_icon == 8:
            output.write('\n		logistics_company = { x = 0 y = 2 }')
        elif company_3_current_icon == 9:
            output.write('\n		maintenance_company = { x = 0 y = 2 }')
        elif company_3_current_icon == 10:
            output.write('\n		military_police = { x = 0 y = 2 }')
        elif company_3_current_icon == 8:
            output.write('\n		motorized_recon = { x = 0 y = 2 }')
        elif company_3_current_icon == 9:
            output.write('\n		rocket_art = { x = 0 y = 2 }')
        elif company_3_current_icon == 10:
            output.write('\n		signal_company = { x = 0 y = 2 }')
        elif company_3_current_icon == 9:
            output.write('\n		engineer = { x = 0 y = 2 }')
        elif company_3_current_icon == 10:
            output.write('\n		recon = { x = 0 y = 2 }')
        
        if company_4_current_icon == 1:
            output.write('')
        elif company_4_current_icon == 2:
            output.write('\n		anti_air = { x = 0 y = 3 }')
        elif company_4_current_icon == 3:
            output.write('\n		armored_car_recon = { x = 0 y = 3 }')
        elif company_4_current_icon == 4:
            output.write('\n		armored_recon = { x = 0 y = 3 }')
        elif company_4_current_icon == 5:
            output.write('\n		art = { x = 0 y = 3 }')
        elif company_4_current_icon == 6:
            output.write('\n		at = { x = 0 y = 3 }')
        elif company_4_current_icon == 7:
            output.write('\n		field_hospital = { x = 0 y = 3 }')
        elif company_4_current_icon == 8:
            output.write('\n		logistics_company = { x = 0 y = 3 }')
        elif company_4_current_icon == 9:
            output.write('\n		maintenance_company = { x = 0 y = 3 }')
        elif company_4_current_icon == 10:
            output.write('\n		military_police = { x = 0 y = 3 }')
        elif company_4_current_icon == 8:
            output.write('\n		motorized_recon = { x = 0 y = 3 }')
        elif company_4_current_icon == 9:
            output.write('\n		rocket_art = { x = 0 y = 3 }')
        elif company_4_current_icon == 10:
            output.write('\n		signal_company = { x = 0 y = 3 }')
        elif company_4_current_icon == 9:
            output.write('\n		engineer = { x = 0 y = 3 }')
        elif company_4_current_icon == 10:
            output.write('\n		recon = { x = 0 y = 3 }')
        
        if company_5_current_icon == 1:
            output.write('')
        elif company_5_current_icon == 2:
            output.write('\n		anti_air = { x = 0 y = 4 }')
        elif company_5_current_icon == 3:
            output.write('\n		armored_car_recon = { x = 0 y = 4 }')
        elif company_5_current_icon == 4:
            output.write('\n		armored_recon = { x = 0 y = 4 }')
        elif company_5_current_icon == 5:
            output.write('\n		art = { x = 0 y = 4 }')
        elif company_5_current_icon == 6:
            output.write('\n		at = { x = 0 y = 4 }')
        elif company_5_current_icon == 7:
            output.write('\n		field_hospital = { x = 0 y = 4 }')
        elif company_5_current_icon == 8:
            output.write('\n		logistics_company = { x = 0 y = 4 }')
        elif company_5_current_icon == 9:
            output.write('\n		maintenance_company = { x = 0 y = 4 }')
        elif company_5_current_icon == 10:
            output.write('\n		military_police = { x = 0 y = 4 }')
        elif company_5_current_icon == 8:
            output.write('\n		motorized_recon = { x = 0 y = 4 }')
        elif company_5_current_icon == 9:
            output.write('\n		rocket_art = { x = 0 y = 4 }')
        elif company_5_current_icon == 10:
            output.write('\n		signal_company = { x = 0 y = 4 }')
        elif company_5_current_icon == 9:
            output.write('\n		engineer = { x = 0 y = 4 }')
        elif company_5_current_icon == 10:
            output.write('\n		recon = { x = 0 y = 4 }')
        output.write('\n	}')
        if priority == 2:
            output.write('\n	priority = 2')
        elif priority == 3:
            output.write('\n	priority = 0')
        elif priority == 1:
            output.write('\n	priority = 1')
        output.write('\n}')
        output.write('\n')
        output.close()
        print("Saved!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
