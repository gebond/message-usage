class NumberItem:

    __number = None
    __provided = None

    def __init__(self, number):
        if number[0] == "7":
            number = "8" + number[1:]
        self.__number = number
        self.__provided = False

    def getNumber(self):
        return self.__number

    def setProvided(self, value):
        self.__provided = value