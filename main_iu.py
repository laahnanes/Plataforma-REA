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
        self.pages.setGeometry(QRect(170, 70, 1111, 661))
        self.pg_inicio = QWidget()
        self.pg_inicio.setObjectName(u"pg_inicio")
        self.saudacao = QLabel(self.pg_inicio)
        self.saudacao.setObjectName(u"saudacao")
        self.saudacao.setGeometry(QRect(10, 10, 271, 81))
        font = QFont()
        font.setFamily(u"Biko")
        font.setPointSize(30)
        self.saudacao.setFont(font)
        self.listView = QTableView(self.pg_inicio)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(20, 150, 1071, 491))
        self.label_2 = QLabel(self.pg_inicio)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 120, 220, 25))
        font1 = QFont()
        font1.setFamily(u"Biko")
        font1.setPointSize(14)
        self.label_2.setFont(font1)
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
        self.titulo_2 = QLabel(self.pg_publicar)
        self.titulo_2.setObjectName(u"titulo_2")
        self.titulo_2.setGeometry(QRect(30, 100, 91, 31))
        font2 = QFont()
        font2.setFamily(u"Biko")
        font2.setPointSize(18)
        self.titulo_2.setFont(font2)
        self.autor = QLabel(self.pg_publicar)
        self.autor.setObjectName(u"autor")
        self.autor.setGeometry(QRect(30, 160, 81, 31))
        self.autor.setFont(font2)
        self.tipo = QLabel(self.pg_publicar)
        self.tipo.setObjectName(u"tipo")
        self.tipo.setGeometry(QRect(30, 220, 71, 31))
        self.tipo.setFont(font2)
        self.datapubli = QLabel(self.pg_publicar)
        self.datapubli.setObjectName(u"datapubli")
        self.datapubli.setGeometry(QRect(30, 270, 261, 51))
        self.datapubli.setFont(font2)
        self.txt_titulo = QLineEdit(self.pg_publicar)
        self.txt_titulo.setObjectName(u"txt_titulo")
        self.txt_titulo.setGeometry(QRect(120, 100, 971, 31))
        self.txt_autor = QLineEdit(self.pg_publicar)
        self.txt_autor.setObjectName(u"txt_autor")
        self.txt_autor.setGeometry(QRect(120, 160, 401, 31))
        self.cb_tipo = QComboBox(self.pg_publicar)
        self.cb_tipo.addItem("")
        self.cb_tipo.addItem("")
        self.cb_tipo.addItem("")
        self.cb_tipo.addItem("")
        self.cb_tipo.setObjectName(u"cb_tipo")
        self.cb_tipo.setGeometry(QRect(100, 220, 211, 31))
        self.date_publi = QDateEdit(self.pg_publicar)
        self.date_publi.setObjectName(u"date_publi")
        self.date_publi.setGeometry(QRect(300, 280, 131, 31))
        self.arquivo = QLabel(self.pg_publicar)
        self.arquivo.setObjectName(u"arquivo")
        self.arquivo.setGeometry(QRect(30, 330, 111, 51))
        self.arquivo.setFont(font2)
        self.txt_arquivo = QLineEdit(self.pg_publicar)
        self.txt_arquivo.setObjectName(u"txt_arquivo")
        self.txt_arquivo.setGeometry(QRect(140, 340, 401, 31))
        self.btn_publicarRecurso = QPushButton(self.pg_publicar)
        self.btn_publicarRecurso.setObjectName(u"btn_publicarRecurso")
        self.btn_publicarRecurso.setGeometry(QRect(490, 580, 141, 41))
        palette3 = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
        self.btn_publicarRecurso.setPalette(palette3)
        self.btn_publicarRecurso.setFont(font1)
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
        self.btn_publicarRecurso.setText(QCoreApplication.translate("MainWindow", u"Publicar", None))
        self.saudacao.setText(QCoreApplication.translate("MainWindow", u"Bem vindo!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Recursos disponíveis", None))
        self.informes.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"Publicar Novo Recurso", None))
        self.titulo_2.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo:", None))
        self.autor.setText(QCoreApplication.translate("MainWindow", u"Autor:", None))
        self.tipo.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.cb_tipo.setItemText(0, QCoreApplication.translate("Cadastro", u"Artigo", None))
        self.cb_tipo.setItemText(1, QCoreApplication.translate("Cadastro", u"Livro", None))
        self.cb_tipo.setItemText(2, QCoreApplication.translate("Cadastro", u"Execício", None))
        self.cb_tipo.setItemText(3, QCoreApplication.translate("Cadastro", u"Vídeo", None))
        self.datapubli.setText(QCoreApplication.translate("MainWindow", u"Data de publica\u00e7\u00e3o:", None))
        self.arquivo.setText(QCoreApplication.translate("MainWindow", u"Arquivo:", None))
    # retranslateUi

