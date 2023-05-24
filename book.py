class Book: 

    def __init__(self, name: str, phone: int, date: str, time: str, numbertable: str, notes: str):
        self.name = name
        self.phone = phone 
        self.date = date
        self.time = time 
        self.numbertable = numbertable
        self.notes = notes 

    def getInfo(self):
        return str(f"{self.name}:{self.phone}:{self.date}:{self.time}:{self.numbertable}:{self.notes}")



