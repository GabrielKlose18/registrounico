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
        # db.close()
        return cursor
    except sqlite3.Error as e:
        db.close()
        print("An error occurred:", e.args[0])
        return False

def validaPacienteExiste(cpf):
    query = ''' SELECT COUNT(*) as qtd FROM paciente WHERE ds_paciente_cpf = "''' + str(cpf) + '''" '''  
    resultado = OpenRecordSet(query)
    result = resultado.fetchone()
    if result[0] > 0:
        return True
    else:
        return False

def buscarConsulta():
    cpf = int(input('Digite o cpf do paciente: '))
    if(validaPacienteExiste(cpf)):
        queryPaciente = ''' SELECT * FROM paciente WHERE ds_paciente_cpf = "''' + str(cpf) + '''" '''  
        resultadoPaciente = OpenRecordSet(queryPaciente)
        resultadoPaciente = resultadoPaciente.fetchone()
        printPaciente = 'Nome: {} \n CPF: {} \n Endereço: {} \n Data de nasc: {}'.format(resultadoPaciente[0], resultadoPaciente[1],resultadoPaciente[2], resultadoPaciente[3])

        queryConsulta = ''' SELECT consulta.ds_consulta_motivo, consulta.dt_consulta FROM paciente JOIN consulta USING(cd_paciente) WHERE paciente.ds_paciente_cpf = "''' + str(cpf) + '''" ''' 
        resultadoConsulta = OpenRecordSet(queryConsulta)
        if(resultadoConsulta != False):
            print(printPaciente+'\n')
            for consulta in resultadoConsulta:
                print('Data da Consulta: {}, Motivo: {} \n'.format(consulta[1], consulta[0]))
        else:
            print('Este paciente não possui consultas.')
        
    else:
         print('Desculpe, este CPF não está cadastrado.')
        


    