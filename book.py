class Book: 

    def __init__(self, name: str, phone: int, table: str, time: str, notes: str):
        self.name = name
        self.phone = phone 
        self.table = table
        self.time = time 
        self.notes = notes 

    def getInfo(self):
        return str(f"{self.name}:{self.phone}:{self.table}:{self.time}:{self.notes}")



