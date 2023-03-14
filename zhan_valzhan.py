def number_with_comma(number):
    snumber=str(number)
    new_snumber=snumber[0]
    for i in range(1,len(snumber)):
        new_snumber = new_snumber+ ',' + snumber[i]
    return new_snumber

def number_sum_digits(number):
    sum=0
    snumber=str(number)
    for i in range(5):
        sum=sum+int(snumber[i])
    return sum

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    number = input("enter your number boy:\n")
    print('You entered the number: '+str(number))
    print('The digits of this number are: '+number_with_comma(number))
    print('The sum of the digits is: '+str(number_sum_digits(number)))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
