from managers.FilesManager import FilesManager

print("Hello")
# ----- configuration ---------

path = ".\\new-version-dir\\"
fileWithSource = "source1"
fileWithFamiliarNums = "famnums"

# ----- initiation ------------
filesManager = FilesManager(path)

# ----- call functions --------
familiarPreNums = filesManager.readfile(fileWithFamiliarNums, delimeter=',')
sourcePreNums = filesManager.readfile(fileWithSource, doubletry=True)

# ----- results ---------------
print("famNums:\n" + familiarPreNums)
print("source:\n" + sourcePreNums)
