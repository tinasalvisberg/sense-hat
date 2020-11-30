#Mechatronik Einführung @HSLU
#Autorinnen: Sabrina Schmitz, Conny Troxler, Tina Salvisberg

from sense_hat import SenseHat
from time import sleep
from random import choice

sense = SenseHat()
sense.set_imu_config(False, True, False)  # gyroscope only

r = (255, 0, 0)  # red
b = (0, 0, 255)  # blue
g = (0, 255, 0)  # green
w = (255, 255, 255)  # white
y = (255, 255, 0)  # yellow
s = (0, 0, 0)  # Black
# Set up where each colour will display

def wuerfel():
    eins = [s, s, s, s, s, s, s, s,
        s, s, s, s, s, s, s, s,
        s, s, s, s, s, s, s, s,
        s, s, s, w, w, s, s, s,
        s, s, s, w, w, s, s, s,
        s, s, s, s, s, s, s, s,
        s, s, s, s, s, s, s, s,
        s, s, s, s, s, s, s, s]

    zwei = [s, s, s, s, s, s, s, s,
        s, s, s, s, s, w, w, s,
        s, s, s, s, s, w, w, s,
        s, s, s, s, s, s, s, s,
        s, s, s, s, s, s, s, s,
        s, w, w, s, s, s, s, s,
        s, w, w, s, s, s, s, s,
        s, s, s, s, s, s, s, s]

    drei = [s, s, s, s, s, s, s, s,
        s, s, s, s, s, w, w, s,
        s, s, s, s, s, w, w, s,
        s, s, s, w, w, s, s, s,
        s, s, s, w, w, s, s, s,
        s, w, w, s, s, s, s, s,
        s, w, w, s, s, s, s, s,
        s, s, s, s, s, s, s, s]

    vier = [s, s, s, s, s, s, s, s,
        s, w, w, s, s, w, w, s,
        s, w, w, s, s, w, w, s,
        s, s, s, s, s, s, s, s,
        s, s, s, s, s, s, s, s,
        s, w, w, s, s, w, w, s,
        s, w, w, s, s, w, w, s,
        s, s, s, s, s, s, s, s]

    five = [s, s, s, s, s, s, s, s,
        s, w, w, s, s, w, w, s,
        s, w, w, s, s, w, w, s,
        s, s, s, w, w, s, s, s,
        s, s, s, w, w, s, s, s,
        s, w, w, s, s, w, w, s,
        s, w, w, s, s, w, w, s,
        s, s, s, s, s, s, s, s]

    sechs = [s, w, w, s, s, w, w, s,
         s, w, w, s, s, w, w, s,
         s, s, s, s, s, s, s, s,
         s, w, w, s, s, w, w, s,
         s, w, w, s, s, w, w, s,
         s, s, s, s, s, s, s, s,
         s, w, w, s, s, w, w, s,
         s, w, w, s, s, w, w, s]

    augen = [eins, zwei, drei, vier, five, sechs]
    zahlen = choice(augen)
    sense.set_pixels(zahlen)
    sleep(12)
    sense.clear()

while True:
    orientation = sense.get_orientation_degrees()
    pitch = orientation.get("pitch")
    print(pitch)

    if 0 <= pitch <= 40 or 320 <= pitch <= 360:
        print("nichts tun")
    else:
        wuerfel()
