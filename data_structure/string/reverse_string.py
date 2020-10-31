# Run time complexity: O(n)
def reverse(str):
    if str is None:
        raise Exception('Illegal argument')

    lst = []
    for i in range(len(str)-1, -1, -1):
        lst.append(str[i])

    return ''.join(lst)


if __name__ == "__main__":
    print(reverse("Reverse me"))
    print(reverse(""))
    # print(reverse(None))    # Exception: Illegal argument
