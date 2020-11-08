# Solution 1
# Total Run time complexity: O(n^2.n!), Space complexity: O(n.n!)
def get_permutations(array):

    if len(array) == 0:
        return []

    return _get_permutations(array, [], [])


# Helper method - Run time complexity: O(n^2.n!), Space complexity: O(n.n!)
def _get_permutations(array, permutation, permutations):

    if len(array) == 0:
        permutations.append(permutation)
        return

    for num in array:
        new_permutation = permutation + [num]
        remaining_list = array[0:]
        remaining_list.remove(num)
        _get_permutations(remaining_list, new_permutation, permutations)

    return permutations


# Solution 2
# Total Run time complexity: O(n.n!), Space complexity: O(n.n!)
def get_permutations_2(array):
    permutations = []
    _get_permutations_2(0, array, permutations)

    return permutations


def _get_permutations_2(i, array, permutations):
    if i == len(array)-1:
        permutations.append(array[:])
        return

    for j in range(i, len(array)):
        swap(array, i, j)
        _get_permutations_2(i+1, array, permutations)
        swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


if __name__ == "__main__":
    print(get_permutations([1, 2, 3]))
    print(get_permutations([]))
    print(get_permutations_2([1, 2, 3]))
    print(get_permutations_2([]))
