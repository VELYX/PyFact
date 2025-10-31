def add_format(default_formats, new_format):
    # default_formats[new_format] = True
    new_default = default_formats.copy()
    new_default[new_format] = True
    return new_default


def remove_format(default_formats, old_format):
    # default_formats[old_format] = False
    new_default = default_formats.copy()
    new_default[old_format] = False
    return new_default
