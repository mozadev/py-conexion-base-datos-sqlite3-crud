'''
a cursor is an object of acces to date that you cant for a joint of rows
in a table or insert rows a the table
'''


import sqlite3

class Conexion:

    def __init__(self):
        self.conection = sqlite3.connect("basedatos")
        USER_TABLE = """CREATE TABLE users(
                codigo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
                usuario VARCHAR(50) NOT NULL,
                clave VARCHAR(50) NOT NULL
                )"""
        DROP_USER = "DROP TABLE IF EXISTS `users` "
        cursor = self.conection.cursor()
        cursor.execute(DROP_USER)
        cursor.execute(USER_TABLE)

    def __str__(self):
        data_base= self.query_in_table()
        register=""
        for row in data_base:
            register=register + str(row) + "\n"
        return register
    
    def query_in_table(self):
        cursor_object = self.conection.cursor()
        cursor_object.execute("SELECT * FROM users")
        data_base = cursor_object.fetchall()
        cursor_object.close()
        return data_base

    def insert_in_table(self, usuario, clave, codigo):
        cursor_object = self.conection.cursor()
        instruction='''INSERT INTO users (usuario,clave,codigo) 
        VALUES( '{}', '{}', '{}')'''.format(usuario, clave, codigo)
        cursor_object.execute(instruction)
        n=cursor_object.rowcount
        self.conection.commit()
        cursor_object.close()
        return n    

    def elimina_tabla(self,codigo):
        cursor_object = self.conection.cursor()
        instruccion='''DELETE FROM users WHERE codigo = {}'''.format(codigo)
        cursor_object.execute(instruccion)
        n=cursor_object.rowcount
        self.conection.commit()
        cursor_object.close()
        return n   

    def modifica_tabla(self,usuario,clave,codigo):
        cursor_object = self.conection.cursor()
        instruction='''UPDATE users SET usuario='{}', clave='{}', codigo='{}',
        WHERE codigo={}'''.format(usuario,clave,codigo)
        cursor_object.execute(instruction)
        n=cursor_object.rowcount
        self.conection.commit()
        cursor_object.close()
        return n   
conection_object=Conexion()
conection_object.insert_in_table('juan', '123', '11')
conection_object.insert_in_table('cesar', '125', '12')
print(conection_object)

