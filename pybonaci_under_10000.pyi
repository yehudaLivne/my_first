def fibonachi_number(a,b):
    return a+b

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a=1
    b=1
    print(a)
    print(b)
    while True:
        c=fibonachi_number(a,b)
        a=b
        b=c
        if c>10000:
            break
        print(c)

ff




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
