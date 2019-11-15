#!/usr/bin/env python
# coding: utf-8

# In[64]:


import re
import string
import sys


def remove_bracket(dict):
    with open(dict, "r+") as ins:
        array = []
        lines = ins.readlines()
        desired_lines = lines[0:]
        for line in desired_lines:
            if line[0] != '#':
                array.append(line)
    # print(array)
    ewords1 = []
    hwords1 = []
    for i in array:
        str1 = i.split('\t')
        ewords1 += str1[::2]  # list slicing
        hwords1 += str1[1::2]  # list slicing
    # print(ewords1)
    for i in ewords1:
        if '(' in i:
            k = i.index('(')
            s = len(i)
            j = i[k+2:s-2]
            # print(j)
            l = i[0:k-1]
            n = ewords1.index(i)
            # i.replace(i,l)
            # print(i)
            # ewords[n]=l
            # ewords.append(j)
            m = hwords1[n]
            # print(m)
            str = l+"\t"+m
            array[n] = str
            g = 0
            for k in j:
                if k >= 'a' and k <= 'z':
                    g = j.index(k)
                    break
            array.append(j[g:]+"\t"+m)
    # print(array)
    array.sort()
    return array
    # print(ewords1)


input_dict = sys.argv[1]
#input_dict1 = sys.argv[2]
output_dict = sys.argv[2]
# converting_dictionaries_into_list()
output = remove_bracket(input_dict)
with open(output_dict, "w") as out:
    for i in output:
        out.write(i)

# remove_bracket("/home/user/anusaaraka/Anu_data/domain/multi_word_dic/sample2")


# In[ ]:
