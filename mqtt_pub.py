import paho.mqtt.client as mqtt

pub_client=mqtt.Client()
pub_client.connect('Broker.hivemq.com',1883)
print('Broker connected')

pub_client.publish('gpcet/ai','pavan sunny............................')
