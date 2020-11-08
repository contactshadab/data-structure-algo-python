'''
Source: AlgoExpert
Write a function that takes in an array of unique integers and returns its powerset. 
The powerset P(X) of a set X is the set of all subsets of X.
For example, the powerset of [1,2] is [[], [1], [2], [1,2]].
Note that the sets in the powerset do not need to be in any particular order. 

Input: [1, 2, 3]
Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]] 
'''


# Time Complexity: O(n*2^n), Space complexity: O(2^n)
def powerset(array, i=None):
    # First time this function is called i will not be provided by the user.
    if i is None:
        i = len(array)-1

    if i == -1:
        return [[]]

    current = array[i]
    subsets = powerset(array, i-1)
    for i in range(len(subsets)):
        subset = subsets[i]
        subsets.append([current] + subset)

    return subsets


# Time Complexity: O(n*2^n), Space complexity: O(2^n)
def powerset_iterative(array):
    subsets = [[]]
    for item in array:
        temp = []
        for subset in subsets:
            temp.append(subset + [item])
        subsets = subsets + temp

    return subsets


if __name__ == "__main__":
    print(powerset([1, 2, 3]))
    print(powerset_iterative([1, 2, 3]))
