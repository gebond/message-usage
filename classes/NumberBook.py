from classes.NumberItem import NumberItem
class NumberBook:

    __numbers = None

    def __init__(self):
        self.__numbers = []

    def addNumber(self, numberItem):
        alreadyExists = False
        for num in self.__numbers:
            if num.getNumber() == numberItem.getNumber():
                alreadyExists = True
        if not alreadyExists:
            self.__numbers.append(numberItem)
            print("succesful added " + numberItem.getNumber())
        else:
            print("already exists " + numberItem.getNumber())


    def showNumbers(self):
        for num in self.__numbers:
            print(num.getNumber())