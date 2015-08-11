# Implimentation of various sorting algorithms for lists
##########################

def python_sort(our_list):
    return sorted(our_list)


def list_swap(our_list, low, high):
    our_list[low], our_list[high] = our_list[high], our_list[low]
    return our_list


def selection_sort(our_list):
    """
    Look through the list.  Find the smallest element.  Swap it to the front.
    Repeat.
    """
    for start in range(len(our_list)):
        mindex = start
        minimum = our_list[start]
        for index in range(start + 1, len(our_list)):
            if our_list[index] < minimum:
                mindex = index
                minimum = our_list[index]
        if mindex != start:
            list_swap(our_list, start, mindex)
    return our_list


def insertion_sort(our_list):
    """
    Insert (via swaps) the next element in the sorted list of the previous
    elements.
    """
    for index in range(1, len(our_list)):
        candidate = our_list[index]
        comparison_index = index - 1
        while comparison_index >= 0:
            if candidate < our_list[comparison_index]:
                list_swap(our_list, comparison_index, comparison_index + 1)
                comparison_index -= 1
            else:
                break
    return our_list


def merge_sort(our_list):
    """
    Our first recursive algorithm.
    """
    if len(our_list) == 1:
        return our_list
    else:
        middle = len(our_list) // 2
        list1 = merge_sort(our_list[:middle])
        list2 = merge_sort(our_list[middle:])
        list3 = []
        while len(list1) > 0 and len(list2) > 0:
            if list1[0] <= list2[0]:
                list3.append(list1.pop(0))
            else:
                list3.append(list2.pop(0))
        return list3 + list1 + list2

if __name__ == '__main__':
    with open('int100.txt') as f:
        int100 = eval(f.read())
    with open('float100.txt') as f:
        float100 = eval(f.read())
    with open('char100.txt') as f:
        char100 = eval(f.read())
    print(selection_sort(int100))
    print(insertion_sort(float100))
    print(merge_sort(char100))
