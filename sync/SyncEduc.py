import sqlite3


banco = sqlite3.connect('SyncEduc.db')

cursor = banco.cursor()

'''cursor.execute(""" 
   CREATE TABLE tb_student (
        Id_user INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Name CHAR(200) NOT NULL,
        Email CHAR(200) NOT NULL,
        Date_birth DATE NOT NULL,
        Password CHAR(200) NOT NULL         
 );

""")'''

'''cursor.execute(""" 
   CREATE TABLE tb_teacher (
        Id_user INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Name CHAR(200) NOT NULL,
        Email CHAR(200) NOT NULL,
        Date_birth DATE NOT NULL,
        Password CHAR(200) NOT NULL,
        Cpf VARCHAR(11) NOT NULL      
 );

""")'''


cursor.execute("SELECT * FROM tb_student")
print(cursor.fetchall())
cursor.execute("SELECT * FROM tb_teacher")
print(cursor.fetchall())  



