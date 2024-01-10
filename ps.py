import dht
import machine
import time
import urequests

# Configuration du capteur DHT
pin_dht = 2  # GPIO 2 (D4)
sensor = dht.DHT11(machine.Pin(pin_dht))

# Configuration du réseau WiFi
ssid = "123456"
password = "izrw2424az"

# Configuration du serveur Django
server_address = "http://adresse_du_serveur_django/api/enregistrement/"

def connect_wifi():
    import network
    station = network.WLAN(network.STA_IF)
    if not station.isconnected():
        print("Connexion au WiFi en cours...")
        station.active(True)
        station.connect(ssid, password)
        while not station.isconnected():
            pass
    print("Connecté au WiFi")

def read_sensor_data():
    sensor.measure()
    humidity = sensor.humidity()
    temperature = sensor.temperature()
    return humidity, temperature

def send_data_to_django(humidity, temperature):
    url = f"{server_address}?humidity={humidity}&temperature={temperature}"
    response = urequests.get(url)
    print("Réponse du serveur:", response.text)
    response.close()

def main():
    connect_wifi()

    while True:
        humidity, temperature = read_sensor_data()
        print("Humidité:", humidity, "%")
        print("Température:", temperature, "°C")

        send_data_to_django(humidity, temperature)

        # Attendre un certain temps avant la prochaine lecture et envoi de données
        time.sleep(30)  # Attente d'une minute (ajustez selon vos besoins)

if __name__ == "__main__":
    main()
