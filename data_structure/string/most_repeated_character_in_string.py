'''
Find the most repeated character in a string.
Input: “Hellooo!!”
Output: ‘o’ 
'''


def most_repeated(str):
    if str is None:
        raise Exception('Illegal argument')

    _ASCII_SIZE = 256
    frequencies = [0] * _ASCII_SIZE
    for ch in str:
        frequencies[ord(ch)] += 1

    max_frequency_index = 0
    for i in range(len(frequencies)):
        if frequencies[i] > frequencies[max_frequency_index]:
            max_frequency_index = i

    return chr(max_frequency_index)


if __name__ == "__main__":
    print(most_repeated("Hellooo!!"))  # o
    print(most_repeated("Hellooo!!!"))  # !, which one has lower ASCII
    print(most_repeated(""))  # Empty string
    # print(most_repeated(None))  # Exception: Illegal argument
