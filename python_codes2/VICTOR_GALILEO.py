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
X=0
s=0
m=0

#Call one of the loop*() functions to maintain network traffic flow with the broker
client.loop_start()

while s<=60:
     print m, 'Minutes', s, 'Seconds'
     time.sleep(1) #program stops for 1 second
     s+=1
     client.publish("test/topic" , "SEGUNDOS="+str(s), 0, False)
     if s == 60:
          m+=1
          X+=1
          client.publish("test/topic" , "MINUTO="+str(s), 0, False)
          s=0
        if m == 60:
             m=0
             s=0
             client.loop_stop(False)






