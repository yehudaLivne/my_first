# duplicates a text file and coping it to another file

def main():
    output_file = open('b.txt', 'a')
    with open('a.txt', 'r')as input_file:
        for line in input_file:
            output_file.write(line)
    output_file.close()


if __name__ == '__main__':
    main()
