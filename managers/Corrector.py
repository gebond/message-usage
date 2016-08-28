

class Corrector:

    @staticmethod
    def correct(itemsToCorrect):
        startlen = itemsToCorrect.__len__()
        correctedItems = []
        print("do correct " + str(startlen) + " items")
        for item in itemsToCorrect:
            print("Corrector: item - [" + item + "]")
            # -------- 1 correction
            correctedItem = Corrector.correctSymbols(Corrector.changeNums(item))
            # -------- 2 correction
            print("Corrector: AFTER - [" + correctedItem + "]")
            correctedItems.append(correctedItem)
        print(str(startlen - correctedItems.__len__()) + " items was delete\n")
        return correctedItems

    @staticmethod
    def correctSymbols(item):
        if item[len(item)-1] == '\n':
            item = item[:len(item)-1]
        index = 0
        for char in item:
            if char == 'b':
                item = item[:index] + "5" + item[index+1:]

            if char == '?':
                item = item[:index] + "2" + item[index+1:]

            if char == '/':
                item = item[:index] + "7" + item[index+1:]

            if char == '.':
                item = item[:index] + item[index+1:]

            index += 1
        return item
    @staticmethod
    def changeNums(item):
        if len(item) == 10:
            item = "8" + item

        if item[0] == "7" and len(item) == 11:
            item = "8" + item[1:]

        return item