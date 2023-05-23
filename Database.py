import user

class Database: 

    def __init__(self, db_name):
        self.db_name = db_name
        self.db_file = open(db_name, "a+")

    def write(self, user: user): # возможность записи

        self.db_file.write(f"{user.getInfo()}")
        self.db_file.write("\n")

    def read_all(self): # возможность чтения
        self.db_file.seek(0)
        return self.db_file.readlines()

    def searchfor(self, value: str) -> bool:
        flag=0
        with open(self.db_name) as f:
                for i in f:
                    if (f"{value}") in i:
                        flag+=1
                        break
        if flag!=0:
                return True
        else: return False

    

    def update(self, key, value, new_data): # возможность обновления
        lines = self.read_all()
        self.db_file.seek(0)
        self.db_file.truncate(0)
        for line in lines:
            if key in line and value in line:
                line = new_data
            self.db_file.write(line)

    def delete(self, key, value): # возможность удаления
        lines = self.read_all()
        self.db_file.seek(0)
        self.db_file.truncate(0)
        for line in lines:
            if not (key in line and value in line):
                self.db_file.write(line)
    def close(self):
        self.db_file.close()
