
from classes.NumberManager import NumberManager

print("Hello")

manager = NumberManager()
path = "C:\\Users\\glbo0616\\repository\\myrep\\message-usage\\message-usage\\sourse-numbers\\"
file = "my"

manager.readNumbers(file, path, delimiter=',')