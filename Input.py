class Input:
    def __init__(self, dayNr):
        self.dayNr = dayNr


    def lines(self):
        f = open('input' + str(self.dayNr) + '.txt', 'r')
        lines = f.readlines()
        f.close()
        return lines