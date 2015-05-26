import paho.mqtt.client as HERO
import time

#General Usage Flow
#Create Client Instance
client=HERO.Client("GALILEOPUBLISH", True, None)
#CALLBACK
def on_connect(client, userdata, flags, rc):
    print("===================================")
    print("Informacoes def on_connect")
    print("                                   ")
    print("Client    ="+str(client))
    print("                                   ")
    print("Userdata  ="+str(userdata))
    print("                                   ")
    print("Flags     ="+str(flags))
    print("                                   ")
    print("RC        ="+str(rc))                  #Result Code
    print("                                   ")
    print("                                   ")
    print("                                   ")
    print("===================================")
    client.publish("test/topic","VITAOOOOOOO_MALA_SEM_ALCA", 0, True)


def on_publish(client, obj, mid):
    print("===================================")
    print("Informacoes def on_publish")
    print("                                   ")
    print("mid  = "+str(mid))
    print("                                   ")
    print("===================================")  


client.on_connect=on_connect
client.on_publish=on_publish


#Connect to a broker using one of the connect*() functions
client.connect("iot.eclipse.org", 1883, 60)#Conecta no Iot Eclipse Org na Porta 1883 com Keep Alive = 60

s=0 # Variavel para segundos
m=0 # Variavel para minutos
mili=0 #Variavel para milisegundos

#Call one of the loop*() functions to maintain network traffic flow with the broker
client.loop_start()

while mili<=60:
     print m, 'Minutes', s, 'Seconds',mili, 'miliSeconds'
     time.sleep(0.001) #program stops for 1 second
     mili+=1
     client.publish("MINUTOS "+str(m),"     SEGUNDOS "+str(s) , "       MILISEGUNDOS "+str(mili), 0, False)
     if mili == 1000:
          s+=1
          
          #client.publish("test/topic" , "SEGUNDOS="+str(s), 0, False)
          mili=0
          if s == 60:
              m=m+1
              client.publish("MINUTO ehhh"+str(m))
              s=0
              mili=61

client.loop_stop(force=False)






