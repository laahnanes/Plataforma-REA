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
                FOREIGN KEY (id_Usuario) REFERENCES usuarios(id_Usuario), 
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
                FOREIGN KEY (id_Curso) REFERENCES cursos(id_Curso),             
                FOREIGN KEY (id_Usuario) REFERENCES usuarios(id_Usuario)
                           
                )""")
            
        except Exception as e:
            print("Falha em criar tabela alunos:", e)

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
                )
            """)
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao criar tabela: {e}")
        except sqlite3.OperationalError as e:
            print(f"Erro operacional ao criar tabela: {e}")
        except sqlite3.DatabaseError as e:
            print(f"Erro no banco de dados ao criar tabela: {e}")
        except Exception as e:
            print(f"Falha desconhecida ao criar tabela: {e}")

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
                nome VARCHAR(255) NOT NULL,
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
                status TEXT NOT NULL CHECK(status IN ('Concluído', 'Falha')),
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
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir aluno: {e}")
        except sqlite3.OperationalError as e:
            print(f"Erro operacional ao inserir aluno: {e}")
        except sqlite3.DatabaseError as e:
            print(f"Erro no banco de dados ao inserir aluno: {e}")
        except Exception as e:
            print(f"Falha desconhecida ao inserir aluno: {e}")

    def insertProfessores(self, id_Usuario, especialidade, id_Disciplina):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
 
                INSERT INTO professores(id_Usuario, especialidade, id_Disciplina) VALUES (?, ?, ?)
                """, (id_Usuario, especialidade, id_Disciplina))
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir aluno: {e}")
        except sqlite3.OperationalError as e:
            print(f"Erro operacional ao inserir aluno: {e}")
        except sqlite3.DatabaseError as e:
            print(f"Erro no banco de dados ao inserir aluno: {e}")
        except Exception as e:
            print(f"Falha desconhecida ao inserir aluno: {e}")



    def insertAlunos(self, id_Usuario, id_Curso, matricula, anoentrada):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO alunos(id_Usuario, id_Curso, matricula, ano_entrada) VALUES (?, ?, ?, ?)
            """, (id_Usuario, id_Curso, matricula, anoentrada))
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir aluno: {e}")
        except sqlite3.OperationalError as e:
            print(f"Erro operacional ao inserir aluno: {e}")
        except sqlite3.DatabaseError as e:
            print(f"Erro no banco de dados ao inserir aluno: {e}")
        except Exception as e:
            print(f"Falha desconhecida ao inserir aluno: {e}")


    def insertRecursos(self, titulo, tipo_recurso, autor, publicacao, arquivo):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO recursos (titulo, tipo_recurso, autor, publicacao, arquivo)
                VALUES (?, ?, ?, ?, ?)
            """, (titulo, tipo_recurso, autor, publicacao, arquivo))
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade ao inserir recurso: {e}")
        except sqlite3.OperationalError as e:
            print(f"Erro operacional ao inserir recurso: {e}")
        except sqlite3.DatabaseError as e:
            print(f"Erro no banco de dados ao inserir recurso: {e}")
        except Exception as e:
            print(f"Falha desconhecida ao inserir recurso: {e}")


    def insertCurso(self, id_Curso, nomecurso):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
 
                INSERT INTO cursos(id_Curso, nome) VALUES (?, ?)
                """, (id_Curso, nomecurso))
            self.connection.commit()
        except: 
            print("Falha em inserir curso")

    def insertDisciplina(self, id_Curso, nomedisciplina):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO disciplinas (id_Curso, nome)
                VALUES (?, ?)
            """, (id_Curso, nomedisciplina))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Falha em inserir disciplina: {e}")


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

    def deleteUsuario(self, id_Usuario):
        try:
            cursor = self.connection.cursor()

            # Deletar registro na tabela alunos, se existir
            cursor.execute("DELETE FROM alunos WHERE id_Usuario = ?", (id_Usuario,))

            # Deletar registro na tabela professores, se existir
            cursor.execute("DELETE FROM professores WHERE id_Usuario = ?", (id_Usuario,))

            # Deletar registro na tabela usuarios
            cursor.execute("DELETE FROM usuarios WHERE id_Usuario = ?", (id_Usuario,))
            
            self.connection.commit()
            print(f"Usuário com ID {id_Usuario} deletado com sucesso.")
        except Exception as e:
            print("Falha em deletar usuário:", e)

    def dropTable_recursos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DROP TABLE IF EXISTS recursos")
            self.connection.commit()
            print("Tabela 'recursos' excluída com sucesso.")
        except sqlite3.OperationalError as e:
            print(f"Erro operacional ao excluir tabela: {e}")
        except sqlite3.DatabaseError as e:
            print(f"Erro no banco de dados ao excluir tabela: {e}")
        except Exception as e:
            print(f"Falha desconhecida ao excluir tabela: {e}")
        

if __name__ == "__main__":
    db = Database()     
    db.conexao()
    db.createTable_recursos()
    
    

    db.cortarConexao()        