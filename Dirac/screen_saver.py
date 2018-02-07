# from sense_hat import SenseHat
import time


def project(sense): # Project a screensaver on the led
    end = False
    sense.low_light = True

    O = (0, 0, 0)
    Z = (0, 127, 250)  # azzurro
    R = (255, 0, 0)  # rosso
    G = (255, 255, 0)  # giallo
    V = (0, 255, 0)  # verde

    terra = [
        Z, Z, Z, Z, Z, Z, Z, Z,
        Z, V, Z, Z, Z, Z, Z, Z,
        Z, V, V, Z, Z, V, V, Z,
        Z, V, V, V, V, V, V, Z,
        Z, V, V, V, V, Z, Z, Z,
        Z, V, V, Z, Z, Z, Z, Z,
        Z, V, Z, Z, Z, Z, Z, Z,
        Z, Z, Z, Z, Z, Z, Z, Z,
        Z, V, Z, Z, Z, Z, V, Z,
        Z, V, V, V, V, V, Z, Z,
        Z, V, V, V, V, Z, Z, Z,
        Z, V, V, V, V, V, Z, Z,
        Z, Z, V, Z, V, V, V, Z,
        Z, V, Z, V, V, Z, Z, Z,
    ]

    terra_1 = [
        O, O, Z, Z, Z, Z, O, O,
        O, Z, Z, Z, Z, Z, Z, O,
        Z, V, Z, Z, Z, Z, V, Z,
        Z, V, V, V, V, V, Z, Z,
        Z, V, V, V, V, Z, Z, Z,
        Z, V, V, V, V, V, Z, Z,
        O, Z, V, Z, V, V, V, O,
        O, O, Z, V, V, Z, O, O,
    ]

    terra_2 = [
        O, O, V, Z, Z, Z, O, O,
        O, V, Z, Z, Z, Z, Z, O,
        Z, Z, Z, Z, Z, Z, Z, Z,
        Z, V, Z, Z, Z, Z, V, Z,
        Z, V, V, V, V, V, Z, Z,
        Z, V, V, V, V, Z, Z, Z,
        O, V, V, V, V, V, Z, O,
        O, O, V, Z, V, V, O, O,
    ]

    terra_3 = [
        O, O, V, V, V, Z, O, O,
        O, V, V, Z, Z, Z, Z, O,
        Z, V, Z, Z, Z, Z, Z, Z,
        Z, Z, Z, Z, Z, Z, Z, Z,
        Z, V, Z, Z, Z, Z, V, Z,
        Z, V, V, V, V, V, Z, Z,
        O, V, V, V, V, Z, Z, O,
        O, O, V, V, V, V, O, O,
    ]

    terra_4 = [
        O, O, V, V, V, V, O, O,
        O, V, V, V, V, Z, Z, O,
        Z, V, V, Z, Z, Z, Z, Z,
        Z, V, Z, Z, Z, Z, Z, Z,
        Z, Z, Z, Z, Z, Z, Z, Z,
        Z, V, Z, Z, Z, Z, V, Z,
        O, V, V, V, V, V, Z, O,
        O, O, V, V, V, Z, O, O,
    ]

    terra_5 = [
        O, O, V, Z, Z, V, O, O,
        O, V, V, V, V, V, V, O,
        Z, V, V, V, V, Z, Z, Z,
        Z, V, V, Z, Z, Z, Z, Z,
        Z, V, Z, Z, Z, Z, Z, Z,
        Z, Z, Z, Z, Z, Z, Z, Z,
        O, V, Z, Z, Z, Z, V, O,
        O, O, V, V, V, V, O, O,
    ]

    terra_6 = [
        O, O, Z, Z, Z, Z, O, O,
        O, V, V, Z, Z, V, V, O,
        Z, V, V, V, V, V, V, Z,
        Z, V, V, V, V, Z, Z, Z,
        Z, V, V, Z, Z, Z, Z, Z,
        Z, V, Z, Z, Z, Z, Z, Z,
        O, Z, Z, Z, Z, Z, Z, O,
        O, O, Z, Z, Z, Z, O, O,
    ]

    terra_7 = [
        O, O, Z, Z, Z, Z, O, O,
        O, V, Z, Z, Z, Z, Z, O,
        Z, V, V, Z, Z, V, V, Z,
        Z, V, V, V, V, V, V, Z,
        Z, V, V, V, V, Z, Z, Z,
        Z, V, V, Z, Z, Z, Z, Z,
        O, V, Z, Z, Z, Z, Z, O,
        O, O, Z, Z, Z, Z, O, O,
    ]

    terra_8 = [
        O, O, Z, V, V, Z, O, O,
        O, Z, Z, Z, Z, Z, Z, O,
        Z, V, Z, Z, Z, Z, Z, Z,
        Z, V, V, Z, Z, V, V, Z,
        Z, V, V, V, V, V, V, Z,
        Z, V, V, V, V, Z, Z, Z,
        O, V, V, Z, Z, Z, Z, O,
        O, O, Z, Z, Z, Z, O, O,
    ]

    terra_9 = [
        O, O, V, Z, V, V, O, O,
        O, V, Z, V, V, Z, Z, O,
        Z, Z, Z, Z, Z, Z, Z, Z,
        Z, V, Z, Z, Z, Z, Z, Z,
        Z, V, V, Z, Z, V, V, Z,
        Z, V, V, V, V, V, V, Z,
        O, V, V, V, V, Z, Z, O,
        O, O, V, Z, Z, Z, O, O,
    ]

    terra_10 = [
        O, O, V, V, V, V, O, O,
        O, Z, V, Z, V, V, V, O,
        Z, V, Z, V, V, Z, Z, Z,
        Z, Z, Z, Z, Z, Z, Z, Z,
        Z, V, Z, Z, Z, Z, Z, Z,
        Z, V, V, Z, Z, V, V, Z,
        O, V, V, V, V, V, V, O,
        O, O, V, V, V, Z, O, O,
    ]

    terra_11 = [
        O, O, V, V, V, Z, O, O,
        O, V, V, V, V, V, Z, O,
        Z, Z, V, Z, V, V, V, Z,
        Z, V, Z, V, V, Z, Z, Z,
        Z, Z, Z, Z, Z, Z, Z, Z,
        Z, V, Z, Z, Z, Z, Z, Z,
        O, V, V, Z, Z, V, V, O,
        O, O, V, V, V, V, O, O,
    ]

    terra_12 = [
        O, O, V, V, V, V, O, O,
        O, V, V, V, V, Z, Z, O,
        Z, V, V, V, V, V, Z, Z,
        Z, Z, V, Z, V, V, V, Z,
        Z, V, Z, V, V, Z, Z, Z,
        Z, Z, Z, Z, Z, Z, Z, Z,
        O, V, Z, Z, Z, Z, Z, O,
        O, O, V, Z, Z, V, O, O,
    ]

    terra_13 = [
        O, O, Z, Z, Z, Z, O, O,
        O, V, V, V, V, V, Z, O,
        Z, V, V, V, V, Z, Z, Z,
        Z, V, V, V, V, V, Z, Z,
        Z, Z, V, Z, V, V, V, Z,
        Z, V, Z, V, V, Z, Z, Z,
        O, Z, Z, Z, Z, Z, Z, O,
        O, O, Z, Z, Z, Z, O, O,
    ]

    terra_14 = [
        O, O, Z, Z, Z, Z, O, O,
        O, V, Z, Z, Z, Z, V, O,
        Z, V, V, V, V, V, Z, Z,
        Z, V, V, V, V, Z, Z, Z,
        Z, V, V, V, V, V, Z, Z,
        Z, Z, V, Z, V, V, V, Z,
        O, V, Z, V, V, Z, Z, O,
        O, O, Z, Z, Z, Z, O, O,
    ]

    while not end:
        sense.set_pixels(terra_1)
        time.sleep(1)
        sense.set_pixels(terra_2)
        time.sleep(1)
        sense.set_pixels(terra_3)
        time.sleep(1)
        sense.set_pixels(terra_4)
        time.sleep(1)
        sense.set_pixels(terra_5)
        time.sleep(1)
        sense.set_pixels(terra_6)
        time.sleep(1)
        sense.set_pixels(terra_7)
        time.sleep(1)
        sense.set_pixels(terra_8)
        time.sleep(1)
        sense.set_pixels(terra_9)
        time.sleep(1)
        sense.set_pixels(terra_10)
        time.sleep(1)
        sense.set_pixels(terra_11)
        time.sleep(1)
        sense.set_pixels(terra_12)
        time.sleep(1)
        sense.set_pixels(terra_13)
        time.sleep(1)
        sense.set_pixels(terra_14)
        time.sleep(1)
