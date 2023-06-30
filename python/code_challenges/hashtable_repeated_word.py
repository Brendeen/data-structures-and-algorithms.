def first_repeated_word(string):
    if not string:
        return False

    visited = {}
    list_of_words = string.split()

    for word in list_of_words:
        if word in visited:
            return word
        else:
            visited[word] = True

    return False


if __name__ == "__main__":
    repeated_word = first_repeated_word("Bruh")

    if repeated_word:
        print("The first repeated word is:", repeated_word)
    else:
        print("No repeated words found.")
