class NumberItem:

    __number = None
    __provided = None

    def __init__(self, number):
        self.__number = number
        self.__provided = False

    def getNumber(self):
        return self.__number

    def setProvided(self, value):
