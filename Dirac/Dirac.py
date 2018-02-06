import time
import logging
import math
import event_recognition
#from sense_hat import SenseHat


def logging_setup():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def main():  # Main program
    #sense = SenseHat()
    sense = None  # Debug code
    logging_setup()
    backup_file = "file"
    trigger_value = input("Insert the debug threshold value\n")  # Debug code
    program = event_recognition.EventRecognition(sense, trigger_value, backup_file)
    program.recognize()


if "__main__" == __name__:
    main()
