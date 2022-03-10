from geopy.geocoders import Nominatim
from flask import Flask, render_template
import folium
import smtplib,ssl
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
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email,adr)
m = folium.Map(location=[20,0], tiles="OpenStreetMap", zoom_start=2)
marker = folium.Marker(
    location=['33.76326745','-84.39511726814364'],popup=adr)
marker.add_to(m)

m.save('templates/map.html')
app = Flask(__name__)
@app.route("/")
def maplocation():
    return render_template("map.html")
if __name__ == '__main__':
    app.run()
