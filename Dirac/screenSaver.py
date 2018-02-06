# from sense_hat import SenseHat
import time

end = False

sense = SenseHat()

sense.low_light = True

O = (0, 0, 0)   
Z = (0, 127,250)	       #azzurro		
R = (255, 0, 0)		       #rosso
G = (255,255, 0)			#giallo
V = (0, 255, 0)			#verde

terra_1 = [
        O, O, V, V, V, V, O, O,
	O, Z, V, V, V, V, V, O,
	Z, Z, Z, V, V, V, V, Z,
	Z, Z, Z, Z, Z, V, Z, Z,
	Z, Z, V, V, Z, Z, Z, Z,
	Z, Z, V, V, V, Z, Z, Z,
	O, V, V, V, V, V, Z, O,
	O, O, V, V, V, Z, O, O,
    ]

terra_2 = [
        O, O, V, V, V, V, O, O,
	O, Z, Z, V, V, V, V, O,
	Z, Z, Z, Z, Z, V, Z, Z,
	Z, Z, V, V, Z, Z, Z, Z,
	Z, Z, V, V, V, Z, Z, Z,
	Z, V, V, V, V, V, Z, Z,
	O, V, V, V, V, Z, Z, O,
	O, O, V, V, V, Z, O, O,
    ]

while not end:
    sense.set_pixels(terra_1)
    time.sleep(2)
    sense.set_pixels(terra_2)
    time.sleep(2)
    
    

    
