from book import Book

class BookingDatabase:

    def __init__(self, db_name):
        self.db_name = db_name
        self.db_file = open(db_name, "a+")

    def isfree(self, time: str):
        with open(self.db_name) as f:
                for i in f:
                    if time in i:
                        return False 
                else: return True
  

    def write(self, book: Book): # возможность записи
        self.db_file = open(self.db_name, "a+")
        self.db_file.write(book.getInfo())       
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

    def close(self):
        self.db_file.close()
        