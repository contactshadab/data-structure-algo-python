
def binary_search(items, target):
    return _binary_search(items, 0, len(items)-1, target)


def _binary_search(items, start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2
    if target == items[mid]:
        return mid

    if target < items[mid]:
        return _binary_search(items, start, mid-1, target)

    return _binary_search(items, mid+1, end, target)

    return -1


def binary_search_iterative(items, target):
    start = 0
    end = len(items)-1
    while start <= end:
        mid = (start + end) // 2

        if items[mid] == target:
            return mid

        if target < items[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


if __name__ == "__main__":
    items = [-10, 0, 10, 20, 30]
    print(binary_search(items, -10))  # 0
    print(binary_search(items, 30))  # 4
    print(binary_search(items, 0))  # 1
    print(binary_search(items, 100))    # -1
    print(binary_search_iterative(items, -10))  # 0
    print(binary_search_iterative(items, 30))  # 4
    print(binary_search_iterative(items, 0))  # 1
    print(binary_search_iterative(items, 100))    # -1
