from classes.NumberItem import NumberItem
class NumberBook:

    __numbers = None

    def __init__(self):
        self.__numbers = []

    def addNumber(self, numberItem):
        for num in self.__numbers:
            if num.getNumber() == numberItem.getNumber():
                print("\t -> already exists " + numberItem.getNumber())
                break
            if num.getNumber()[0] is not "8":
                print("\t -> suspecious number! " + numberItem.getNumber())

            self.__numbers.append(numberItem)
            print("\t -> added " + numberItem.getNumber())



    def showNumbers(self):
        for num in self.__numbers:
            print(num.getNumber())