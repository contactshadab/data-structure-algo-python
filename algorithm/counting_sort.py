
def counting_sort(items, k):
    if items is None or k < 1:
        raise Exception('Illegal Arguments')

    # Create a list of k size
    counts = [0] * (k+1)

    # Fill the list with no of occurance of each item in the right index
    for item in items:
        counts[item] += 1

    index = 0
    for i in range(len(counts)):
        if counts[i] == 0:
            continue

        for j in range(counts[i]):
            items[index] = i
            index += 1


if __name__ == "__main__":
    items1 = [30, 20, 40, 10, 50, 0, 30]
    counting_sort(items1, 50)
    print(items1)

    items2 = [30]
    counting_sort(items2, 30)
    print(items2)

    items3 = []
    counting_sort(items3, 1)
    print(items3)
