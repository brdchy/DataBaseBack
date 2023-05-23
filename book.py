class Book: 

    def __init__(self, name: str, phone: int, time: str, notes:str):
        self.name = name
        self.phone = phone 
        self.time = time 
        self.notes = notes 

    def getInfo(self):
        return str(f"{self.name}:{self.phone}:{self.time}:{self.notes}")



