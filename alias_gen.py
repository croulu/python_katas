FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', 'D': 'Data', 'F': 'Function', 'H': 'Half-life',
              'M': 'Malware', 'W': 'WiFi'}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst', 'K': 'Killer', 'M': 'Mike', 'P': 'Payload',
           'T': 'T-Rex', 'W': 'Worm'}


def alias_gen(f_name, l_name):
    result = ''
    fisrt_name = find_alias(f_name, FIRST_NAME)
    last_name = find_alias(l_name, SURNAME)

    if fisrt_name == 'NotAStr' or last_name == 'NotAStr':
        result = 'Your name must start with a letter from A - Z.'
    else:
        result = fisrt_name + ' ' + last_name

    return result


def first_letter_in_uppercase(name):
    result = ''
    if name[0].isalpha():
        result = name[0].upper()
    else:
        result = 'NotAStr'

    return result


def find_alias(to_find, mapping):
    result = ''
    first_letter = first_letter_in_uppercase(to_find)
    if first_letter != 'NotAStr':
        result = mapping[first_letter]
    else:
        result = 'NotAStr'

    return result
