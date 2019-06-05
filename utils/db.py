import pymysql
# Open database connection
db = pymysql.connect(
    "localhost",
    "root",
    "",
    "registrounico" 
)
def OpenRecordSet(query):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    try:
        # execute SQL query using execute() method.
        cursor.execute(query)
        db.close()
        return cursor
    except pymysql.Error as e:
        db.close()
        print("could not close connection error pymysql %d: %s" %(e.args[0], e.args[1]))
        return False


    
    

#x = OpenRecordSet('SELECT * FROM paciente')
#for i in x:
    #print(i)