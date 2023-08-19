import SyncEduc, sqlite3

inName = input('Nome: ')
inEmail = input('Email: ')
inDate_birth = input('Nascimento em (yyyy-mm-dd): ')
inPassword = input('Senha: ')
inCpf = input('CPF: ')

banco = sqlite3.connect('SyncEduc.db')

cursor = banco.cursor()

cursor.execute("""
INSERT INTO tb_teacher (Name, Email, Date_birth, Password, Cpf)
VALUES (?,?,?,?,?)
""", (inName, inEmail, inDate_birth, inPassword, inCpf)

)

banco.commit()

print('Dados inseridos com sucesso.')

banco.close()