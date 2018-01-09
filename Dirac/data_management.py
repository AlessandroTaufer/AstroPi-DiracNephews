class Chunk:
    def __init__(self, x, y, z, time):
        self.x = x
        self.y = y
        self.z = z
        self.time = time
        logging.debug("Created a chunk with x: " + str(x) + " y:" + str(y) + " z:" + str(z) + "at time: " + str(time) )
        return


class Measure:
    def __init__(self, c0=False, c1=False, c2=False):
        self.chunks = [c0, c1, c2]  # Chunk vector
        self.chunks_sum = self.sum()
        return

    def insert_chunk(self, x, y, z, time):  # Insert a chunk in the measure
        for i in range(len(self.chunks)):
            if not self.chunks[i]:
                self.chunks[i] = Chunk(x, y, z, time)
                logging.debug("Inserted chunk")
                return True
        logging.warn("Failed to create chunk")
        return False

    def sum(self): 
        sum = 0
        for i in range(len(self.chunks)):
            if self.chunks[i] is not False:
                sum += self.chunks[i]
            return sum
        return False

    def to_string(self): #Print the sequence of measurement
        self.line = "------------------------------------------------------------------------------------------"
        for i in range(len(self.chunks)):
            if not self.chunks[i] = 0:
                self.line += "x:"+ str(x)+"y:"+str(y)+"z:"+str(z)+"time:"+str(time)+"\n"
                logging.debug("Inserted measure")
        self.line += "Ctot"+ str(sum())+"\n"
        self.line += "------------------------------------------------------------------------------------------"+"\n"
        logging.debug("Inserted measure")    
        return self.line
