

class Telephone:

    __number = None

    def __init__(self, number):
        self.__number = number

    def get(self):
        return str(self.__number)

    def show(self):
        print("TelNumber: [" + self.get() + "]")
