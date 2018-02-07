import data_management
import file_management
import datetime
import logging
import time
import io
# import picamera
from PIL import Image
from threading import Thread


class EventRecognition:  # Takes measures and looks for events
    def __init__(self, sense, threshold, backup_file):
        self.file_manager = file_management.WriteToFile(backup_file)  # Object that manage files
        self.sense = sense  # RaspberryPi SenseHat object
        self.threshold = threshold  # Event trigger value
        logging.debug("Current threshold: " + str(threshold))
        self.chunks = []  # All taken measures
        self.chunks_lapse = 1  # Time between two chunks
        self.stop = False

    def get_chunk(self):  # Takes a chunk measure and returns it
        chunk = data_management.Chunk()
        logging.debug("Inserting a new chunk in the measure")
        for i in range(3):  # Inserts all 3 chunks in the measure
            x, y, z, current_time = self.read_compass()
            chunk.insert_instant_value(x, y, z, current_time)
        return chunk

    # def read_compass(self):  # Returns compass value and current time
    #     raw_data = self.sense.compass_raw
    #     x = raw_data.get('x')
    #     y = raw_data.get('y')
    #     z = raw_data.get('z')
    #     current_time = datetime.datetime.time(datetime.datetime.now())  # Gets current time
    #     logging.debug("Compass value(xyz): " + x + " " + y + " " + z + "  at" + str(current_time))
    #     self.capture_image() TODO Uncomment that
    #     return x, y, z, current_time

    def read_compass(self):  # Debug method
        time.sleep(0.5)
        x = input("Insert x value:")
        y = input("Insert y value:")
        z = input("Insert z value:")
        current_time = datetime.datetime.time(datetime.datetime.now())  # Gets current time
        return x, y, z, current_time

    def event_finder(self):  # Checks if the measures countains an event
        logging.debug("Starting event finder")
        # try:
        for i in range(len(self.chunks)-1):
            if self.chunks[i].sum() > self.threshold:
                self.threshold = self.chunks[i].sum()
                logging.debug("Found and event!")
                self.save_measure((self.chunks[i-1], self.chunks[i], self.chunks[i+1]))
            if i > 0:
                self.chunks.pop(i-1)
                logging.debug("Erased a old chunk")
            time.sleep(self.chunks_lapse)
        # except:
        #     logging.warning("And error occured during the event finder ")
        #     logging.debug("Blocked event finder loop")
        return

    def save_measure(self, measures_set):  # Saves a set of measures on the file
        logging.debug("Saving data on file")
        self.file_manager.write_measure(measures_set)
        return

    def recognize(self):  # Recognize an event and saves measures
        logging.debug("Starting recognizing event method")
        self.acquire_measures_loop()
        # self.event_finder()
        return

    def acquire_measures_loop(self):  # Acquires measures repeatedly
        logging.debug("Initializing acquire measure loop")
        i = 0
        while not self.stop:
            # try:
            if i >= 3:
                # Thread(self.event_finder).start()
                Thread(target=self.event_finder).start()
            self.chunks.append(self.get_chunk())
            time.sleep(self.chunks_lapse)
            i += 1
            # except:
            #     logging.warning("An error occured during the acquire measure loop")
        logging.debug("Blocked measure loop")
        return

    def capture_image(self):  # Capture an image and returns it
        logging.debug("Getting an image")
        stream = io.BytesIO()
        with picamera.PiCamera() as camera:
            camera.capture(stream, format='jpeg')
        stream.seek(0) # Rewind the stream
        image = Image.open(stream)
        return image