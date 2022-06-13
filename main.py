import paho.mqtt.client as mqtt
from geopy.geocoders import Nominatim
from flask import Flask, render_template
import folium
import smtplib,ssl

#def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
#   print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
#client.subscribe("digitest/test1")  # Subscribe to the topic “digitest/test1”, receive any messages published on it


#def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
 #   print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg


#client = mqtt.Client("digi_mqtt_test")  # Create instance of client with client ID “digi_mqtt_test”
#client.on_connect = on_connect  # Define callback function for successful connection
#client.on_message = on_message  # Define callback function for receipt of a message
#client.connect('127.0.0.1',17300,60) # Connect to (broker, port, keepalive-time)
#client.loop_forever()  # Start networking daemon

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "m.laroui@esi-sba.dz"
receiver_email = "m.bendaoud@esi-sba.dz"
password = "i love nfdk"
geolocator = Nominatim(user_agent="myapp")
location = geolocator.reverse("33.76326745, -84.39511726814364")
adr=location.address
print(adr)
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
 server.starttls(context=context)
#server.login(sender_email, password)
#server.sendmail(sender_email, receiver_email,adr)

m = folium.Map(location=[20,0], tiles="OpenStreetMap", zoom_start=2)
marker = folium.Marker(
    location=['33.76326745','-84.39511726814364'],popup=adr)
marker.add_to(m)

m.save('templates/map.html')
app = Flask(__name__)
@app.route('/')
def onclick():
 return render_template("frontend.html")

@app.route('/maplocation')
def maplocation():
  return render_template("map.html")

if __name__ == '__main__':
 app.run()
