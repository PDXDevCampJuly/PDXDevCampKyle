import random


def random_list(n, var_type = "int"):
    """Generates a list of ints or floats in random order."""
    if var_type == "int":
        holder = list(range(1, n + 1))
        output = []
        while len(holder) > 0:
            index = random.randint(0, len(holder) - 1)
            output.append(holder.pop(index))
        return output
    else:
        return [random.random() for x in range(n)]


def random_string(n):
    """Generates a list of 'words' of length n to be sorted."""
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    output = []
    for index in range(n):
        length = random.randint(3, 7)
        word = ""
        for x in range(length):
            word += letters[random.randint(0, 25)]
        output.append(word)
    return output


if __name__ == '__main__':
    filename = input("Under what filename would you like to save? >> ")
    n = int(input("How long would you like your list? >> "))
    var_type = input("What type of element would you like (int)? >> ")
    with open(filename, 'w') as f:
        f.write(str(random_list(n, var_type)))
