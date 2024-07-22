from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PySide2.QtGui import QGuiApplication
from PySide2.QtCore import QDate
from login_ui import Ui_Form
from main_iu import Ui_MainWindow
from cadastro_ui import Ui_Cadastro
from database import Database
from datetime import datetime
import sys


class Login(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login - Plataforma REA UPE")
        self.center() 

        self.btn_login.clicked.connect(self.checarUsuario)
        self.btn_cadastro.clicked.connect(self.open_cadastro)


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


    def checarUsuario(self):
        self.nome = Database()
        self.nome.conexao()
        autenticar = self.nome.checarPerfilUsuario(self.txt_nome.text().upper(), self.txt_senha.text())

        if autenticar.lower() == "aluno" or autenticar.lower() == "professor":
            self.w = MainWindow(autenticar.lower())
            self.w.show()
            self.close()
        else: 
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro ao acessar")
            msg.setText(f"Nome ou senha incorretos!")
            msg.exec_()


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
        matricula = self.txt_matricula.text()
        anoentrada = self.txt_anoentrada.text()
        especialidade = self.txt_especialidade.text()

        db = Database()
        db.conexao()
        db.insertUsuarios(nome, email, senha, tipo_usuario, data_registro)

        # Obter o ID do usuário inserido
        cursor = db.connection.cursor()
        cursor.execute("SELECT last_insert_rowid()")
        id_Usuario = cursor.fetchone()[0]
        id_Curso = self.cb_curso.currentIndex() + 1
        id_Disciplina = self.cb_disciplina.currentIndex() + 6

        if self.cb_perfil.currentIndex() == 0: #aluno
            db.insertAlunos(id_Usuario, id_Curso, matricula, anoentrada)
        elif self.cb_perfil.currentIndex() == 1: # professor
            db.insertProfessores(id_Usuario, especialidade, id_Disciplina) 

        db.cortarConexao()

        self.txt_nome.setText("")
        self.txt_email.setText("")
        self.txt_senha.setText("")
        self.cb_perfil.setCurrentIndex(-1)
        self.txt_matricula.setText("")
        self.txt_anoentrada.setText("")
        self.txt_especialidade.setText("")
        self.cb_curso.setCurrentIndex(-1)
        self.cb_disciplina.setCurrentIndex(-1)

        self.w = MainWindow(tipo_usuario)
        self.w.show()
        self.close()

# Criando a classe MainWindow que instancia uma MainWindow e a tela principal main
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, tipo_usuario):

        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Plataforna UPE REA")

        if tipo_usuario.lower() == "aluno":
            self.btn_publicar.setVisible(False)

        # Butões para as páginas do sistema
        self.btn_inicio.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_inicio))
        self.btn_sobre.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_sobre))
        self.btn_publicar.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_publicar))
        self.btn_publicarRecurso.clicked.connect(self.coletaDadosRecursos)

    def coletaDadosRecursos(self):
        titulo = self.txt_titulo.text()
        autor = self.txt_autor.text()
        publicacao = self.date_publi.date().toString("yyyy-MM-dd")  # Use o formato ISO para datas
        tipo = self.cb_tipo.currentText()
        arquivo = self.txt_arquivo.text()

        db = Database()
        db.conexao()
        db.insertRecursos(titulo, tipo, autor, publicacao, arquivo)
        db.cortarConexao()
        
        self.txt_titulo.setText("")
        self.txt_autor.setText("")
        self.date_publi.setDate(QDate.currentDate())
        self.cb_tipo.setCurrentIndex(-1)
        self.txt_arquivo.setText("")


# Inicializando o Aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
