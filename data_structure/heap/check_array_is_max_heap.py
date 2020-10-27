def is_max_heap(items):
    if items is None:
        raise Exception('Empty heap')

    # Leafs are max heap
    last_non_leaf = (int)(len(items)/2) - 1

    for i in range(0, last_non_leaf+1):
        if not _is_max_heap(items, i):
            return False

    return True


def _is_max_heap(items, index):
    left_child_index = index * 2 + 1
    right_child_index = index * 2 + 2
    larger_child = items[left_child_index]
    if right_child_index < len(items) and items[right_child_index] > items[left_child_index]:
        larger_child = items[right_child_index]

    return items[index] >= larger_child


if __name__ == "__main__":
    print(is_max_heap([8, 5, 4, 3, 2, 1]))  # True
    print(is_max_heap([8, 5, 4, 3, 2, 1, 3]))  # True
    print(is_max_heap([8, 5, 4, 3, 2, 1, 4]))  # True
    print(is_max_heap([8, 5, 4, 3, 2, 1, 5]))  # False
