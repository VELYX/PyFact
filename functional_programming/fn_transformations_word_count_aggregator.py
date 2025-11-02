def word_count_aggregator():
    count = 0

    def word_number_calculator(doc):
        number_of_words = len(doc.split())
        nonlocal count
        count += number_of_words
        return count

    return word_number_calculator
