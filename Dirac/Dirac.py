import logging
import event_recognition
import screen_saver
from threading import Thread
#from sense_hat import SenseHat


def logging_setup():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def main():  # Main program
    #sense = SenseHat()
    sense = 1  # TODO Debug code
    Thread(target=screen_saver.project, args=(sense,)).start()
    logging_setup()
    backup_file = "file"
    trigger_value = input("Insert the debug threshold value\n")  # Debug code
    program = event_recognition.EventRecognition(sense, trigger_value, backup_file)
    program.recognize()


if "__main__" == __name__:
    main()
