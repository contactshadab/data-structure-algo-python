from heap_implementaion import Heap


def get_kth_largest(items, k):
    if items is None or k > len(items) or k <= 0:
        raise Exception('Illegal Argument')

    # Add all items to heap
    heap = Heap()
    for item in items:
        heap.insert(item)

    # Keep removing k-1 items and the root will have kth largest value
    for i in range(k-1):
        largest = heap.remove()

    return heap.items[0]


if __name__ == "__main__":
    items = [5, 3, 8, 4, 1, 2]

    print(get_kth_largest(items, 1))    # 8
    print(get_kth_largest(items, 2))    # 5
    print(get_kth_largest(items, 6))    # 1
    # print(get_kth_largest(items, 7))    # Exception
    # print(get_kth_largest(items, 0))    # Exception
    # print(get_kth_largest(items, -10))    # Exception
