names_list = ['sriknath', 'Aravind','Russ', 'aravind', 'Suchi', 'Aravind']
#names_list2 = ['Thangella','Akula']

#https://www.geeksforgeeks.org/how-to-replace-values-in-a-list-in-python/
for i in range(len(names_list)):
    if names_list[i] == 'Aravind':
        names_list[i] = 'Aravind Thangella'

    if names_list[i] == 'aravind':
        names_list[i] = 'aravind Thangella'


print('the output:', names_list)

# for x in names_list:
#     for y in names_list2:
#         print("printing from for loop",x,y)

# print("before", names_list)
# names_list[0] = 'Srikath Akula'
# print("after", names_list)