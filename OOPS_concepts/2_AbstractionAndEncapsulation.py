# class = customer
# layer of abstraction = request for book

class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
        pass
    
    def displayAvailableBooks(self):
        print()
        print("Available books: ")
        for book in self.availableBooks:
            print(book)
        pass

    def lendbook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You have borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("not available")
        pass

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have returned the book")
        pass

class Customer:


    def requestBook(self):
        print("Enter the name of the book you want: ")
        self.book = input()
        return self.book 
        pass

    def returnBook(self):
        print("Which book do you want to return")
        self.book = input()
        return self.book 
        pass


#create object

library = Library(['Think and grow rich','Who will cry when you die','For one more day'])
customer = Customer()

print ("1 to display available books")
print ("2 to request a book")
print ("3 to return a book")
print ("4 to exit")

userchoice = int(input())
while True:
    if userchoice is 1:
        library.displayAvailableBooks()
    elif userchoice is 2:
        requestedBook = customer.requestBook()
        library.lendbook(requestedBook)

    elif userchoice is 3:
        returnBook = customer.returnBook()
        library.addBook(returnedBook)

    elif userchoice is 4:
        quit()

