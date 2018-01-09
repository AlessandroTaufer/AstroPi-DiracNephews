import time
import logging
import math
from sense_hat import SenseHat


def main():
    sense = SenseHat()
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    for i in range(100):
        print(sense.compass_raw)
        time.sleep(1)


if "__main__" == __name__:
    main()

