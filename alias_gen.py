FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', 'D': 'Data', 'F': 'Function', 'H': 'Half-life',
              'M': 'Malware', 'W': 'WiFi'}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst', 'K': 'Killer', 'M': 'Mike', 'P': 'Payload',
           'T': 'T-Rex', 'W': 'Worm'}


def alias_gen(complete_name):
    result = ''
    for v in complete_name:
        print (v)

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


def map_complete_name(fisrt_name_to_change, last_name_to_change):
    result = ''
    fisrt_name = find_alias(fisrt_name_to_change, FIRST_NAME)
    last_name = find_alias(last_name_to_change, SURNAME)

    if fisrt_name == 'NotAStr' or last_name == 'NotAStr':
        result = 'Your name must start with a letter from A - Z.'
    else:
        result = fisrt_name + ' ' + last_name

    return result
