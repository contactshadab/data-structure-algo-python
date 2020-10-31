# Unlike linear search we will not iterate over each element.
# We will divide the array in some blocks and keep jumping to the right block that may contain the target value
# In that block we'll do linear search
# Optimum size of the block is Sqrt(n) which can be proven mathematically but is beyond the scope of this excercise.
# Run time complexity: O(sqrt(n)), Space complexity: O(1)

from math import sqrt


def block_search(items, target):
    block_size = (int)(sqrt(len(items)))
    start = 0
    next = block_size
    while start < len(items) and target > items[next-1]:
        start = next
        # Advance next by next block but also reset it to last item in the array if it passes the array length
        next = min(next + block_size, len(items))

    # Search this block
    while start < next:
        if target == items[start]:
            return start

        start += 1

    return -1


if __name__ == "__main__":
    items = [-10, 0, 10, 20, 30]
    print(block_search(items, -10))  # 0
    print(block_search(items, 30))  # 4
    print(block_search(items, 0))  # 1
    print(block_search(items, 100))    # -1
    print(block_search([10], 10))    # 0
    print(block_search([], 10))    # -1
