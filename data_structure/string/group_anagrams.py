'''
Source: AlgoExpert

Write a function that takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't
matter.
Input:  = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
Output: [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
'''

# Solution 1
# Run time complexity: O(w * nlog(n) + nwlog(w)) where n is the no of characters in largest word and w is the no orwords
# Space complexity: O(w*n)


def group_anagrams_1(words):
    if len(words) == 0:
        return []

    sorted_words = [''.join(sorted(w)) for w in words]
    sorted_indices = [i for i in range(len(sorted_words))]
    sorted_indices.sort(key=lambda i: sorted_words[i])

    results = []
    anagrams = [words[sorted_indices[0]]]
    previous = sorted_words[sorted_indices[0]]
    for i in range(1, len(sorted_indices)):
        word = words[sorted_indices[i]]
        sorted_word = sorted_words[sorted_indices[i]]
        if sorted_word == previous:
            anagrams.append(word)
            continue

        results.append(anagrams)
        anagrams = [word]
        previous = sorted_word

    # If we come out of loop we still have anagrams to push to result
    results.append(anagrams)

    return results

# Solution 2
# Run time complexity: O(w * nlog(n)) where n is the no of characters in largest word and w is the no orwords
# Space complexity: O(w*n)


def group_anagrams_2(words):
    if len(words) == 0:
        return []

    anagrams = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
            continue

        anagrams[sorted_word] = [word]

    return list(anagrams.values())


if __name__ == "__main__":
    print(group_anagrams_1(
        ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))
    print(group_anagrams_2(
        ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))
