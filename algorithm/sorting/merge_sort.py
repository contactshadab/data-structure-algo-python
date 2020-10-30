
def merge_sort(items):
    if items is None:
        raise Exception('Empty list')

    if len(items) <= 1:
        return

    # Divide the array into half
    mid = len(items) // 2
    left = items[0: mid]
    right = items[mid: len(items)]

    # Sort the both halves
    merge_sort(left)
    merge_sort(right)

    # Merge the two sorted arrays
    _merge(items, left, right)


def _merge(target, left, right):
    left_p = right_p = target_p = 0
    while left_p < len(left) and right_p < len(right):
        if left[left_p] < right[right_p]:
            target[target_p] = left[left_p]
            left_p += 1
        else:
            target[target_p] = right[right_p]
            right_p += 1

        target_p += 1

    # Copy remaining items from left
    while left_p < len(left):
        target[target_p] = left[left_p]
        left_p += 1
        target_p += 1

    # Copy remaining items from right
    while right_p < len(right):
        target[target_p] = right[right_p]
        right_p += 1
        target_p += 1


if __name__ == "__main__":
    items1 = [30, 20, 40, 10, 50, 0]
    merge_sort(items1)
    print(items1)   # [0, 10, 20, 30, 40, 50]

    items2 = [30]
    merge_sort(items2)
    print(items2)   # [30]

    items3 = []
    merge_sort(items3)
    print()   # []
