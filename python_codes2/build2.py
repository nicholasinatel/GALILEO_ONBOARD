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

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("$SYS/broker/clients/active")

def on_message(client, userdata, msg):
    print("Received message '"+str(msg.payload)+"'on topic '"+msg.topic+"' with Qos "+str(msg.qos))    

def on_publish(client, obj, mid):
    print("mid Publish EH  ->: "+str(mid))

def on_subscribe(client, userdata, mid, granted_qos):
	print("mid Subscribe EH  ->"+str(mid)+"   granted_qos eh   ->"+str(granted_qos))

def on_log(client, obj, level, string):
    print(" on log client eh  -> "+str(client))	

#Conecta no Iot Eclipse Org na Porta 1883 com Keep Alive = 60

client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe=on_subscribe
client.on_publish=on_publish

client.connect("iot.eclipse.org", 1883, 60)

client.loop_forever()
