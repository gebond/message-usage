

class Validator:

    @staticmethod
    def validate(itemsToValidate, familiarNums):
        startlen = itemsToValidate.__len__()
        print("do validate " + str(startlen) + " items")
        for item in itemsToValidate:
            # -------- 1 validation
            if not Validator.checkFamiliarUnique(item, familiarNums):
                itemsToValidate.remove(item)
                continue
            # -------- 2 validation
            if not Validator.checkAllDigits(item):
                itemsToValidate.remove(item)
                continue
            # -------- 3 validation
        return itemsToValidate

        print(str(startlen - itemsToValidate.__len__()) + " items was delete\n")
        return itemsToValidate

    @staticmethod
    def checkFamiliarUnique(currentNumber, familiarNums):
        print("Validator: check num is unique")
        for famNumber in familiarNums:
            if Validator.getSiblingCoeff(currentNumber, famNumber) > 63:
                print("Validator: looks like current num [" + str(currentNumber) + "] is pretty familiar!")
                return False
        print("Validator: OK! [" + str(currentNumber) + "] is a new one")
        return True

    @staticmethod
    def checkAllDigits(currentNumber):
        print("Validator: check all digits")
        for char in currentNumber:
            if not char.isdigit():
                print("Validator: -> NO")
                return False
        print("Validator: -> OK")
        return True

    @staticmethod
    def getSiblingCoeff(number, famNumber):
        siblingCoeff = 0
        index = 0
        while index < len(number) - 1:
            if number.__getitem__(index) == famNumber.__getitem__(index):
                siblingCoeff = siblingCoeff + 9.09
            index += 1
        return siblingCoeff