class User: 

    def __init__(self, login, password, is_Admin = False):
        self.login = login 
        self.password = password 
        

    def getInfo(self):
        return str(f"{self.login}:{self.password}:{self.is_Admin}")



