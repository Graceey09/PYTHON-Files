def subtract_from_list():
    new_list = []
    unique_list = []
    my_list = [22, 41, 15, 8, 2, 1]
    for element in my_list:
        if element % 2 != 0 and element not in new_list:
            new_list.append(element)
            for item in new_list:
                item = item - 2
                if item not in unique_list:
                    unique_list.append(item)
                print(unique_list)


if __name__ == '__main__':
    subtract_from_list()