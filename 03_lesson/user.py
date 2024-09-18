class User:
    def __init__ (self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name

    def printFirstName(self):
        print("Имя", self.firstName)

    def printLastName(self):
        print("Фамилия", self.lastName)
    
    def printFirstNameLastName(self):
        print("Имя и фамилия", self.firstName, self.lastName)
    