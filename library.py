#Library module containing the USER, BOOK and LIBRARY class.

class Book:

    def __init__(self, author, title, year, id):
        self.author = author
        self.title = title
        self.year = year
        self.id = id
        self.states = ['available', 'on loan']

        self.status = self.states[0]

    def getAuthor(self):
        return self.author
    
    def getTitle(self):
        return self.title
    
    def getYear(self):
        return self.year

    def takeOut(self):
        if self.status == self.states[0]:
            self.status = self.states[1]
            print(f"{self.title} is now on loan to you.")
        else:
            print(f"{self.title} is already on loan.")


class User:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    

class Library:
    bookList = []
    userList = []

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def addBook(self, book):
        self.bookList.append(book)

    def addUser(self, user):
        self.bookList.append(user)

    def getBooks(self):
        return self.bookList
    
    def getUsers(self):
        return self.userList