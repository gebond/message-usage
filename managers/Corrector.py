

class Corrector:

    @staticmethod
    def correct(itemsToCorrect):
        startlen = itemsToCorrect.__len__()
        print("do correct " + str(startlen) + " items")

        print(str(startlen - itemsToCorrect.__len__()) + " items was delete\n")
        return itemsToCorrect




