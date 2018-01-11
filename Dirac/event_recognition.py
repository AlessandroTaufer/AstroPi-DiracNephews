import data_management
import file_management
import datetime
import logging
import time


class EventRecognition:  # Takes measures and looks for events
    def __init__(self, sense, trigger, backup_file):
        self.file_manager = file_management.WriteToFile(backup_file)  # Object that manage files
        self.sense = sense  # RaspberryPi SenseHat object
        self.trigger = trigger  # Event trigger value
        self.measures = []  # All taken measures
        self.measures_lapse = 1

    def get_measure(self):  # Takes a measure and returns it
        measure = data_management.Measure()
        for i in range(3):  # Inserts all 3 chunks in the measure
            logging.debug("Inserting a new chunk in the measure")
            x, y, z, time = self.read_compass()
            measure.insert_chunk(x, y, z, time)
        return measure

    def read_compass(self):  # Returns compass value and current time
        raw_data = self.sense.compass_raw
        x = raw_data.get('x')
        y = raw_data.get('y')
        z = raw_data.get('z')
        time = datetime.datetime.time(datetime.datetime.now())  # Gets current time
        logging.debug("Compass value(xyz): " + x + " " + y + " " + z + "  at" + time)
        return x, y, z, time

    def check_measure(self, measure):  # Checks if the measure has spotted and event
        if measure.sum() > self.trigger:
            logging.debug("Measure exceeds trigger")
            return True
        return

    def save_measure(self, measure): # Saves a measure on the file
        logging.debug("Saving data on file")
        self.file_manager.write(measure)
        return

    def recognize(self):  # Recognize an event and saves measures
        logging.debug("Starting recognizing event method")
        stop = False
        last_measure = 0
        while not stop:
            self.measures.append(self.get_measure())
            if self.measures[last_measure]:
                self.save_measure(self.measures[last_measure])
            last_measure += 1
            time.sleep(self.measures_lapse)
        return
