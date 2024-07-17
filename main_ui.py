# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1297, 737)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1297, 737))
        MainWindow.setMaximumSize(QSize(1297, 737))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(1297, 737))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(156, 0, 1141, 51))
        self.label.setPixmap(QPixmap(u"images_.qrc/fundofaixa.png"))
        self.label.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 161, 741))
        self.label_3.setMidLineWidth(0)
        self.label_3.setPixmap(QPixmap(u"images_.qrc/fundofaixa.png"))
        self.label_3.setScaledContents(True)
        self.btn_inicio = QPushButton(self.centralwidget)
        self.btn_inicio.setObjectName(u"btn_inicio")
        self.btn_inicio.setGeometry(QRect(30, 120, 93, 28))
        self.btn_sobre = QPushButton(self.centralwidget)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setGeometry(QRect(30, 170, 93, 28))
        self.btn_publicar = QPushButton(self.centralwidget)
        self.btn_publicar.setObjectName(u"btn_publicar")
        self.btn_publicar.setGeometry(QRect(30, 220, 93, 28))
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setGeometry(QRect(170, 60, 1111, 661))
        self.pg_inicio = QWidget()
        self.pg_inicio.setObjectName(u"pg_inicio")
        self.saudacao = QLabel(self.pg_inicio)
        self.saudacao.setObjectName(u"saudacao")
        self.saudacao.setGeometry(QRect(10, 10, 271, 81))
        font = QFont()
        font.setFamily(u"Biko")
        font.setPointSize(30)
        self.saudacao.setFont(font)
        self.listView = QListView(self.pg_inicio)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(20, 150, 1071, 491))
        self.label_2 = QLabel(self.pg_inicio)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 120, 191, 16))
        font1 = QFont()
        font1.setFamily(u"Biko")
        font1.setPointSize(14)
        self.label_2.setFont(font1)
        self.label_4 = QLabel(self.pg_inicio)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 270, 591, 211))
        font2 = QFont()
        font2.setPointSize(40)
        self.label_4.setFont(font2)
        self.pages.addWidget(self.pg_inicio)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.informes = QLabel(self.pg_sobre)
        self.informes.setObjectName(u"informes")
        self.informes.setGeometry(QRect(10, 10, 291, 81))
        self.informes.setFont(font)
        self.pages.addWidget(self.pg_sobre)
        self.pg_publicar = QWidget()
        self.pg_publicar.setObjectName(u"pg_publicar")
        self.titulo = QLabel(self.pg_publicar)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(10, 10, 541, 81))
        self.titulo.setFont(font)
        self.pages.addWidget(self.pg_publicar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_3.setText("")
        self.btn_inicio.setText(QCoreApplication.translate("MainWindow", u"IN\u00cdCIO", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_publicar.setText(QCoreApplication.translate("MainWindow", u"PUBLICAR", None))
        self.saudacao.setText(QCoreApplication.translate("MainWindow", u"Bem vindo!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Meus downloads", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"MUDOU", None))
        self.informes.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"Publicar Novo Recurso", None))
    # retranslateUi

