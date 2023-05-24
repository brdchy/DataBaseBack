import user

class Database: 

    def __init__(self, db_name):
        self.db_name = db_name
        self.db_file = open(db_name, "a+")

    def write(self, user: user): # возможность записи
        self.db_file = open(self.db_name, "a+")
        self.db_file.write(user.getInfo()) 
        self.db_file.write("\n")
        self.db_file.close()

    def searchfor(self, value: str):                
        with open(self.db_name) as f:
                for i in f:
                    if (f"{value}") in i:                       
                        return True, str(i)
                                              
        return False, ""

    

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


    def unload_users(self): # выгрузка пользователей с возможность взаимодействия в цикле
        a = ""
        with open(self.db_name, "r") as file:
            for line in file:
                a += str(line) 

        return a
            


    def close(self):
        self.db_file.close()

        
    def delete_record(self, login): # удаление строк по логину пользователя
        with open(self.db_name, "r") as file:
            lines = file.readlines()

        deleted = False
        updated_lines = []
        for line in lines:
            if login not in line:
                updated_lines.append(line)
            else:
                deleted = True

        if not deleted:
            return False  # Запись с заданным логином не найдена


        with open(self.db_name, "w") as file:
            file.writelines(updated_lines)

        return True  # Запись успешно удалена
