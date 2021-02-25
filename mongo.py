import pymongo


mycliente=pymongo.MongoClient("mongodb://localhost:27017/")

db=mycliente['Sensores']


pir=db['pir']
dht11=db['dht11']
ultrasonico=db['ultrasonico']

def storeMongo(valores,sensor=''):
    if sensor=='pir':
        if valores['movimiento']=='Se detecta movimiento':
            pir.insert_one({
                'valor':valores['movimiento'],
                'fecha hora':valores['fecha']
            })
    elif sensor=='DHT11':
        dht11.insert_one({
            'Humedad':valores['humedad'],
            'Temperatura':valores['temp'],
            'fecha hora':valores['fecha']
        })
    elif sensor=='ultrasonico':
        ultrasonico.insert_one({
            'distancia':valores['distancia'],
            'fecha hora':valores['fecha']
        })
