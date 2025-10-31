def remove_invalid_lines(document):
    lines = document.split("\n")
    filtered_lines = "\n".join(filter(lambda x: not x.startswith("-"), lines))
    return filtered_lines
