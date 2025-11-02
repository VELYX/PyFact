def find_longest_word(document, longest_word=""):
    # Trim trailing white space
    document = document.lstrip()

    # If the document is empty return longest word
    if not document:
        return longest_word

    # Split the document
    parts = document.split(maxsplit=1)

    # Assign the split word for easy handling, this will also assign the last word for comparison
    first = parts[0]

    # Compare word lengths
    if len(first) > len(longest_word):
        longest_word = first

    # Return if this is the last word
    if len(parts) == 1:
        return longest_word

    # Call function recursively
    return find_longest_word(parts[1], longest_word)
