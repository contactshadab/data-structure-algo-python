'''
Source: AlgoExpert
Write a function that takes in a "special" array and returns its product sum. 
A "special" array is a non-empty array that contains either integers or other "special" arrays.
The product sum of a "special" array is the sum of its elements, where "special" arrays inside it are summed themselves and then multiplied by their level of depth. 
The depth of a "special" array is how far nested it is. For instance, the depth of [] is 1
The depth of the inner array in [[]] is 2
The depth of the innermost array in [[[]]] is 3
Input  = [5, 2, [7, -1], 3, [6, [-13, 8], 4]] 
Output = 12
'''


def product_sum(array, level=1):
    sum = 0
    for i in range(len(array)):
        if type(array[i]) is int:
            sum += array[i]
            continue

        sum += product_sum(array[i], level + 1)

    return sum * level


if __name__ == "__main__":
    print(product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
