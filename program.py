
from classes.NumberManager import NumberManager

print("Hello")

manager = NumberManager()
path = ".\\sourse-numbers\\"
file = "1_part"

manager.readNumbers(file, path, "\t")