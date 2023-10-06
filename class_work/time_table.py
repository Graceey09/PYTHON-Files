def multiplication_table():
    number = int(input("Enter a number\n"))
    for numbers in range(1, 11):
        product = number * numbers
        print(number, " ",  "*", " ",  numbers, " ", "=", " ", product)


if __name__ == '__main__':
    multiplication_table()
