class person:
    def __init__(self,name='anonimous',age = 30):
        self.__name = name
        self.__age = age

    def say(self):
        return "hi :)"

    def __str__(self):
        return "person {} is {} years old".format(self.__name,self.__age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age


def main():
    return

if __name__ == '__main__':
    main()
