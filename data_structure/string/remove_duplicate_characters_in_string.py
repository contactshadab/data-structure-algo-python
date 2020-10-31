
def remove(str):
    if str is None:
        raise Exception('Illegal argument')

    seen = set()
    result = []
    for ch in str:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)

    return ''.join(result)


if __name__ == "__main__":
    print(remove("ABCD!!abcd???AD!!"))  # ABCD!abcd?
    print(remove("!"))  # !
    print(remove(""))  # Empty string
