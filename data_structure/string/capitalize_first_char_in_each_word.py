'''
Capitalize the first letter of each word in a sentence. Also, remove any
extra spaces between words.
Input: “trees are beautiful”
Output: “Trees Are Beautiful”
Input: “ trees are beautiful ”
Output: “Trees Are Beautiful”
'''
import re


def capitalize(text):
    if text is None:
        raise Exception('illegal Argument')

    clean_text = re.sub(r' +', ' ', text).strip()
    # If it is empty string after trimming whitespaces
    if not clean_text:
        return ""

    # Replace multiple spaces with one
    words = re.sub(r" +", ' ', clean_text).split(' ')
    for i in range(len(words)):
        # Check empty words in case of multiple consecutive spaces
        if not words[i]:
            continue

        words[i] = words[i][0].upper() + words[i][1:].lower()

    return ' '.join(words)


if __name__ == "__main__":
    print(capitalize("   can you tRy  to capatalize me   "))
    print(capitalize("   "))    # Empty string
