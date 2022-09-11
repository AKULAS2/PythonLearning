first_name = 'Srikanth'
last_name = 'Akula'
second_fname = 'Ravi'
second_last = 'Itha'
i = 'Test'
j = 20
l = 30


def add_name_original(fname, lname):
    result = fname + ' ' + lname
    sum = 10 + 20
    print(sum)
    return result


def add_name(fname, lname):
    result = ' '.join([fname, lname])
    return result


def add_name2(i, j, l):
    result = ' '.join(map(str, [i, j, l]))
    return result



full_name = add_name_original(first_name, last_name)
print('Type of full_name:', type(full_name))
print('Type of 100 value:', type(100))
print('Type of 100.237 value:', type(100.237))
print('Name:', full_name)

name = add_name(second_fname, second_last)
print('Name:', name)

k = add_name2(i, j, l)
print('sum of two number:', k)

full_name = add_name(first_name, last_name)
print('Name:', full_name)
print('Length:', len(full_name))



