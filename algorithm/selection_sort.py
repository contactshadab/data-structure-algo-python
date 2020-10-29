# Run time Complexity - O(n^2) both best case and worst case
# Space complexity = O(1)

def selection_sort(items):
    if items is None:
        raise Exception('Empty list')

    for i in range(len(items)):
        min = i
        j = i
        while j < len(items):
            if items[j] < items[min]:
                min = j

            j = j + 1
        _swap(items, i, min)


def _swap(items, left, right):
    temp = items[left]
    items[left] = items[right]
    items[right] = temp


if __name__ == "__main__":
    items1 = [30, 20, 40, 10, 50, 0]
    selection_sort(items1)
    print(items1)

    items2 = [30]
    selection_sort(items2)
    print(items2)

    items3 = []
    selection_sort(items3)
    print(items3)
