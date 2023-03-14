import sys
import os


def valid_line(line_arguments):
    if len(line_arguments) > 3:
        return False
    if not line_arguments[0].isdigit():
        return False
    if not line_arguments[2].isdigit():
        return False
    if not is_this_math_operation(line_arguments[1]):
        return False
    if line_arguments[1] == '/' and line_arguments[2] == '0':
        return False
    return True


def solution(line_arguments):
    a = int(line_arguments[0])
    b = int(line_arguments[2])
    operation = line_arguments[1]
    if operation == '+':
        return a+b
    if operation == '-':
        return a-b
    if operation == '*':
        return a*b
    if operation == '/':
        return a/b


def is_this_math_operation(operation):
    if (operation == '+') or (operation == '-') or (operation == '*') or (operation == '/'):
        return True
    return False


def normal_str(line_arguments):
    return line_arguments[0]+' '+line_arguments[1]+' '+line_arguments[2]


def main():
    home_work = sys.argv[1]
    solutions = sys.argv[2]

    home_work_solutions = open(solutions, 'w')
    home_work_solutions.close()

    while not os.path.exists(home_work):
        home_work = input("wrong path enter a different one: ")

    with open(solutions, 'a') as home_work_solutions:
        with open(home_work, 'r') as home_work_input:
            for line in home_work_input:
                line_arguments = line.split()
                if not valid_line(line_arguments):
                    home_work_solutions.write('this line format is not good\n')
                    print('this line format is not good')
                    continue
                home_work_solutions.write(normal_str(line_arguments) + ' = ' + str(solution(line_arguments))+'\n')
                print(normal_str(line_arguments) + ' = ' + str(solution(line_arguments)))


if __name__ == '__main__':
    main()
