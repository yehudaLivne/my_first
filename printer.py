import sys
def main():
    FILENAME=1
    with open(sys.argv[FILENAME],'r') as input_file:
        for line in input_file:
            print(line,end='')

if __name__ == '__main__':
    main()
