class BigThing:
    def __init__(self,thing):
        self.__thing = thing

    def size(self):
        if isinstance(self.__thing, (int, float)):
            return self.__thing
        elif isinstance(self.__thing, (list, str, dict)):
            return len(self.__thing)

class BigCat(BigThing):
    def __init__(self,thing,weight):
        super(BigCat,self).__init__(thing)
        self.__weight = weight

    def size(self):
        if self.__weight > 20: return 'very fat'
        if self.__weight > 15: return 'fat'
        else: return 'OK'


def main():
    thing1 = BigThing('asda')
    cat1 = BigCat('asda',345)
    print(thing1.size())
    print(cat1.size())

if __name__ == '__main__':
    main()
