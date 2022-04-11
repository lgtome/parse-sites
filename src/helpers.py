whitespace_regex = '\s'


def convert_to_tuple(list):
    return tuple(list)


def space_transforme(tupled, symbol: str):
    return f'{symbol}'.join(tupled)


def link(uri, label=None):
    if label is None:
        label = uri
    parameters = ''

    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)
