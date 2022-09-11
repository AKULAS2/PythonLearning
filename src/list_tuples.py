#creating a class
class MyList:
    list_constructor = list(("Test", "of", "Constructor"))#contructor
    names = ['Srikanth', 'Kiran', 'Aravind']
    names.append('Navya')
    names_2 = ['Srikanth', 'Kiran', 'Aravind' 'Srikanth', 'Kiran', 'srikanth', 'SRIKANTH', 'aravind']
    names_2.append(names)
    #names = ['Srikanth', 'Ravi', 'Kiran', 'Aravind']
    names_3 = ['Srikanth', 'Kiran', 20, True]
    names_4 = [10, 20, 30, 40]
    names_5 = [True, True, False, False]


    print(names)#print using print function
    print(names_2)
    print("length of the list:",len(names_2))
    #length = print(len(names_2))
    #print(length)
    print(names[1])#indexing
    print(names_3)#printing multiple data type at once
    print(names_4)# printing int type
    print(names_5)# printing boolean type
    print(type(names_3))
    print(list_constructor)