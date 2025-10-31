def change_bullet_style(document):
    splitted_string = document.split("\n")
    replaced = map(convert_line, splitted_string)
    return "\n".join(replaced)


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
