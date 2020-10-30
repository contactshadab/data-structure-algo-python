def ternary_search(items, target):
    return _ternary_search(items, target, 0, len(items)-1)


def _ternary_search(items, start, end, target):
    if start > end:
        return - 1

    # Divide the array in three parts
    partition_size = (end - start) // 3
    mid1 = start + partition_size
    mid2 = end - partition_size

    if target == items[mid1]:
        return mid1

    if target == items[mid2]:
        return mid2

    if target < items[mid1]:
        return _ternary_search(items, start, mid1 - 1, target)
    elif target > items[mid1] and target < items[mid2]:
        return _ternary_search(items, mid1 + 1, mid2 - 1, target)

    return _ternary_search(items, mid1 + 1, mid2 - 1, target)


if __name__ == "__main__":
    items = [-10, 0, 10, 20, 30]
    print(ternary_search(items, -10))  # 0
    print(ternary_search(items, 30))  # 4
    print(ternary_search(items, 0))  # 1
    print(ternary_search(items, 100))    # -1
