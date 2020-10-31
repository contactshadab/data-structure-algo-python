def count(str):
    count = 0
    for ch in str:
        if ch in 'aeiou':
            count += 1

    return count


print(count("I have a vowel"))
print(count(""))
