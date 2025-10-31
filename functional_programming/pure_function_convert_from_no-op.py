doc = """I *love* Markdown.
I **really love** Markdown.
I ***really really love*** Markdown."""


def remove_emphasis(doc):
    #     global doc
    #     lines = doc.split("\n")
    #     new_lines = map(remove_line_emphasis, lines)
    #     doc = "\n".join(new_lines)
    new_doc = doc
    lines = new_doc.split("\n")
    new_lines = map(remove_line_emphasis, lines)
    new_doc = "\n".join(new_lines)
    return new_doc


# Don't touch below this line


def remove_line_emphasis(line):
    words = line.split()
    new_words = map(remove_word_emphasis, words)
    return " ".join(new_words)


def remove_word_emphasis(word):
    return word.strip("*")
