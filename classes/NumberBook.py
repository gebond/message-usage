class NumberBook:

    __numbers = None

    def __init__(self):
        self.__numbers = []

    def addNumber(self, numberItem):
        self.__numbers.append(numberItem)


    def showNumbers(self):
        for num in self.__numbers:
            print(num)


