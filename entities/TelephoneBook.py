

class TelephoneBook:

    __telephones = []

    def add(self, tel):
        if not self.exists(tel):
            self.__telephones.append(tel)

    def exists(self, newtel):
        exists = False
        for tel in self.__telephones:
            if tel.get() == newtel:
                exists = False
        return exists

    def show(self):
        print("TelBook:")
        counter = 0
        for tel in self.__telephones:
            print("# " + counter + " " + tel.get())
            counter += 1

