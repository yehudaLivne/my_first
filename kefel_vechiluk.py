def kefel(var1,var2):
    """multyply two numbers
    Args:
        var1 - an Int
        var2 - an Int
        """
    return var1*var2

def chiluk(var1,var2):
    """devides two numbers
    Args:
        var1 - an Int
        var2 - an Int
        """
    if(var2==0):
        return 'ilegal'
    else:
        return var1/var2

if __name__ == '__main__':
    print(kefel(1,4))
    print(chiluk(1, 4))
    print(chiluk(1, 0))
    help(kefel)
