def add_length(str_):
    str_in = str_.split(' ')
    new_str = []
    for element in str_in:
        new_str.append(element + " " + str(len(element)))
    return new_str