def odd_numbers_in_list():
    empty_list = []
    my_list = [22, 41, 15, 8, 2, 1]
    for digits in my_list:
        if digits % 2 != 0 and digits not in empty_list:
            empty_list.append(digits)
            print(empty_list)


if __name__ == '__main__':
    odd_numbers_in_list()
