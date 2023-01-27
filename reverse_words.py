def reverse_words(s):
    return s[::-1]


test = 'je fais un test'
print(test)
print (test[0:1:1])
print (test[0:2:1])
print (test[0:5:1])
print (test[3:8:1])
print (test[::-1])


def reverse_a_string_more_slowly(my_string):
    new_string = []
    index = len(my_string)
    while index:
        index -= 1
        new_string.append(my_string[index])
    return ''.join(new_string)


print(reverse_a_string_more_slowly(test))
