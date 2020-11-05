'''
Source: AlgoExpert
Write a function that takes in an array of integers and returns the length of
the longest peak in the array.
A peak is defined as adjacent integers in the array that are strictly
increasing until they reach a tip (the highest value in the peak), at which
point they become strictly decreasing. At least three integers are required to
form a peak.
Input:  [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
Output: 6 // 0, 10, 6, 5, -1, -3
'''

# Run time complexity: O(n), Space complexity: O(1)


def longest_peak(array):
    count = 0
    current = 1
    while current < len(array)-1:
        if not is_peak(array, current):
            current += 1
            continue

        left = current - 2  # We have already checked previous one in is_peak
        while left >= 0 and array[left+1] > array[left]:
            left -= 1

        right = current + 2  # We have already checked next one in is_peak
        while right < len(array) and array[right-1] > array[right]:
            right += 1

        count = max(count, right - left - 1)

        current = right

    return count


def is_peak(array, tip):
    return array[tip] > array[tip-1] and array[tip] > array[tip+1]


if __name__ == "__main__":
    result = [1, 2, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    print(longest_peak(result))
