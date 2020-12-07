#Mechatronik Einführung @HSLU
#authors: Sabrina Schmitz, Conny Troxler, Tina Salvisberg

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
s = (0, 0, 0)  # black

#dice player one
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

fuenf = [s, s, s, s, s, s, s, s,
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

#dice player two
einsA = [s, s, s, s, s, s, s, s,
        s, s, s, s, s, s, s, s,
        s, s, s, s, s, s, s, s,
        s, s, s, g, g, s, s, s,
        s, s, s, g, g, s, s, s,
        s, s, s, s, s, s, s, s,
        s, s, s, s, s, s, s, s,
        s, s, s, s, s, s, s, s]

zweiA = [s, s, s, s, s, s, s, s,
        s, s, s, s, s, g, g, s,
        s, s, s, s, s, g, g, s,
        s, s, s, s, s, s, s, s,
        s, s, s, s, s, s, s, s,
        s, g, g, s, s, s, s, s,
        s, g, g, s, s, s, s, s,
        s, s, s, s, s, s, s, s]

dreiA = [s, s, s, s, s, s, s, s,
        s, s, s, s, s, g, g, s,
        s, s, s, s, s, g, g, s,
        s, s, s, g, g, s, s, s,
        s, s, s, g, g, s, s, s,
        s, g, g, s, s, s, s, s,
        s, g, g, s, s, s, s, s,
        s, s, s, s, s, s, s, s]

vierA = [s, s, s, s, s, s, s, s,
        s, g, g, s, s, g, g, s,
        s, g, g, s, s, g, g, s,
        s, s, s, s, s, s, s, s,
        s, s, s, s, s, s, s, s,
        s, g, g, s, s, g, g, s,
        s, g, g, s, s, g, g, s,
        s, s, s, s, s, s, s, s]

fuenfA = [s, s, s, s, s, s, s, s,
        s, g, g, s, s, g, g, s,
        s, g, g, s, s, g, g, s,
        s, s, s, g, g, s, s, s,
        s, s, s, g, g, s, s, s,
        s, g, g, s, s, g, g, s,
        s, g, g, s, s, g, g, s,
        s, s, s, s, s, s, s, s]

sechsA = [s, g, g, s, s, g, g, s,
         s, g, g, s, s, g, g, s,
         s, s, s, s, s, s, s, s,
         s, g, g, s, s, g, g, s,
         s, g, g, s, s, g, g, s,
         s, s, s, s, s, s, s, s,
         s, g, g, s, s, g, g, s,
         s, g, g, s, s, g, g, s]

one = [eins, zwei, drei, vier, fuenf, sechs]
two = [einsA, zweiA, dreiA, vierA, fuenfA, sechsA]

state = 1
player = one
scoreone = 0
scoretwo = 2

def wuerfel(player):
    #TODO: set random with number
    # random.randint(0,5)
    zahlen = choice(player)
    sense.set_pixels(zahlen)
    sleep(6)
    sense.clear()
    return 5

#def winner(scoreone, scoretwo):
    #if scoreone < scoretwo:
        #spieler zwei gewinnt
    #elif scoreone > scoretwo:
        #sense.show_message("win white", text_colour=w, scroll_speed=0.05)
    #else:
        #unentschieden

while True:
    #TODO: state machine
    orientation = sense.get_orientation_degrees()
    pitch = orientation.get("pitch")
    #print(pitch)

    if 0 <= pitch <= 40 or 320 <= pitch <= 360:
        print("nichts tun")
        #TODO: display color of player
    else:
        scoreone = wuerfel(player)
        print(scoreone)