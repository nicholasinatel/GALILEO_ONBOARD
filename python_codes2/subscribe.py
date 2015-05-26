import paho.mqtt.client as HERO
import time

#Nicholas Paolillo codigo feito em 23/03/2015 em python
#General Usage Flow
#Create Client Instance
#Connect to a broker using one of the connect*() functions
#Call one of the loop*() functions to maintain network traffic flow with the broker
#Use subcribe() to subscribe to a topic and receibe messages
#Use publish() to publish messages to the broker
#Use disconnect() to disconnect from the broker


#Programacao orientada ao objeto dar uma estudada
client=HERO.Client("INATElEMBARCADO", True, None)

def on_connect(client, userdata, flags, rc):
    print("Conectado com codigo do CONNACK ==   "+str(rc))
    client.subscribe("$SYS/broker/clients/total")


def on_message(client, userdata, msg):
    print("Msg recebida->"+str(msg.payload)+"Numero de clientes conectados no Topico ->  "+msg.topic+" com Qos "+str(msg.qos))    

#def on_subscribe(client, userdata, mid, granted_qos):
#	print("mid eh->"+str(mid)+"   granted_qos eh->"+str(granted_qos))

#Conecta no Iot Eclipse Org na Porta 1883 com Keep Alive = 60

client.on_connect = on_connect
client.on_message = on_message
#client.on_subscribe=on_subscribe

client.connect("iot.eclipse.org", 1883, 60)

client.loop_forever()
