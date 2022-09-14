animals_tuples = ('Tiger','dog', 'fish', 'lion', 'Hen', 'Goat')
single_tuple = ('Srikanth',)
single_tuple2 = ('Srikanth')


if 'Tiger' in animals_tuples:
    print('Yes, I am here in the tuples')


#Convert the tuple to list
converted_tuple = list(single_tuple2)
print("type of converted_tuple variable:", type(converted_tuple))
print("print of converted_tuple variable:", converted_tuple)
print("type of converted_tuple variable:", len(converted_tuple))



print('printing type of variable:', type(animals_tuples))
print('printing length of variable:', len(animals_tuples))
print('printing type of variable:', type(single_tuple))
print('printing type of variable:', type(single_tuple2))
print('print the single_tuple variable:', single_tuple)
print('print the single_tuple variable:', single_tuple2)
print('printing by index of variable:', (animals_tuples[:6]))