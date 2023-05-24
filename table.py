class Table:

    def __init__(self, numbertable, tables_role):

        self.numbertable = numbertable
        self.tables_role = tables_role

    def getInfo(self):
        return str(f"{self.numbertable}:{self.tables_role}")
