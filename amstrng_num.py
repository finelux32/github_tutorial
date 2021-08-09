# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def is_narcissistic(number):
    sum_of_digits = 0
    numbers_str = str(number)  # e.g. number_str = "153"

    for number_str in numbers_str:
        number_int = int(number_str)
        sum_of_digits += number_int ** 3
    return sum_of_digits == number


def solution(start_num, end_num):
    solutions = []
    # 각 자리별로 is_narcissistic check => print
    current_number = start_num
    while current_number <= end_num:
        #  Narsisstic Number인지 체크
        if is_narcissistic(current_number):
            solutions.append(current_number)
        current_number += 1
    return solutions


if __name__ == '__main__':
    # # 입력 받기
    # user_input = input()  # user_input = "100 500"
    # user_inputs = user_input.split()  # user_inputs = ['100', '500']
    # start_num = int(user_inputs[0])  # start_num = 100
    # end_num = int(user_inputs[1])  # end_num = 500
    # solutions = solution(start_num, end_num)

    test_inputs = [[100, 300], [100, 500]]
    test_outputs = [[153], [153, 370, 371, 407]]
    for i, test_input in enumerate(test_inputs):
        # Test Case #01
        if (solution(test_input[0], test_input[1]) == test_outputs[i]):
            print('OK')
        else:
            print('FAIL')



