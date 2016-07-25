class NumberItem:

    __number = None
    __provided = None
    __famNumbers = []

    def __init__(self, number):

        number = self.correctSymbols(number)
        number = self.correctNumber(number)
        number = self.validateAllDigits(number)
        number = self.validateLength(number)
        number = self.validateNotSimiliar(number)

        self.__number = number
        self.__famNumbers = ["89023849576", "89093803160", "9878374368", "89064075224"]
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

    def validateLength(self, number):
        if len(number) == 11:
            return number
        else:
            return "00000000001"

    def validateNotSimiliar(self, currentNum):
        for familiar in self.__famNumbers:
            result = self.getcomarasion(familiar, currentNum)
            print("Result: " + result)
            if result == -1 or result < 77:
                return currentNum
            else:
                return "00000000001"

    def getcomarasion(self, num1, num2):
        step = 9.09  # 11/100%
        indicator = 0
        count = 0
        if len(num1) is not len(num2):
            return -1
        for digit in num1:
            if num2[count] == digit:
                indicator += step
        print(str(num1) + " and " + str(num2) + " famil:" + str(indicator))
        return indicator