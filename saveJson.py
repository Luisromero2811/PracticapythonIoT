import json


data={}
data['pir']=[]
data['DHT11']=[]
data['ultrasonico']=[]

def storeJson(valores,sensor=''):
    if sensor=='pir':
        if valores['movimiento']=='Se detecta movimiento':
            data['pir'].append({
                'Valor':valores['movimiento'],
                'fecha hora':valores['fecha']
            })
        
    elif sensor=='DHT11':
        data['DHT11'].append({
            'humedad':valores['humedad'],
            'temperatura':valores['temp'],
            'fecha hora':valores['fecha']
        })
    elif sensor=='ultrasonico':
        data['ultrasonico'].append({
            'distancia':valores['distancia'],
            'fecha hora':valores['fecha']
        })
    
    with open('data.json','w') as file:
            json.dump(data,file, indent=4)



