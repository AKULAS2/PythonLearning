''#Author: Srikanth Akula
#Date: 08-09-2022
#This program is used to just to print some values
#using some methods
statement1 = 'python $ coding makes job life  esay and simple tree'
statement2 = 'Amazon web services is in India'
statement3 = 'Accenture is the best company in the world'

#Printing the statement1 outside the fuction without using funtion call
output = statement1.split('$')
print(output)
print('calling from out of the function:', statement1.split('%'))
print(type(statement1.split('$')))
print('calling from out of the function:', type(statement1.split()))
print('calling from out of the function:', len(statement1.split('$')))

#Printing the statement2 outside the fuction without using funtion call
print('India' in statement2)
print('AWS' in statement2)
print('Testing:', statement2[3], statement2[7] )
if "India" in statement2:
    print("Yes! it is present in the string")
else:
    print("No! it is not present")

#Printing the statement3 outside the fuction without using funtion call
print('Converting the statement3 to uppercase:', statement3.upper())


# create a sentance and find out number of words in the sentance.
def count_sentence(sent):
    sentence = 'python coding makes job life esay and simple'
    print(sentence)#python coding makes job life esay and simple
    if "India" in statement2:
        print("Yes! it is present in the string")#Yes! it is present in the string
    else:
        print("No! it is not present")
    result = sent
    return result


#finding the length and number of word in the sentence
length_of_sentence = count_sentence(statement1)#'python coding makes job life esay and simple'
print('Length of sentence=', len(length_of_sentence))#44
print('number of words in statement are:', len(length_of_sentence.split()))#8


# search = count_sentence(statement2)
# print(search.find())

#fining the words in the sentence
length_of_sentence = count_sentence(statement2)
print('India' in statement2)
print('AWS' in statement2)
print('Print using Contains funtion: ', length_of_sentence.__contains__('AWS'))

#converting the sentence to Upper case letters
length_of_sentence = count_sentence(statement3)
print('Converting the statement3 to uppercase:', length_of_sentence.upper())
