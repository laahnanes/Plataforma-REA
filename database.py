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
            self.connection.close()

            # Criação das tabelas

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
            
        except sqlite3.DatabaseError as e:
            print(f"Falha ao criar tabela usuarios: {e}")

    def createTable_professores(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS professores(
                           
                id_Usuario INTEGER NOT NULL PRIMARY KEY,
                especialidade VARCHAR(255),
                id_Disciplina INTEGER NOT NULL,
                FOREIGN KEY (id_Usuario) REFERENCES usuarios(id_Usuario), 
                FOREIGN KEY (id_Disciplina) REFERENCES disciplinas(id_Disciplina)            
                )""")
            
        except sqlite3.DatabaseError as e:
            print(f"Falha ao criar tabela professores: {e}")

    def createTable_alunos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS alunos(
                           
                id_Usuario INTEGER NOT NULL PRIMARY KEY,
                id_Curso INTEGER NOT NULL,
                matricula VARCHAR(255),
                ano_entrada INTEGER,
                FOREIGN KEY (id_Curso) REFERENCES cursos(id_Curso),             
                FOREIGN KEY (id_Usuario) REFERENCES usuarios(id_Usuario)        
                )""")
            
        except sqlite3.DatabaseError as e:
            print(f"Falha ao criar tabela alunos: {e}")

    def createTable_recursos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS recursos (
                    id_Recurso INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    titulo VARCHAR(255) NOT NULL,
                    tipo_recurso TEXT NOT NULL CHECK(tipo_recurso IN ('Artigo', 'Livro', 'Vídeo', 'Exercício')),
                    autor VARCHAR(255) NOT NULL,
                    publicacao DATE NOT NULL,
                    arquivo TEXT NOT NULL
                )""")
            
        except sqlite3.DatabaseError as e:
            print(f"Falha ao criar tabela recursos: {e}")

    def createTable_cursos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS cursos(
                           
                id_Curso INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL           
                )""")
            
        except sqlite3.DatabaseError as e:
            print(f"Falha ao criar tabela cursos: {e}") 

    def createTable_disciplinas(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS disciplinas(
                           
                id_Disciplina INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                id_Curso INTEGER NOT NULL,
                nome VARCHAR(255) NOT NULL,
                FOREIGN KEY (id_Curso) REFERENCES cursos(id_Curso)           
                )""")
            
        except sqlite3.DatabaseError as e:
            print(f"Falha ao criar tabela disciplinas: {e}")  

    #   Métodos de inserção         

    def insertUsuarios(self, nome, email, senha, tipo_usuario, data_registro):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
 
                INSERT INTO usuarios(nome, email, senha, tipo_usuario, data_registro) VALUES (?, ?, ?, ?, ?)
                """, (nome, email, senha, tipo_usuario, data_registro))
            
            self.connection.commit()

        except sqlite3.DatabaseError as e:
            print(f"Falha ao inserir usuarios: {e}")

    def insertProfessores(self, id_Usuario, especialidade, id_Disciplina):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
 
                INSERT INTO professores(id_Usuario, especialidade, id_Disciplina) VALUES (?, ?, ?)
                """, (id_Usuario, especialidade, id_Disciplina))
            
            self.connection.commit()

        except sqlite3.DatabaseError as e:
            print(f"Falha ao inserir professores: {e}")


    def insertAlunos(self, id_Usuario, id_Curso, matricula, anoentrada):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO alunos(id_Usuario, id_Curso, matricula, ano_entrada) VALUES (?, ?, ?, ?)
            """, (id_Usuario, id_Curso, matricula, anoentrada))

            self.connection.commit()

        except sqlite3.DatabaseError as e:
            print(f"Falha ao inserir alunos: {e}")


    def insertRecursos(self, titulo, tipo_recurso, autor, publicacao, arquivo):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO recursos (titulo, tipo_recurso, autor, publicacao, arquivo)
                VALUES (?, ?, ?, ?, ?)
            """, (titulo, tipo_recurso, autor, publicacao, arquivo))

            self.connection.commit()

        except sqlite3.DatabaseError as e:
            print(f"Falha ao inserir recursos: {e}")


    def insertCurso(self, id_Curso, nomecurso):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
 
                INSERT INTO cursos(id_Curso, nome) VALUES (?, ?)
                """, (id_Curso, nomecurso))
            
            self.connection.commit()

        except sqlite3.DatabaseError as e:
            print(f"Falha ao inserir cursos: {e}")

    def insertDisciplina(self, id_Curso, nomedisciplina):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO disciplinas (id_Curso, nome)
                VALUES (?, ?)
            """, (id_Curso, nomedisciplina))

            self.connection.commit()

        except sqlite3.DatabaseError as e:
            print(f"Falha ao inserir disciplina: {e}")


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
        except:
            print("Usuário não cadastrado")

    def deleteUsuario(self, id_Usuario):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM alunos WHERE id_Usuario = ?", (id_Usuario,))
            cursor.execute("DELETE FROM professores WHERE id_Usuario = ?", (id_Usuario,))
            cursor.execute("DELETE FROM usuarios WHERE id_Usuario = ?", (id_Usuario,))
            
            self.connection.commit()

        except Exception as e:
            print("Falha em deletar usuário:", e)


    def fetchRecursos(self):
            cursor = self.connection.cursor()
            cursor.execute("SELECT titulo, arquivo FROM recursos")
            return cursor.fetchall()  
        
if __name__ == "__main__":
    db = Database()     
    db.conexao()
    db.createTable_usuarios()
    db.createTable_professores()
    db.createTable_alunos()
    db.createTable_recursos()
    db.createTable_cursos()
    db.createTable_disciplinas()
    db.cortarConexao()        