__author__ = 'Gleb'


class FilesManager:

    __directory = None
    __famName = None
    __source1 = None
    __source2 = None

    def __init__(self, directory, FamiliarfilesName, Source1Name, Source2Name):
        self.__director = directory
        self.__famName = FamiliarfilesName
        self.__source1 = Source1Name
        self.__source2 = Source2Name

    def readfile(self, filename, delimeter):
        print("reading file: " + filename + ".txt")
        resultlines = []
        with open(self.__directory + filename + ".txt", "r", encoding="utf-8") as searchfile:
            for line in searchfile:
                lineDelimeterItems = line.split(delimeter)
                for item in lineDelimeterItems:
                    if item == '\n':
                        continue
                    resultlines.append(item)
        return resultlines