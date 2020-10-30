
def quick_sort(items):
    if items is None:
        raise Exception('Empty array')

    _quick_sort(items, 0, len(items)-1)


def _quick_sort(items, start, end):
    # A single element array is already sorted
    if start >= end:
        return

    # Partition the array
    boundry = _partition(items, start, end)

    # Sort left and right partitions
    _quick_sort(items, 0, boundry-1)
    _quick_sort(items, boundry+1, end)


def _partition(items, start, end):
    pivot = items[end]
    boundry = start-1
    for i in range(start, end+1):
        if items[i] <= pivot:
            boundry += 1
            _swap(items, boundry, i)

    return boundry


def _swap(items, left, right):
    temp = items[left]
    items[left] = items[right]
    items[right] = temp


if __name__ == "__main__":
    items1 = [30, 20, 40, 10, 50, 0, 30]
    quick_sort(items1)
    print(items1)

    items2 = [30]
    quick_sort(items2)
    print(items2)

    items3 = []
    quick_sort(items3)
    print(items3)   # []

    # quick_sort(None)
    # print(items3)   # Exception: Empty array
