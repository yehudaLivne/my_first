def factorial(var):
    """return the factorial of given int
    Args:
        var - an Int
        """
    factor = 1
    if var == 0:
        return 1
    while var > 0:
        factor = factor * var
        var -= 1
    return factor


def beep(sentnce):
    """returns the sentnce with a "beep" at end
    Args:
        sentece - a string
        """
    return sentnce + 'beep'


def kefel(var1, var2):
    """multyply two numbers if result is negative returns 0
    Args:
        var1 - an Int
        var2 - an Int
        """
    if var1 * var2 < 0:
        return 0
    return var1 * var2


if __name__ == '__main__':
    print(beep('ass'))
    print(factorial(1))
    print(factorial(0))
    print(factorial(8))
    print(kefel(1, 8))
    print(kefel(1, -8))


