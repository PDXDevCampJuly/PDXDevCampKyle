from sys import argv

def get_secret(fileName):
    with open(fileName, 'r') as f:
        output = f.read()
    return output


def detransform(string):
    charList = string.split()
    message = ""
    for char in charList:
        if len(char) >= 7:
            message += chr(int(char[3:(3+int(char[0]))]))
        else:
            message += chr(int(char))
    print(message)


def main():
    if len(argv) > 2:
        print("Usage: decode.py <fileName>")
    else:
        try:
            fileName = argv[1]
        except IndexError:
            fileName = 'secret.txt'
        secret = get_secret(fileName)
        detransform(secret)


if __name__ == '__main__':
    main()
