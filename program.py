from managers.FilesManager import FilesManager
from entities.TelephoneBook import TelephoneBook
from managers.Corrector import Corrector
from managers.Filter import Filter
from managers.Validator import Validator


print("Hello")


# ----- configuration ---------
print("\n#################### CONFIGURATION ##################\n")
path = ".\\new-version-dir\\"
fileWithSource = "source1"
fileWithFamiliarNums = "famnums"


# ----- initiation ------------
filesManager = FilesManager(path)
telBook = TelephoneBook()


# ----- call functions --------
familiarPreNums = filesManager.readfile(fileWithFamiliarNums, delimeter=',')
sourcePreNums = filesManager.readfile(fileWithSource, doubletry=True)

sourcePreNums = Validator.validate(Corrector.correct(Filter.dofilter(sourcePreNums)), familiarPreNums)

# ----- results ---------------
print("\n#################### RESULTS ########################\n")
print("famNums:\n" + familiarPreNums.__str__())
print("source:\n" + sourcePreNums.__str__())
