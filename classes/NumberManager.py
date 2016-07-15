from classes.NumberBook import NumberBook
from classes.NumberItem import NumberItem


class NumberManager:

    __numberBook = None

    def __init__(self):
        self.__numberBook = NumberBook()

    def readNumbers(self, filename, pathname, delimiter=','):

        print("start processing file: " + filename + ".txt")

        with open(pathname + filename + ".txt", "r") as searchfile:
            for line in searchfile:
                lineItems = line.split(delimiter)
                for item in lineItems:
                    if len(item) == 11:
                        if item.isdigit():
                            number = NumberItem(item)
                            self.__numberBook.addNumber(number)
                    if len(item) == 12:
                        if item[1:].isdigit():
                            number = NumberItem(item[1:])
                            self.__numberBook.addNumber(number)
        print("Result is:")
        self.__numberBook.showNumbers()

