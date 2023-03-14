import sys


def solution(line_arguments):
    if len(line_arguments)>3:
        return line_not_good
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


def normal_str(line_arguments):
    return line_arguments[0]+' '+line_arguments[1]+' '+line_arguments[2]


def main():
    home_work = sys.argv[1]
    solutions = sys.argv[2]

    home_work_solutions = open(solutions, 'w')
    home_work_solutions.close()

    while True:
        try:
            home_work_solutions = open(solutions, 'a')
            home_work_input = open(home_work, 'r')
            break
        except Exception as e:
            print('Error is {}'.format(e))
            home_work = input('try to enter another path')

    for line in home_work_input:
        line_arguments = line.split()
        try:
            home_work_solutions.write(normal_str(line_arguments) + ' = ' + str(solution(line_arguments))+'\n')
            print(normal_str(line_arguments) + ' = ' + str(solution(line_arguments)))
        except Exception as e:
            print('Error is {}'.format(e))
            home_work_solutions.write('not a good line')
            print('not a good line')

    home_work_solutions.close()


if __name__ == '__main__':
    main()
