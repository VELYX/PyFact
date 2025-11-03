def new_collection(initial_docs):
    current_docs = initial_docs.copy()

    def new_addition(string):
        nonlocal current_docs
        current_docs.append(string)
        return current_docs

    return new_addition
