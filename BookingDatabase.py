import book

class BookingDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db_file = open(db_name, "a+")

    def write(self, book: book): # возможность записи
        self.db_file = open(self.db_name, "a+")
        self.db_file.write(book.getInfo())       
        self.db_file.close()

    def read_all(self): # выгрузка всех строк из файла
        with open(self.db_name, "r") as file:
            lines = file.readlines()
        return lines
    
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

    def close(self):
        self.db_file.close()
        