
import redis
import os
import time

r = redis.StrictRedis( host=os.environ['REDIS_HOST'], port=6379, db=0)

redis_ready = False

#intenta hasta que este listo el contenedor
while not redis_ready:
    try:
        redis_ready = r.ping()
    except:
        print("waiting for redis")
        time.sleep(3)

print("setup: redis alive")

#lista de palabras
colores = ['rojo','verde','azul','amarillo']

#foreach
for color in colores:
 
    r.lpush('cola_de_mensajes', color )

print('colores enviados')
    