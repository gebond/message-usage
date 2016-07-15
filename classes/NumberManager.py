from classes import NumberBook
from classes.NumberItem import NumberItem


class NumberManager:

    __numberBook = None

    def __init__(self):
        self.__numberBook = NumberBook()

    def readNumbers(self, filename, pathname):
        print("start processinf file: " + filename + ".txt")
        with open(pathname + filename + ".txt", "r") as searchfile:
            for line in searchfile:
                number = NumberItem(line)

                #self.__numberBook.addNumber(number)
        print("Result is:")
        self.__numberBook.showNumbers()

