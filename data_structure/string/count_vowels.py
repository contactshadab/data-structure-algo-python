# Run time complexity: O(n)
def count(str):
    if str is None:
        raise Exception('Illegal argument')

    count = 0
    for ch in str:
        if ch in 'aeiou':
            count += 1

    return count


if __name__ == "__main__":
    print(count("I have a vowel"))
    print(count(""))
    # print(count(None))  # Exception: Illegal argument
