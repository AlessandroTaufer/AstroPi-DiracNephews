import time
import logging
import math
import event_recognition
#from sense_hat import SenseHat


def main():
    #sense = SenseHat()
    sense = None
    backup_file = "file.txt"
    trigger_value = 1000
    program = event_recognition.EventRecognition(sense, trigger_value, backup_file)
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    program.recognize()


if "__main__" == __name__:
    main()

