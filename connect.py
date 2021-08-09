from decimal import Decimal
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from datetime import datetime
import random

def helloworld(self, params, packet):
    print("Received message ")
    print(packet.topic)
    print(packet.payload)

myMQTTClient = AWSIoTMQTTClient("TestID") #random key, if another connection using the same key is opened the previous one is auto closed by AWS IOT
myMQTTClient.configureEndpoint("a2co28axseooi0-ats.iot.us-east-1.amazonaws.com", 8883)

myMQTTClient.configureCredentials("root.pem", "private.pem.key", "certificate.pem.crt")

myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
print ('Initiating Realtime Data Transfer From Raspberry Pi...')
myMQTTClient.connect()
# myMQTTClient.subscribe('iot/topic',1,helloworld)

# while True:
#     time.sleep(5)

while True:
    data = random.randint(10,100)
    print("Publish Data From Raspberry Pi: "+str(data))
    now=datetime.now()
    myMQTTClient.publish(
        topic='iot/topic',
        QoS=1,
        payload='{"river":"Narayani","location" : "Chitwan", "level" : "'+str(data)+'", "created_at" : "'+str(now)+'"}'
    )
    time.sleep(5)
