from classes.NumberBook import NumberBook
from classes.NumberItem import NumberItem


class NumberManager:

    __numberBook = None

    def __init__(self):
        self.__numberBook = NumberBook()

    def readNumbers(self, filename, pathname, delimiter):

        print("start processing file: " + filename + ".txt")

        with open(pathname + filename + ".txt", "r", encoding="utf-8") as searchfile:
            for line in searchfile:
                lineSpaceItems = line.split(delimiter)
                for item in lineSpaceItems:
                    if item == '\n':
                        continue
                    self.processItem(item)

                lineTabItems = line.split("\t")
                for item in lineTabItems:
                    if item == '\n':
                        continue
                    self.processItem(item)

        print("Result is:")
        self.__numberBook.showNumbers()

    def processItem(self, itemLine):
        print("in progress: " + itemLine)

        if len(itemLine) > 8 and len(itemLine) < 14:
            number = NumberItem(itemLine)
            print("\t -> ok len=" + str(len(itemLine)) + " try to add")
            if number is not None:
                self.__numberBook.addNumber(number)

        print("\t -> fail - no handler")