# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Cadastro(object):
    def setupUi(self, Cadastro):
        if not Cadastro.objectName():
            Cadastro.setObjectName(u"Cadastro")
        Cadastro.resize(1297, 737)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Cadastro.sizePolicy().hasHeightForWidth())
        Cadastro.setSizePolicy(sizePolicy)
        Cadastro.setMinimumSize(QSize(1297, 737))
        Cadastro.setMaximumSize(QSize(1297, 737))
        self.faixa = QLabel(Cadastro)
        self.faixa.setObjectName(u"faixa")
        self.faixa.setGeometry(QRect(0, 0, 1297, 111))
        self.faixa.setMinimumSize(QSize(5, 0))
        self.faixa.setPixmap(QPixmap(u"images_.qrc/fundofaixa.png"))
        self.faixa.setScaledContents(True)
        self.saudacao = QLabel(Cadastro)
        self.saudacao.setObjectName(u"saudacao")
        self.saudacao.setGeometry(QRect(560, 20, 211, 81))
        font = QFont()
        font.setFamily(u"Biko")
        font.setPointSize(30)
        self.saudacao.setFont(font)
        self.label = QLabel(Cadastro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 110, 1301, 631))
        self.label.setPixmap(QPixmap(u"images_.qrc/fundorea.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Cadastro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 110, 1041, 591))
        self.label_2.setAutoFillBackground(True)
        self.nome = QLabel(Cadastro)
        self.nome.setObjectName(u"nome")
        self.nome.setGeometry(QRect(300, 170, 231, 41))
        font1 = QFont()
        font1.setFamily(u"Biko")
        font1.setPointSize(18)
        self.nome.setFont(font1)
        self.email = QLabel(Cadastro)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(300, 240, 81, 41))
        self.email.setFont(font1)
        self.senha = QLabel(Cadastro)
        self.senha.setObjectName(u"senha")
        self.senha.setGeometry(QRect(300, 310, 91, 41))
        self.senha.setFont(font1)
        self.perfil = QLabel(Cadastro)
        self.perfil.setObjectName(u"perfil")
        self.perfil.setGeometry(QRect(300, 380, 81, 41))
        self.perfil.setFont(font1)
        self.txt_nome = QLineEdit(Cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(530, 170, 691, 31))
        self.txt_email = QLineEdit(Cadastro)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(390, 240, 831, 31))
        self.txt_senha = QLineEdit(Cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(390, 310, 381, 31))
        self.cb_perfil = QComboBox(Cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setGeometry(QRect(380, 380, 171, 41))
        font2 = QFont()
        font2.setFamily(u"Biko")
        font2.setPointSize(12)
        self.cb_perfil.setFont(font2)
        self.btn_efetuarcadastro = QPushButton(Cadastro)
        self.btn_efetuarcadastro.setObjectName(u"btn_efetuarcadastro")
        self.btn_efetuarcadastro.setGeometry(QRect(670, 620, 201, 51))
        palette = QPalette()
        brush = QBrush(QColor(240, 240, 240, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
        self.btn_efetuarcadastro.setPalette(palette)
        font3 = QFont()
        font3.setFamily(u"Biko")
        font3.setPointSize(14)
        self.btn_efetuarcadastro.setFont(font3)
        self.label.raise_()
        self.faixa.raise_()
        self.saudacao.raise_()
        self.label_2.raise_()
        self.nome.raise_()
        self.email.raise_()
        self.senha.raise_()
        self.perfil.raise_()
        self.txt_nome.raise_()
        self.txt_email.raise_()
        self.txt_senha.raise_()
        self.cb_perfil.raise_()
        self.btn_efetuarcadastro.raise_()

        self.retranslateUi(Cadastro)

        QMetaObject.connectSlotsByName(Cadastro)
    # setupUi

    def retranslateUi(self, Cadastro):
        Cadastro.setWindowTitle(QCoreApplication.translate("Cadastro", u"Form", None))
        self.faixa.setText("")
        self.saudacao.setText(QCoreApplication.translate("Cadastro", u"Cadastro", None))
        self.label.setText("")
        self.label_2.setText("")
        self.nome.setText(QCoreApplication.translate("Cadastro", u"Nome Completo:", None))
        self.email.setText(QCoreApplication.translate("Cadastro", u"Email:", None))
        self.senha.setText(QCoreApplication.translate("Cadastro", u"Senha:", None))
        self.perfil.setText(QCoreApplication.translate("Cadastro", u"Perfil:", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("Cadastro", u"Aluno", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("Cadastro", u"Professor", None))

        self.btn_efetuarcadastro.setText(QCoreApplication.translate("Cadastro", u"Cadastre-se", None))
    # retranslateUi

