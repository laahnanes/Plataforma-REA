from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtGui import QGuiApplication
from login_ui import Ui_Form
from main_iu import Ui_MainWindow
from cadastro_ui import Ui_Cadastro
from database import Database
from datetime import datetime
import sys


# Criando a classe Login que instancia um Widget e a tela de login
class Login(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login - Plataforma REA UPE")
        self.center()  # Centralizando a janela na tela

        self.btn_login.clicked.connect(self.open_system)
        self.btn_cadastro.clicked.connect(self.open_cadastro)

    # Função para centralizar a janela
    def center(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        size = self.geometry()
        self.move(
            (screen.width() - size.width()) // 2,
            (screen.height() - size.height()) // 2
        )

    # Redefinindo resizeEvent para centralizar após redimensionar
    def resizeEvent(self, event):
        self.center()
        super().resizeEvent(event)


    def open_system(self, tipo_usuario):
        if self.txt_senha.text() == "123":
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            print("Senha inválida")

    # Função para abrir a tela de cadastro
    def open_cadastro(self):
        self.cadastro = Cadastro()
        self.cadastro.show()
        self.close()


# Criando a classe Cadastro que instancia um Widget e a tela de cadastro
class Cadastro(QWidget, Ui_Cadastro):
    def __init__(self):
        super(Cadastro, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadastro - Plataforma REA UPE")   

        self.btn_efetuarcadastro.clicked.connect(self.coletarDadosUsuario)

    def coletarDadosUsuario(self):
        nome = self.txt_nome.text()
        email = self.txt_email.text()
        senha = self.txt_senha.text()
        tipo_usuario = self.cb_perfil.currentText()
        data_registro = datetime.now().date()

        db = Database()
        db.conexao()
        db.insertUsuarios(nome, email, senha, tipo_usuario, data_registro)
        db.cortarConexao()

        self.txt_nome.setText("")
        self.txt_email.setText("")
        self.txt_senha.setText("")
        self.cb_perfil.setCurrentIndex(-1)

# Criando a classe MainWindow que instancia uma MainWindow e a tela principal main
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Plataforna UPE REA")

        # Butões para as páginas do sistema
        self.btn_inicio.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_inicio))
        self.btn_sobre.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_sobre))
        self.btn_publicar.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_publicar))


# Inicializando o Aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
