class Table:

    def __init__(self, numbertable, is_booked = False):

        self.numbertable = numbertable
        self.is_booked = is_booked

    def getInfo(self):
        return str(f"{self.numbertable}:{self.is_booked}")
