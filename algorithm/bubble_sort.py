def bubble_sort(items):
    # After every pass the next largest value will be move to its right position
    for i in range(len(items)):
        current = 0
        is_sorted = True

        # Compare two neighbours and swap the larger value with its right
        while current < len(items)-1:
            if items[current] > items[i]:
                # Swap the values
                _swap(items, current, i)
                is_sorted = False

            current = current + 1

        # If array is found sorted in the previous pass no need to iterate again
        if is_sorted:
            return


def _swap(items, left, right):
    temp = items[left]
    items[left] = items[right]
    items[right] = temp


if __name__ == "__main__":
    items1 = [30, 20, 40, 10, 50, 0]
    bubble_sort(items1)
    print(items1)

    items2 = [30]
    bubble_sort(items2)
    print(items2)

    items3 = []
    bubble_sort(items3)
    print(items3)
