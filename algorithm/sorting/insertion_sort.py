# Run time Complexity - O(n^2) both best case and worst case
# Space complexity = O(1)

def insertion_sort(items):
    if items is None:
        raise Exception('Empty list')

    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >= 0 and current < items[j]:

            # Shift item to its right
            items[j + 1] = items[j]

            j = j - 1

        items[j + 1] = current


if __name__ == "__main__":
    items1 = [30, 20, 40, 10, 50, 0]
    insertion_sort(items1)
    print(items1)

    items2 = [30]
    insertion_sort(items2)
    print(items2)

    items3 = []
    insertion_sort(items3)
    print(items3)
