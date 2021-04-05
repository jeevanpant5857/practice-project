class Library:
    def __init__(self,ListofBooks):
        self.books = ListofBooks

    def displayAvailableBooks(self):
        print('books present in library are: ')
        for book in self.books:
            print(book)
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f'you have been issued {bookName}, please keep it safe and return it within 30 days')
            self.books.remove(bookName)
        else:
            print('sorry this book is already issued to someone else')

    def returnBook(self,returnBook):
        self.books.append(returnBook)
        print('thanks for return')

class Student:
    def requestBook(self):
        self.Book = input('enter the book which you want to borrow')
        return self.Book

    def returnBook(self):
        self.Book = input('enter the book which you want to return')
        return self.Book
if __name__ == '__main__':
    centralLibrary = Library(['A', 'B', 'C', 'D'])
    Student = Student()
    centralLibrary.displayAvailableBooks()
    while(True):
        WelcomeMessage = '''*****welcome to the library*****
        choose any option which you want to choose:-
        1.List all the Books
        2.Borrow a Book
        3.Return a Book
        4.Exit the Library'''
        
        print(WelcomeMessage)
        a = int(input('please enter your choice'))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(Student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(Student.returnBook())
        elif a == 4:
            print('thanks for choosing centralLibrary')
            exit()
        else:
            print('please enter the right choice')