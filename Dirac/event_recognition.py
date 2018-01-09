import data_management
import file_management
import datetime
import logging

class EventRecognition:  # Takes measures and looks for events
    def __init__(self, sense, trigger, backup_file):
        self.file_manager = file_management.WriteToFile(backup_file)  # Object that manage files
        self.sense = sense  # RaspberryPi SenseHat object
        self.trigger = trigger  # Event trigger value
        self.measures = []  # All taken measures

    def get_measure(self):  # Takes a measure and returns it
        measure = data_management.Measure()
        for i in range(3):  # Inserts all 3 chunks in the measure
            raw_data = self.sense.compass_raw
            x = raw_data.get('x')
            y = raw_data.get('y')
            z = raw_data.get('z')
            time = datetime.datetime.time(datetime.datetime.now())  # Gets current time
            logging.debug("Inserting a new chunk in the measure")
            measure.insert_chunk(x, y, z, time)
        return measure

    def check_measure(self, measure):  # Checks if the measure has spotted and event
        return measure.sum() > self.trigger

    def save_measure(self, measure):
        logging.debug("Saving data on file")
        self.file_manager.write(measure)
        return
