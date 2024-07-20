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


    def insertUsuarios(self, nome, email, senha, tipo_usuario, data_registro):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
 
                INSERT INTO usuarios(nome, email, senha, tipo_usuario, data_registro) VALUES (?, ?, ?, ?, ?)
                """, (nome, email, senha, tipo_usuario, data_registro))
            self.connection.commit()
        except: 
            print("Falha em inserir usuário")


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