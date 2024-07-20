import sqlite3
from PySide2.QtWidgets import QMessageBox

class Database():
    def __init__(self, name= "system.bd") -> None:
        self.name = name
        self.connection = None

    def conexao(self):
        self.connection = sqlite3.connect(self.name)
        return self.connection

    def cortarConexao(self):
        try:
            self.connection.close()
        except: 
            print("Falha")

    def createTable_usuarios(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS usuarios(
                           
                id_Usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,                         
                email VARCHAR(255) NOT NULL UNIQUE,           
                senha VARCHAR(60) NOT NULL UNIQUE,
                tipo_usuario TEXT NOT NULL CHECK(tipo_usuario IN ('Aluno', 'Professor')),
                data_registro DATE NOT NULL
                )""")
            
        except AttributeError:
            print("Falha em criar tabela usuarios")

    def createTable_professores(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS professores(
                           
                id_Usuario INTEGER NOT NULL PRIMARY KEY,
                especialidade VARCHAR(255),
                id_Disciplina INTEGER NOT NULL,
                FOREIGN KEY (id_Usuario) REFERENCES usuarios(id_Usuario) 
                FOREIGN KEY (id_Disciplina) REFERENCES disciplinas(id_Disciplina)            
                )""")
            
        except AttributeError:
            print("Falha em criar tabela professores")

    def createTable_alunos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS alunos(
                           
                id_Usuario INTEGER NOT NULL PRIMARY KEY,
                id_Curso INTEGER NOT NULL,
                matricula VARCHAR(255),
                ano_entrada INTEGER,
                FOREIGN KEY (id_Curso) REFERENCES cursos(id_Curso)             
                FOREIGN KEY (id_Usuario) REFERENCES usuarios(id_Usuario)
                           
                )""")
            
        except AttributeError:
            print("Falha em criar tabela alunos")

    def createTable_recursos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS recursos(
                           
                id_Recurso INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                titulo VARCHAR(255) NOT NULL,
                tipo_recurso TEXT NOT NULL CHECK(tipo_recurso IN ('Artigo', 'Livro', 'Vídeo', 'Exercício')),
                autor VARCHAR(255) NOT NULL,
                publicacao DATE NOT NULL           
                )""")
            
        except AttributeError:
            print("Falha em criar tabela recursos")     

    def createTable_cursos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS cursos(
                           
                id_Curso INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL           
                )""")
            
        except AttributeError:
            print("Falha em criar tabela cursos")   

    def createTable_disciplinas(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS disciplinas(
                           
                id_Disciplina INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                id_Curso INTEGER NOT NULL,
                nome VARCHAR(255) NOT NULL
                FOREIGN KEY (id_Curso) REFERENCES cursos(id_Curso)           
                )""")
            
        except AttributeError:
            print("Falha em criar tabela disciplinas")      

    def createTable_downloads(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS downloads(
                           
                id_Download INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                id_Usuario INTEGER NOT NULL,
                id_Recurso INTEGER NOT NULL,
                data DATE NOT NULL,
                status TEXT NOT NULL CHECK(tipo_usuario IN ('Concluído', 'Falha')),
                FOREIGN KEY (id_Usuario) REFERENCES usuarios(id_Usuario),
                FOREIGN KEY (id_Recurso) REFERENCES recursos(id_Recurso)                      
                )""")
            
        except AttributeError:
            print("Falha em criar tabela downloads")              


    def insertUsuarios(self, nome, email, senha, tipo_usuario, data_registro):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
 
                INSERT INTO usuarios(nome, email, senha, tipo_usuario, data_registro) VALUES (?, ?, ?, ?, ?)
                """, (nome, email, senha, tipo_usuario, data_registro))
            self.connection.commit()
        except: 
            print("Falha em inserir usuário")

    def insertProfessores(self, id_Usuario, especialidade, id_Disciplina):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
 
                INSERT INTO professores(id_Usuario, especialidade, id_Disciplina) VALUES (?, ?, ?)
                """, (id_Usuario, especialidade, id_Disciplina))
            self.connection.commit()
        except: 
            print("Falha em inserir professor")


    def insertAlunos(self, id_Usuario, id_Curso, matricula, anoentrada):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
 
                INSERT INTO alunos(id_Usuario, id_Curso, matricula, anoentrada) VALUES (?, ?, ?, ?)
                """, (id_Usuario, id_Curso, matricula, anoentrada))
            self.connection.commit()
        except: 
            print("Falha em inserir aluno")

    def insertRecursos(self, id_Recurso, titulo, tipo_recurso, autor, publicacao):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
 
                INSERT INTO recursos(id_Recurso, titulo, tipo_recurso, autor, publicacao) VALUES (?, ?, ?, ?, ?)
                """, (id_Recurso, titulo, tipo_recurso, autor, publicacao))
            self.connection.commit()
        except: 
            print("Falha em inserir recurso")

    def insertCurso(self, id_Curso):
        nomecurso = ""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
 
                INSERT INTO cursos(id_Curso, nome) VALUES (?, ?)
                """, (id_Curso, nomecurso))
            self.connection.commit()
        except: 
            print("Falha em inserir curso")

    def insertDisciplina(self, id_Disciplina, id_Curso):
        nomedisciplina = ""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
 
                INSERT INTO disciplinas(id_Disciplina, id_Curso, nome) VALUES (?, ?, ?)
                """, (id_Disciplina, id_Curso, nomedisciplina))
            self.connection.commit()
        except: 
            print("Falha em inserir disciplina")













    def checarPerfilUsuario(self, nome, senha):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

            SELECT * FROM usuarios;

            """)

            for linha in cursor.fetchall():
                if linha[1].upper() == nome.upper() and linha[3] == senha and linha[4] == "Aluno":
                    return "Aluno"
                elif linha[1].upper() == nome.upper() and linha[3] == senha and linha[4] == "Professor":
                    return "Professor"
                else:
                    continue
            return "Usuário não cadastrado"
        except:
            print("Usuário não cadastrado")
              

if __name__ == "__main__":
    db = Database()     
    db.conexao()
    db.createTable_usuarios()
    db.cortarConexao()        