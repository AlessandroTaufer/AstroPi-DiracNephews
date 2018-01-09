class WriteToFile:  # Write measures on the file
    def __init__(self, file):
        self.file = file
        
        

    def write(self, measure): # Write a new measure on the file
        pass measure
        file = open (self.file,"w")
        file.write(measure.to_string())
        logging.debug("Inserted measure")
        file.close()
        
        
    def read(self):
        text = " "
        file = open (self.file ,"r")
        text = file.read()
        file.close()
