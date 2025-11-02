def count_nested_levels(nested_documents, target_document_id, level=1):
    # If the nested_documents is empty return -1
    if not nested_documents:
        return -1

    # Loop through the dictionary
    for document in nested_documents:
        # print(document, target_document_id)

        # If the current document matches the target, return it's level
        if document == target_document_id:
            # print(f"match found at {level}")
            return level

        # Assign the value of the recursive call to a variable
        found = count_nested_levels(
            nested_documents[document], target_document_id, level + 1
        )

        # If the return of the recursion is not -1 then return the recursion value
        if found != -1:
            return found

    return -1
