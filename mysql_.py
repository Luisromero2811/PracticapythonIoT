import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="cheque",
  password="root",
  database="IoT"
)

mycursor = mydb.cursor()

def Insertar(valores,sensor):
    sql = "INSERT INTO Sensores (nombre, valor, fecha) VALUES (%s, %s, %s)"
    if sensor=='pir':
        fecha=valores['fecha']
        valor=valores['movimiento']
        val=(sensor,valor,fecha)
        mycursor.execute(sql, val)
        mydb.commit()
    elif sensor=='DHT11':
        humedad='humedad'
        temp='temperatura'
        fecha=valores['fecha']
        valor1=valores['humedad']
        valor2=valores['temp']
        val=(humedad,valor1,fecha)
        val2=(temp,valor2,fecha)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute(sql,val2)
        mydb.commit()
    elif sensor=='ultrasonico':
        fecha=valores['fecha']
        valor=valores['distancia']
        val=(sensor,valor,fecha)
        mycursor.execute(sql, val)
        mydb.commit()


    

