def number_with_comma(number):
    """returns a number as a separated digits separated by a comma
    Args:
        number - a number as an int
    return value:
        new_str_number - string - a number as a separated digits separated by a comma
        """
    str_number = str(number)
    new_str_number = str_number[0]
    for i in range(1, len(str_number)):
        new_str_number = new_str_number + ',' + str_number[i]
    return new_str_number


def number_sum_digits(number):
    """returns a number as a separated digits separated by a comma
        Args:
            number - a number as an int
        return value:
            sum_of_digits - int the sim of the digits
            """
    sum_of_digits = 0
    str_number = str(number)
    for i in range(5):
        sum_of_digits = sum_of_digits + int(str_number[i])
    return sum_of_digits


def check_number_validation(number):
    """checks if the input is a 5 digits number
            Args:
                number - a number as an int
            return value:
                True/False
                """
    if not number.isdigit():
        return False
    if not len(str(number)) == 5:
        return False
    return True


def main():
    assert number_with_comma(13453) == '1,3,4,5,3', 'not what was supposed to happen'
    assert number_sum_digits(13453) == 1+3+4+5+3, 'not what was supposed to happen'
    assert (check_number_validation(str(13453))) is True, 'not what was supposed to happen'
    assert (check_number_validation(str(1353))) is False, 'not what was supposed to happen'
    assert check_number_validation('') is False, 'not what was supposed to happen'
    assert check_number_validation('asa') is False, 'not what was supposed to happen'

    number = input("please insert a 5 digit number:\n")
    while not check_number_validation(number):
        number = input("please insert a 5 digit number:\n")
    print('You entered the number: ' + str(number))
    print('The digits of this number are: ' + number_with_comma(number))
    print('The sum of the digits is: ' + str(number_sum_digits(number)))


if __name__ == '__main__':
    main()
