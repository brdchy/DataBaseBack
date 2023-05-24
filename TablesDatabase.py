
class TablesDatabase:

    def __init__(self, db_name):
        self.db_name = db_name
        self.db_file = open(db_name, "a+")


    def unload_tables(self): # выгрузка столов
        b = ""
        with open(self.db_name, "r") as file:
            for line in file:
                b += str(line) 

        return b