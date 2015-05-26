import paho.mqtt.client as HERO
import time

#General Usage Flow
#Create Client Instance
#Connect to a broker using one of the connect*() functions
#Call one of the loop*() functions to maintain network traffic flow with the broker
#Use subcribe() to subscribe to a topic and receibe messages
#Use publish() to publish messages to the broker
#Use disconnect() to disconnect from the broker

#Programacao orientada ao objeto dar uma estudada
client=HERO.Client("INATElEMBARCADO", True, None)
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
    #client.subscribe("$SYS/broker/clients/active")
    client.publish("test/topic","MESSAGE INAHELL", 0, True)
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print("===================================")
    print("Informacoes def on_connect")
    print("                                   ")
    print("Received message '"+str(msg.payload))
    print("                                   ")
    print("'on topic '"+msg.topic)
    print("                                   ")
    print("' with Qos "+str(msg.qos))  
    print("                                   ") 
    print("===================================") 
		
def on_publish(client, obj, mid):
    print("===================================")
    print("Informacoes def on_publish")
    print("                                   ")
    print("mid  = '"+str(mid))
    print("                                   ")
    print("===================================")

def on_subscribe(client, userdata, mid, granted_qos):
    print("===================================")
    print("Informacoes def on_subscribe")
    print("                                   ")
    print("mid Subscribe ="+str(mid))
    print("                                   ")
    print("granted_qos   ="+str(granted_qos))
    print("                                   ")
    print("===================================")




client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe=on_subscribe
client.on_publish=on_publish

client.connect("iot.eclipse.org", 1883, 60)     #Conecta no Iot Eclipse Org na Porta 1883 com Keep Alive = 60

client.loop_forever()
