import logging
import event_recognition
import screen_saver
from threading import Thread
from sense_hat import SenseHat


def logging_setup(): # Setup basic logging configuration
    logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")


def main():  # Main program
    sense = SenseHat()
    Thread(target=screen_saver.project, args=(sense,)).start()
    logging_setup()
    backup_file = "logfile-"
    trigger_value = 300  # Estimated trigger value
    program = event_recognition.EventRecognition(sense, trigger_value, backup_file)
    program.recognize()


if "__main__" == __name__:
    main()
