#Mechatronik Einführung @HSLU
#authors: Sabrina Schmitz, Conny Troxler, Tina Salvisberg

from sense_hat import SenseHat
from time import sleep
import random

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
scoreone = -1
scoretwo = -1

def wuerfel(player):
    zahlen = random.randint(0, 5)
    sense.set_pixels(player[zahlen])
    sleep(6)
    sense.clear()
    return zahlen

def winner(scoreone, scoretwo):
    #if scoreone < scoretwo:
        #spieler zwei gewinnt
    #elif scoreone > scoretwo:
        #sense.show_message("win white", text_colour=w, scroll_speed=0.05)
    #else:
        #unentschieden
    return "Spieler 1"

while True:
    #TODO: state machine
    if state == 1:
        player = one
        orientation = sense.get_orientation_degrees()
        pitch = orientation.get("pitch")

        if 0 <= pitch <= 40 or 320 <= pitch <= 360:
            sense.clear(w)
        else:
            scoreone = wuerfel(player)
            state += 1

    elif state == 2:
        player = two
        orientation = sense.get_orientation_degrees()
        pitch = orientation.get("pitch")

        if 0 <= pitch <= 40 or 320 <= pitch <= 360:
            sense.clear(g)
        else:
            scoretwo = wuerfel(player)
            state += 1

    elif state == 3:
        player = one
        won = winner(scoreone, scoretwo)
        print(won)

    else:
        print("ungültiger Status")