import functools


def join(doc_so_far, sentence):
    print(f"doc_so_far: {doc_so_far}, sentence: {sentence}")
    return doc_so_far + ". " + sentence


def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    final_string = f"{functools.reduce(join, sentences[:n])}."
    return final_string
