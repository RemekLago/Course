from pprint import pprint

text ="Russian Foreign 23 Minister 45 2.5 Sergei Lavrov says 1.12 2.5 Moscow will send a formal response to the US on the issue of security guarantees on Ukraine"
words_list = text.split()

words_number = []
words_string = []

"""if word is number(int or float) create separate folder for it and the 
rest of text go to other folder"""
for idx in words_list:
    if idx.isnumeric():
        words_number.append(idx)
    elif idx.isalnum():
        words_string.append(idx)
    else:
        words_number.append(idx)

dict_number = {}
dict_string = {}

for word in words_number:
    if word in dict_number:
        dict_number[word] += 1
    else:
        dict_number[word] = 1

for word in words_string:
    if word in dict_string:
        dict_string[word] += 1
    else:
        dict_string[word] = 1

sorted_number = sorted(dict_number.items(),
                       key=lambda value: value[1], reverse=False)
sorted_string = sorted(dict_string.items(),
                       key=lambda value: value[1], reverse=False)

pprint(sorted_number)
pprint(sorted_string)