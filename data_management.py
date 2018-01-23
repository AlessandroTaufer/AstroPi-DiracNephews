import logging
import math


class Chunk:
    def __init__(self, x, y, z, time):
        self.x = x
        self.y = y
        self.z = z
        self.time = time
        self.average = math.sqrt(x**2 + y**2 ++ z**2)
        logging.debug("Created a chunk with x: " + str(x) + " y:" + str(y) + " z:" + str(z) + "at time: " + str(time) )
        return


    def to_string(self):
        x = bin(val if val>0 else val+(1<8))
        y = bin(val if val>0 else val+(1<8))
        z = bin(val if val>0 else val+(1<8))
        
        return "x: " + str(self.x)+" y: "+str(self.y)+" z: "+str(self.z)+" time: "+str(self.time)+"\n"

    

class Measure:
    def __init__(self, c0=False, c1=False, c2=False):
        self.chunks = [c0, c1, c2]  # Chunk vector
        self.chunks_sum = self.sum()
        return

    def insert_chunk(self, x, y, z, time):  # Insert a chunk in the measure
        for i in range(len(self.chunks)):
            if not self.chunks[i]:
                self.chunks[i] = Chunk(x, y, z, time)
                logging.debug("Inserted chunk in measure object")
                return True
        logging.warn("Failed to create chunk")
        return False

    def sum(self):
        sum = 0
        for i in range(len(self.chunks)):
            if self.chunks[i] is not False:
                sum += self.chunks[i].average
            return sum
        return False

    def to_string(self):  # Print the sequence of measurement
        line = "<---------------------------------------------------------------------------------------->"+"\n"
        for i in range(len(self.chunks)):
            line = self.chunks[i].to_string()
            logging.debug("Inserted measure on file")
        line += "Ctot" + str(self.sum()) + "\n"
        line += "*----------------------------------------------------------------------------------------*"+"\n"
        logging.debug("Inserted measure")
        return line
