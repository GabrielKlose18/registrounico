import sqlite3
from datetime import datetime

def OpenRecordSet(query):
    # Open database connection
    db = sqlite3.connect('registrounico.db')
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    try:
        # execute SQL query using execute() method.
        cursor.execute(query)
        db.commit()
        return cursor
    except sqlite3.Error as e:
        db.close()
        print("An error occurred:", e.args[0])
        return False

def validaCpfExiste(cpf):
    query = ''' SELECT COUNT(*) as qtd FROM paciente WHERE ds_paciente_cpf = ''' + str(cpf)   
    resultado = OpenRecordSet(query)
    result = resultado.fetchone()
    if result[0] > 0:
       return True
    else:
       return False

def cadastrarPaciente():
    nome = input('Digite o nome do paciente: ')
    cpf = int(input('Digite o cpf do paciente: '))
    endereco = input('Digite o endereço do paciente: ')
    nascimento = input('Digite a data de nascimento do paciente do paciente: [d/m/Y] ')
    nascimento = datetime.strptime(nascimento, '%d/%m/%Y')
    format(nascimento, "%Y-%m-%d")
    nascimento = '{}-{}-{}'.format(nascimento.year, nascimento.month,nascimento.day)
    query = '''
        INSERT INTO `paciente` (`ds_paciente_nome`, `ds_paciente_cpf`, `ds_paciente_endereco`, `dt_paciente_nascimento`) 
        VALUES (" '''+nome+''' ", "'''+str(cpf)+'''", "'''+endereco+'''", "'''+nascimento+'''")
    '''
    if(validaCpfExiste(cpf) != False):
        return 'Desculpe, este CPF já foi inserido.'
    else:
        if(OpenRecordSet(query)):
            print('Paciente cadastrato com sucesso!')
        else:
            print('Ops... Erro ao cadastrar paciente.')


    