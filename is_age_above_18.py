def is_age_above18(age):
    if age>18:
        return 'age above 18'
    else:
        return 'age not above 18'

def print_respnse_to_the_age(is_age_above18):
    if(is_age_above18=='age above 18'):
        print('Congratulations')
    else:
        print('You are so young')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    age1=15
    is_age_above18 = is_age_above18(age1)
    print_respnse_to_the_age(is_age_above18)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
