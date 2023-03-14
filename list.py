def list():
    """creates a 5 length list
        """
    stam_list = ['asd', 144, 'a l f', 33.13, 0]
    return stam_list


def SLICED_list(list):
    """return rvery seconf element in list
        """
    return list[::2]

def summer(list):
    sum = list[0]
    for element in list:
        if element !=list[0]:
            sum = sum+element
    return sum


if __name__ == '__main__':
    for elemnt in list():
        print(elemnt,end=" ")
    print()

    for elemnt in SLICED_list(list()):
        print(elemnt,end=" ")
    print()
    print(summer([10,11,13,0.75]))
    print(summer([True,False,True,True]))
    print(summer(['aa', 'bb','cc','dd']))
    print(summer([[1,2,3,'a'],[4,'b','c','d']]))




