import logging


class WriteToFile:  # Write measures on the file
    def __init__(self, file, max_measures=10):
        self.file = file
        self.extension = ".txt"
        self.img_extension = ".jpg"
        self.file_id = 0  # Initial file number
        self.max_measures = max_measures
        self.current_measures = 0

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

    def save_image(self, images):
        logging.debug("Saving image")
        images.save(self.file + str(self.file_id) + self.img_extension)
        return
    # def read(self):  # Reads all the file
    #     file = open(self.file, "rb")
    #     text = file.read()
    #     file.close()
    #     return text
    #
    # def read_line(self, row):  # Reads a file line
    #     file = open(self.file, "rb")
    #     for i in range(row):
    #         text = file.readLine()
    #     file.close()
    #     return text
    #
    # def measures_on_file(self):  # Counts the number of measures on the file
    #     txt = self.read()
    #     txt = txt.split("<-")
    #     return len(txt)

    # def is_full(self):  # Checks if the file has the max number of measures
    #     if self.measures_on_file > self.max_measures:
    #         logging.debug("File is full!")
    #         return True
    #     return False
    #     # return self.measures_on_file > self.max_measures

    # def worst_measure_on_file(self):  # Returns the measure with the lowest sum value - NOT WORKING
    #     worst = self.read(5)
    #     position = 1
    #     for i in range(1, self.max_measures+1):
    #         txt = self.read(i * 5)
    #         txt = txt.split(':')
    #         value = txt[1]
    #         if value < worst:
    #             worst = value
    #             position = i
    #     return position

    def refresh_file_id(self, time):
        self.file_id = str(time)

    # def erase_measure(self, new_measure):  # Delete a measure if the new measure is better
    #     logging.debug("Erasing a measure on the file")
    #     to_erase = self.worst_measure_on_file() * 7
    #     newfile = self.read().split('\n')
    #     newfile = newfile[:to_erase] + newfile[to_erase+7:]  # TODO Erase that
    #     txt = ""
    #     for i in range(len(newfile)):
    #         txt += newfile[i]
    #     file = open(self.file, "w")
    #     file.write(txt)
    #     file.close()
    #     return
