import SyncEduc
import sqlite3

try:
    banco = sqlite3.connect('SyncEduc.db')

    cursor = banco.cursor()

    cursor.execute('DELETE FROM tb_student WHERE Id_user = 1 ')

    banco.commit()
    banco.close()
    print("Os dados foram removidos com sucesso!!")

except sqlite3 as ERROR:
    print('Error ao deletar: ', ERROR)