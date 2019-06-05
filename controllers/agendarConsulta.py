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

def pacienteExiste(cpf):
    query = ''' SELECT COUNT(*) as qtd FROM paciente WHERE ds_paciente_cpf = "''' + str(cpf) + '''" '''  
    resultado = OpenRecordSet(query)
    result = resultado.fetchone()
    if result[0] > 0:
        return True
    else:
        return False

def verificaDisponibilidade(data):
    query = ''' SELECT COUNT(*) as qtd FROM consulta WHERE dt_consulta = "'''+data+''' "'''  
    resultado = OpenRecordSet(query)
    result = resultado.fetchone()
    print(result)
    if result[0] > 0:
        return False
    else:
        return True

def agendarConsulta():
    cpf = int(input('Digite o cpf do paciente: '))
    motivo = input('Motivo da consulta: ')
    data_consultaPt = input('Digite a data da consulta [d/m/Y]:  ')
    try:
        data_consulta = datetime.strptime(data_consultaPt, '%d/%m/%Y')
        format(data_consulta, "%Y-%m-%d")
        data_consulta = '{}-{}-{}'.format(data_consulta.year, data_consulta.month,data_consulta.day)
    except:
        return print('Data invalida!')
    
    if(not pacienteExiste(cpf)):
        print('Desculpe, este CPF não está cadastrato.')
    else:
        if(verificaDisponibilidade(data_consulta)):
            queryPaciente = ''' SELECT cd_paciente FROM paciente WHERE ds_paciente_cpf = ''' + str(cpf)
            resultadoPaciente = OpenRecordSet(queryPaciente)
            result = resultadoPaciente.fetchone()
            cd_paciente = result[0]
            query = '''
                INSERT INTO `consulta` (`cd_paciente`, `dt_consulta`, `ds_consulta_motivo`) 
                VALUES (" '''+str(cd_paciente)+''' ", "'''+data_consulta+'''", "'''+motivo+'''")
            '''
            if(OpenRecordSet(query) != False):
                print('Agendado com Sucesso!')
            else:
                print('Ops... erro ao agendar consulta.')
        else:
            print('Ops... Agenda deste dia está fechada.')


    