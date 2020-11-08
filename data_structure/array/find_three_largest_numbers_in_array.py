# Run time complexity: O(n), Space complexity: O(1)

def findThreeLargestNumbers(array):
    result = [None, None, None]
    for num in array:
        for i in range(2, -1, -1):
            if result[i] is None or num > result[i]:
                insert(result, i, num)
                break

    return result


def insert(array, i, num):
    for j in range(0, i):
        array[j] = array[j+1]
    array[i] = num


if __name__ == "__main__":
    result = findThreeLargestNumbers(
        [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7])
    print(result)
