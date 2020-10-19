'''a_list = [2, 4, 6, 8, 10, 12, 42, 40, 48, 60, 72, 74]
item = int(input("Enter a number: "))
if item in a_list:
    position = a_list.index(item)
    print("Your item is at position", position)
else:
    print("Not found in the list")


# Recursive method


def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if element == array[mid]:
        return mid
    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid - 1)
    else:
        return binary_search_recursive(array, element, mid + 1, end)


element = int(input("Enter a number: "))
array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]
print("Searching for {}".format(element))
print("Index of {}: {}".format(element, binary_search_recursive(array, element, 0, len(array))))'''


# iterative method
def binary_search_iterative(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0
    while start <= end:
        print("Subarray in step {}:{}".format(step, str(array[start:end + 1])))
        step = step + 1
        mid = (start + end) // 2
        if element == array[mid]:
            return mid
        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


element = int(input("Enter a number: "))
array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]
print("Searching for {}".format(element, array))
print("Index of {}: {}".format(element, binary_search_iterative(array, element)))
