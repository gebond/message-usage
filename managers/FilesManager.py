__author__ = 'Gleb'


class FilesManager:

    __directory = None
    __famName = None
    __source1 = None
    __source2 = None

    def __init__(self, directory):
        self.__directory = directory
        print("FilesManager: SET dir = " + self.__directory)

    def readfile(self, filename, delimeter=' ', doubletry=False):
        print("FilesManager:  reading [" + filename + ".txt] ...")
        resultlines = []
        with open(self.__directory + filename + ".txt", "r", encoding="utf-8") as searchfile:
            for line in searchfile:
                lineDelimeterItems = line.split(delimeter)
                for item in lineDelimeterItems:
                    if item == '\n':
                        continue
                    resultlines.append(item)
                if doubletry:
                    lineDelimeterItems = line.split('\t')
                    for item in lineDelimeterItems:
                        if item == '\n':
                            continue
                        resultlines.append(item)
        return resultlines