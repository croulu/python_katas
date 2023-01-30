def create_phone_number(n):
    return "(" + str(n[0]) + str(n[1]) + str(n[2]) + ") " + str(n[3]) + str(n[4]) + str(n[5]) + "-" + str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])

def create_phone_number_2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number_3(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

def create_phone_number_4(n):
    str1 =  ''.join(str(x) for x in n[0:3])
    str2 =  ''.join(str(x) for x in n[3:6])
    str3 =  ''.join(str(x) for x in n[6:10])
    return '({}) {}-{}'.format(str1, str2, str3)
