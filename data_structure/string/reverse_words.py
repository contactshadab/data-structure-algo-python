
# Run time complexity: O(d)
def reverse(text):
    if str is None:
        raise Exception('Illegal argument')

    result = []
    words = text.split(' ')
    for i in range(len(words)-1, -1, -1):
        result.append(words[i])

    return ' '.join(result)


if __name__ == "__main__":
    print(reverse("Reverse me"))
    print(reverse(""))
    # print(reverse(None))    # Exception: Illegal argument
