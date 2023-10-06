def your_vat():
    while True:
        try:
            price, vat = eval(input("Enter the price of item purchased and your percentage VAT\n"))
            vat = vat/100
            if price <= 0 or vat <= 0:
                print("Wrong input, please enter the right values")
                your_vat()
            return price * vat + price
        except (SyntaxError, ValueError, TypeError, NameError, ZeroDivisionError, KeyboardInterrupt,):
            print("Please follow instructions and enter a valid input\n")
        finally:
            print("Thanks for shopping with us")


if __name__ == '__main__':
    print('Your vat inclusive total = ', your_vat())