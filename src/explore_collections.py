# collection

# list
names_list = ['ravi', 'aryaman', 'arjun', 'ravi', 'Srikanth']
different_list = ['Sreekanth', 12, 12.0, True]
# set
names_set = {'ravi', 'arjun', 'aryaman', 'ravi', 'aryaman'}

print("names_list type: {0}, length: {1}", type(names_list), len(names_list))
print("names_list type: {0}, length: {1}", type(names_set), len(names_set))
print('Printing list using print function:', *names_list)
print('Printing set using print function:', *names_set)
print('Printing set using print function:', *different_list)

print("names_list type: {0}, length: {1}".format(type(names_list), len(names_list)))
print("names_list type: {0}, length: {1}".format(type(names_set), len(names_set)))
#"names_list type: {0}, length: {1}".


for x in range(len(names_list)):
    print('Printing elements from list using for loop:',names_list[x])

for x in range(len(names_list)):
    print('Printing elements from list using for loop:',names_list[x])

print('-----------')

for x in range(len(names_set)):
     print('Printing elements from set using for loop:',names_list[x])

print('print afer the for loop')

for x in names_list:
    print('print list using without Range funtion:', x)

for x in names_set:
    print('print set using without Range funtion:', x)