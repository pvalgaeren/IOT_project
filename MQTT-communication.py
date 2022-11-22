import random
import time

from paho.mqtt import client as mqtt_client


broker = 'broker.empx.io'
port = 1883
topic = "python/mqtt"
# genereer willekeurig client-ID met pub-voorvoegsel
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'pi'
password = 'raspberry'


# Deze functie wordt aangeroepen nadat de client is verbonden en we kunnen 
# bepalen of de client succesvol is verbonden volgens rc in deze functie.
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


# Eerst definiëren we een while-lus. In deze lus zullen we de publicatiefunctie van de MQTT-client 
# instellen om elke seconde berichten naar het onderwerp python/mqtt te sturen.
def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


# Schrijf de bericht terugbelfunctie on_message. Deze functie wordt aangeroepen nadat de client berichten van de MQTT Broker heeft ontvangen.
# In deze functie printen we de naam van geabonneerde onderwerpen en de ontvangen berichten.
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message



def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()

