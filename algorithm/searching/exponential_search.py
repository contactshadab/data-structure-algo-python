# Start with bound 2 and then keep increasing bound = bound*2 if the element is greater than bound

def exponential_search(items, target):
    bound = 1
    while bound < len(items) and target > items[bound]:
        bound *= 2

    # Do a binary seach between previoud and current bound
    left = bound // 2
    # Reset current bound if it falls outside of array
    right = min(bound, len(items)-1)
    while left <= right:
        mid = (left+right) // 2
        if items[mid] == target:
            return mid

        if target < items[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__ == "__main__":
    items = [-10, 0, 10, 20, 30]
    print(exponential_search(items, -10))  # 0
    print(exponential_search(items, 30))  # 4
    print(exponential_search(items, 0))  # 1
    print(exponential_search(items, 100))    # -1
    print(exponential_search([10], 10))    # 0
    print(exponential_search([], 10))    # -1
