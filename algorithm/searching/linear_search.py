def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i

    return -1


if __name__ == "__main__":
    items = [7, 6, -3, 1, 5]
    print(linear_search(items, 5))  # 0
    print(linear_search(items, 7))  # 0
    print(linear_search(items, -3))  # 2
    print(linear_search(items, 100))    # -1
