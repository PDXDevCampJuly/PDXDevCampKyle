from sys import argv
from random import randint

def transform(string):
    output = []
    for char in string:
        output.append(str(ord(char)))
    return ' '.join(output)


def transform_plus(string):
    output = []
    for char in string:
        char = str(ord(char))
        output.append("{}{}{}{}".format(len(char), randint(10,99), char, randint(10,99)))
    return ' '.join(output)


def make_secret(string, fileName):
    with open(fileName, 'w') as f:
        f.write(string)


def main():
    if len(argv) > 4:
        print(
            """Usage: encode.py <message> <filename> <strong>"""
        )
    else:
        try:
            message = argv[1]
        except IndexError:
            message = input("What message would you like to send? >> ")
        try:
            fileName = argv[2]
        except IndexError:
            fileName = 'secret.txt'
        try:
            if argv[3].title() in ['F', 'False']:
                strong = False
            else:
                strong = True
        except IndexError:
            strong = True
        if strong:
            encodedMessage = transform_plus(message)
        else:
            encodedMessage = transform(message)
        make_secret(encodedMessage, fileName)
        print("Message encoded to {}.  The lotion is in the basket.".format(fileName))


if __name__ == '__main__':
    main()
