class NumberItem:

    __number = None
    __provided = None

    def __init__(self, number):

        number = self.correctSymbols(number)
        number = self.correctNumber(number)
        number = self.validateAllDigits(number)

        self.__number = number
        self.__provided = False

    def getNumber(self):
        return self.__number

    def setProvided(self, value):
        self.__provided = value

    def correctSymbols(self, number):
        if number[len(number)-1] == '\n':
            number = number[:len(number)-1]
        index = 0
        for char in number:
            if char == 'b':
                number = number[:index] + "5" + number[index+1:]
            if char == '?':
                number = number[:index] + "2" + number[index+1:]
            if char == '/':
                number = number[:index] + "7" + number[index+1:]
            if char == '.':
                number = number[:index] + number[index+1:]
            index += 1
        return number

    def correctNumber(self, number):
        if len(number) == 10:
            number = "8" + number

        if number[0] == "7" and len(number) == 11:
            number = "8" + number[1:]

        if len(number) < 10:
            number = "00000000001"

        return number

    def validateAllDigits(self, number):
        if str(number).isdigit():
            return number
        else:
            return "00000000001"
