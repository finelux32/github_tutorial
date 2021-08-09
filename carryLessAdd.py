def carry_less_add(x, y):
    assert (x >= 0)
    assert (y >= 0)

    x_str = str(x)
    y_str = str(y)

    x_length = len(x_str)
    y_length = len(y_str)
    longest_number_length = -1 # undefined

    # casting from int to str with zero-padding
    if x_length > y_length:
        longest_number_length = x_length
        y_str = y_str.zfill(longest_number_length)
    elif x_length < y_length:
        longest_number_length = y_length
        x_str = x_str.zfill(longest_number_length)
    else:
        longest_number_length = x_length

    # digit-wise addition without carry
    return_val = ''
    for i in range(longest_number_length):
        carry_less_add_result = int(x_str[i]) + int(y_str[i])
        if carry_less_add_result >= 10: # [0, 18]
            carry_less_add_result -= 10
        return_val += str(carry_less_add_result)

    if len(return_val) != 1:
        return_val = return_val.lstrip('0')
    return int(return_val)


if __name__ == '__main__':
    result = carry_less_add(785, 376)
    assert (result == 51)
    print('PASS')

    result = carry_less_add(0, 0)
    assert (result == 0)
    print('PASS')

    result = carry_less_add(123, 5) # '123', '005'
    assert (result == 128)
    print('PASS')

    result = carry_less_add(123, 0)
    assert (result == 123)
    print('PASS')
    
    try:
        result = carry_less_add(-30, -120)
        print('FAIL - You cannot reach here!')
    except Exception:
        print('PASS')

