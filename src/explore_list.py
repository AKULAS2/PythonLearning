customer_names_list = ['Srikanth', 'Kiran', 'Aravind', 'Srikanth', 'Ravi']
customer_sur_names_list = ['Akula', 'AKula', 'Thangella', 'Srikanth', 'Itha', 'Thangella']
name_list_as_string = "Boss"

#from here I will start working with Predefind methods in List
customer_names_list.append('Navya')
#customer_names_list.clear()
customer_names_list.append('sree')
copide_list_variable = customer_names_list.copy()
count_of_list = customer_names_list.count("Srikanth")
sur_names_extends = customer_names_list.extend(customer_sur_names_list)
customer_sur_names_list.extend(name_list_as_string)
index_function_variable = customer_sur_names_list.index('Thangella')
customer_sur_names_list.insert(0,'Arjun')
customer_sur_names_list.pop(1)
customer_names_list.remove('Srikanth')
customer_sur_names_list.reverse()


#print('Print the customer_names_list variable value:', customer_names_list)
print('Print the append value:', customer_names_list)
print('Print the copy function value:', copide_list_variable)
print('Print the count function value:', count_of_list)
print('Print the extends function value:', sur_names_extends)
print('Print the extends function from string value:', customer_sur_names_list)
print('Print the index function value:', index_function_variable)
print('Print the insert function value:', customer_sur_names_list)
print('Print the Pop function value:', customer_sur_names_list)
print('Print the reverse function value:', customer_sur_names_list)
