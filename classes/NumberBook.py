from classes.NumberItem import NumberItem
class NumberBook:

    __numbers = None

    def __init__(self):
        self.__numbers = []

    def addNumber(self, numberItem):
        if self.__validateNumber(numberItem):
            self.__numbers.append(numberItem)
            print("\t -> added " + str(numberItem.getNumber()))


    def __validateNumber(self, number):
        for num in self.__numbers:
            if num.getNumber() == number.getNumber():
                print("\t -> already exists " + str(number.getNumber()))
                return False
        return True

    def showNumbers(self):
        counter = 0
        for num in self.__numbers:
            counter += 1
            print("# " + str(counter) + " " + str(num.getNumber()))
        print("total: " + str(counter) + " nums")