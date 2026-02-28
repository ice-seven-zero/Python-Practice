def pass_word():
    num=int(input("Enter a number:"))
    if num<0:
        raise Exception("Number cannot be negative")


if __name__ == '__main__':
    pass_word()