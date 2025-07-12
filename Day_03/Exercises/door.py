class Door:
    def __init__(self, closed):
        self.closed = closed

    def open(self):
        self.closed = False

    def close(self):
        self.closed = True
        print ("Door is already closed")


