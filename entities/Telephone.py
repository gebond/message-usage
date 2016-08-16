

class Telephone:

    __number = None

    def __init__(self, number):
        self.__number = number

    def get(self):
        return self.__number

    def show(self):
        print("TelNumber: [" + str(self.__number) + "]")