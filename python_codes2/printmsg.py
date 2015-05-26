import paho.mqtt.client as mqtt
import time
 
#Global Stuff
Flag=0
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
   print("Connected with result code CONNACK FUNFOU"+str(rc))
#Tell python to look at the global variable Flag
global Flag
Flag=1
# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.

 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
  print(msg.topic+": "+str(msg.payload))
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.subscribe("#")
 
client.connect("test.mosquitto.org", 1883, 60)
 
#Start Loop
client.loop_start()


 
try:
  while True:
      if(Flag==1):
         print 'The Flag was set! Woohoo!'
         def on_message(client, userdata, msg):
  print(msg.topic+": "+str(msg.payload))
         time.sleep(10)
         Flag=0
      print 'FAZENDO ALGO AQUI'
      print 'ZZZZZzzzzzzz dormindo denovo por time.sleep30'
      time.sleep(30)
except:
    print 'I made a boo boo'
finally:
    print 'All Clean up Now'
    client.loop_stop()
    # GPIO.cleanup() anyone?