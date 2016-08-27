

class Filter:

    @staticmethod
    def dofilter(itemsToFilter):
        startlen = itemsToFilter.__len__()
        print("do filter " + str(startlen) + " items")

        print(str(startlen - itemsToFilter.__len__()) + " items was delete\n")
        return itemsToFilter