class Frog:

    def __init__(self,name=('Kermit')):
        self.__name = name
        self.__age = 0

    def birthday(self):
        self.__age += 1

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self,name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def __str__(self):
        return "Hello friend, i am a frog, my name is {}. I am {} years old, you wanna play?".format(self.get_name(),self.get_age())


def main():
    frog1=Frog()
    print(frog1.get_age())
    frog1.birthday()
    print(frog1.get_age())
    print(frog1)

if __name__ == '__main__':
    main()
