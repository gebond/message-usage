from classes.NumberItem import NumberItem
class NumberBook:

    __numbers = None

    def __init__(self):
        self.__numbers = []

    def addNumber(self, numberItem):
        if self.__validateNumber(numberItem):
            self.__numbers.append(numberItem)
            print("\t -> added " + numberItem.getNumber())


    def __validateNumber(self, number):
        for num in self.__numbers:
            if num.getNumber() == number.getNumber():
                print("\t -> already exists " + number.getNumber())
                return False
        if number.getNumber()[0] is not "8":
            print("\t -> suspecious number! " + number.getNumber())
            return False
        return True

    def showNumbers(self):
        for num in self.__numbers:
            print(num.getNumber())