# creating a class
class MyList:
    list_constructor = list(("Test", "of", "Constructor"))
    print(type(list_constructor))
    list_of_names = ['Srikanth', 'Kiran', 'Aravind', 'Navya', 'SREEKANTH']
    list_with_duplicates = ['Srikanth', 'Kiran', 'Aravind', 'Srikanth', 'Kiran', 'srikanth', 'SRIKANTH', 'aravind']
    set_of_names = {'Srikanth', 'Kiran', 'Aravind', 'Srikanth', 'Kiran', 'srikanth', 'SRIKANTH', 'aravind'}
    list_of_names.remove('Srikanth')
    set_of_names.remove('Srikanth')
    list_of_names.insert(2,'Thangella')
    names_3_set = {'Srikanth', 'Kiran', 'Aravind'}
    set_2 = set_of_names.intersection(names_3_set)
    print('print duplicates:',set_2)
    names_3 = ['Srikanth', 'Kiran', 20, True]
    names_4 = [10, 20, 30, 40]
    names_5 = [True, True, False, False]

    print('Print the list of names:', list_of_names)  # print using print function
    print('Print the list with duplicates:', list_with_duplicates)
    list_of_names.append('Bharath')
    list_of_names.insert(1,'Nani')
    print('set values:', set_of_names)
    print("length of the list:", len(list_with_duplicates))
    # length = print(len(names_2))
    # print(length)
    print(list_of_names)  # indexing
    print(names_3)  # printing multiple data type at once
    print(names_4)  # printing int type
    print(names_5)  # printing boolean type
    print(type(names_3))
    print(list_constructor)

