

class Filter:

    @staticmethod
    def dofilter(itemsToFilter):
        startlen = itemsToFilter.__len__()
        filtredItems = []
        print("do filter " + str(startlen) + " items")
        for item in itemsToFilter:
            print("Filter: item - [" + item + "]")
            # -------- 1 filtration
            if not Filter.checkLength(item):
                print("length < 8 or > 13")
                continue
            # -------- 2 filtration
            #if not True:
                #continue

            print("add item")
            filtredItems.append(item)
        print(str(startlen - filtredItems.__len__()) + " items was delete\n")
        return filtredItems

    @staticmethod
    def checkLength(item):
        if (len(item) > 8) and (len(item) < 13):
            return True
        return False