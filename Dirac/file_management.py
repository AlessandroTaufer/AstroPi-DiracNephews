import logging


class WriteToFile:  # Write measures on the file
    def __init__(self, file, max_measures=10):
        self.file = file
        self.extension = ".txt"
        self.img_extension = ".jpg"
        self.file_id = 0  # Initial file number
        self.max_measures = max_measures
        self.current_measures = 0
        return

    def write_measure(self, measures):  # Write a new measure on the file
        # if self.is_full():  TODO complete
        #     self.erase_measure()
        self.refresh_file_id(measures[0].instant_values[0].time)
        file = open(self.file + str(self.file_id) + self.extension, "wb")
        for i in range(len(measures)):
            file.write(measures[i].to_string())
            # self.save_image(measures.get_images) TODO Uncomment that
            self.current_measures += 1
        logging.debug("Inserted measure")
        file.close()
        return

    def save_image(self, images): # Save the given images on the sd
        try:
            logging.debug("Saving image")
            images.save(self.file + str(self.file_id) + self.img_extension)
        except:
            logging.warning("An error has occured while saving the image")
        return

    def refresh_file_id(self, time):  # Create a new file id
        self.file_id = str(time)
