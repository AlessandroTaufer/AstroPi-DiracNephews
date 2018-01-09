import time
import logging
import math
from sense_hat import SenseHat




class EventRecognition:  # Takes measures and looks for events
    def __init__(self, sense, trigger):
        self.sense = sense
        self.trigger = trigger
        self.measures = []

    def get_measure(self):
        pass

    def check_measure(self):
        pass

    def save_measure(self):
        pass


def main():
    sense = SenseHat()
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    for i in range(100):
        print(sense.compass_raw)
        time.sleep(1)


if "__main__" == __name__:
    main()

