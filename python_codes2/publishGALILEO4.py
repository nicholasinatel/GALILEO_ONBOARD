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
    X=0
    for i in [1,2,3,4,5,6,7,8,9,10]:
    	X=X+1
    	client.publish("test/topic","CONTADOR  ="+str(X), 0, False)
    	time.sleep(15)
    	continue
    	break

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


#Call one of the loop*() functions to maintain network traffic flow with the broker
client.loop_forever()    




