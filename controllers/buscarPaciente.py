import sqlite3
from datetime import datetime

def OpenRecordSet(query):
    # Open database connection
    db = sqlite3.connect('registrounico.db')
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    try:
        # execute SQL query using execute() method.
        return cursor.execute(query)
    except sqlite3.Error as e:
        db.close()
        print("An error occurred:", e.args[0])
        return False

def validaPacienteExiste(cpf):
    query = ''' SELECT COUNT(*) as qtd FROM paciente WHERE ds_paciente_cpf = "''' + str(cpf) + '''" '''  
    resultado = OpenRecordSet(query)
    result = resultado.fetchone()
    print(result)
    if result[0] > 0:
        return True
    else:
        return False

def buscarPaciente():
    cpf = int(input('Digite o cpf do paciente: '))
    if(validaPacienteExiste(cpf)):
        queryPaciente = ''' SELECT * FROM paciente WHERE ds_paciente_cpf = ''' + str(cpf)
        resultadoPaciente = OpenRecordSet(queryPaciente)
        print(resultadoPaciente)
        resultadoPaciente = resultadoPaciente.fetchone()
        print(resultadoPaciente)
        print('Nome: {} \n CPF: {} \n Endereço: {} \n Data de nasc: {}'.format(resultadoPaciente[1], resultadoPaciente[2],resultadoPaciente[3], resultadoPaciente[4]))
    else:
         print('Desculpe, este CPF não está cadastrado.')
        


    