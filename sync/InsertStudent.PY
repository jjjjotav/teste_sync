import SyncEduc, sqlite3

inName = input('Nome: ')
inEmail = input('Email: ')
inDate_birth = input('Nascimento em (yyyy-mm-dd): ')
inPassword = input('Senha: ')

banco = sqlite3.connect('SyncEduc.db')

cursor = banco.cursor()

cursor.execute("""
INSERT INTO tb_student (Name, Email, Date_birth, Password)
VALUES (?,?,?,?)
""", (inName, inEmail, inDate_birth, inPassword)

)

banco.commit()

print('Dados inseridos com sucesso.')

banco.close()