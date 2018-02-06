import logging
import math


class InstantValue:  # Magnetometer measure on a given time
    def __init__(self, x, y, z, time):
        self.x = x
        self.y = y
        self.z = z
        self.time = time
        self.img = None
        self.average = math.sqrt(x**2 + y**2 + z**2)
        logging.debug("Created a chunk with x: " + str(x) + " y:" + str(y) + " z:" + str(z) + "at time: " + str(time))
        return

    def to_string(self):
        return str(self.x)+" "+str(self.y)+" "+str(self.z)+" "+str(self.time)+"\n"

    def to_byte(self):
        pass


class Chunk:  # InstantValues collection
    def __init__(self, c0=False, c1=False, c2=False):
        self.instant_values = [c0, c1, c2]  # Chunk vector
        self.chunk_sum = self.sum()
        return

    def insert_instant_value(self, x, y, z, time):  # Insert a chunk in the measure
        for i in range(len(self.instant_values)):
            if not self.instant_values[i]:
                self.instant_values[i] = InstantValue(x, y, z, time)
                logging.debug("Inserted instant value in chunk object")
                return True
        logging.warn("Failed to create chunk")
        return False

    def sum(self):
        sum = 0
        for i in range(len(self.instant_values)):
            if self.instant_values[i] is not False:
                sum += self.instant_values[i].average
            else:
                return False
        self.chunk_sum = sum
        return sum

    def to_string(self):  # Print the sequence of measurement
        line = str(self.sum())+"\n"
        for i in range(len(self.instant_values)):
            line += self.instant_values[i].to_string()
            # logging.debug("Inserted measure on file")
        line += "\n\n"
        logging.debug("Inserted measure on file")
        return line

    def to_byte(self):
        pass

    def get_images(self):  # Return all the images of the chunk
        images = []
        for i in range(len(self.instant_values)):
            images.append(self.instant_values[i].img)
        return images