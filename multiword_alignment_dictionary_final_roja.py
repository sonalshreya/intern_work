#!/usr/bin/env python
# coding: utf-8

# In[62]:

# RUN: python multiword_alignment_dictionary_final_roja.py <computer_science_multi_dic.txt> <computer_science_dict.txt> <Output-file>  <default-dic_path>
# Ex:  python multiword_alignment_dictionary_final_roja.py computer_science_multi_dic.txt  output $HOME_anu_test/Anu_data/canonical_form_dictionary/dictionaries/default-iit-bombay-shabdanjali-dic_smt.txt

import re
import string
import sys

default_dic = {}


def make_lists_from_single_word_dictionary(dict2):
    with open(dict2, "r+") as ins:
        array = []
        lines = ins.readlines()
    desired_lines = lines[0:]
    for line in desired_lines:
        if line[0] != '#':
            array.append(line)
    # print(array)
    ewords1 = []
    hwords1 = []
    ewords = []
    hwords = []
    hwords2 = []
    for i in array:
        str1 = i.split('\t')
        ewords1 += str1[::2]  # list slicing
        hwords1 += str1[1::2]  # list slicing
        #ewords = [x.lower() for x in ewords]
    # print(ewords1)
    for m in hwords1:
        m = m.strip('\n')
        hwords2.append(m)
    for n in ewords1:
        n = n.strip('_noun')
        ewords.append(n)
    list1 = []
    for k in hwords2:
        list1 = k.split('/')
        hwords.append(list1)
    # print(hwords)
    return ewords, hwords


def make_lists_from_multi_word_dictionary(dict1):
    with open(dict1, "r+") as ins:
        array = []
        lines = ins.readlines()
    desired_lines = lines[0:]
    for line in desired_lines:
        if line[0] != '#':
            array.append(line)
    # print(array)
    ewords1 = []
    hwords1 = []
    ewords = []
    hwords = []
    hwords2 = []
    d = ""
    for i in array:
        str1 = i.split('\t')
        ewords1 += str1[::2]  # list slicing
        hwords1 += str1[1::2]  # list slicing
        ewords = [x.lower() for x in ewords1]
    # print(ewords)
    for j in hwords1:
        d = ""
        for k in j:
            if k != '#':
                d = d+k
            elif k == '#':
                break
        hwords.append(d)
    # print(ewords1)
    list1 = []
    list2 = []
    for n in ewords1:
        list1 = n.split('_')
        list2.append(list1)
    # print(list2)
    # hwords2=[]
    # for i in hwords:
        #str=i.replace('_',' ')
        # hwords2.append(str)
    # print(hwords)
    return list2, hwords


# make_lists_from_multi_word_dictionary()
# make_lists_from_single_word_dictionary()


def meaning_of_every_word_seperately(dict1, dict2):
    elist, hlist = make_lists_from_multi_word_dictionary(dict1)
    elist1, hlist1 = make_lists_from_single_word_dictionary(dict2)
    list2 = []
    list3 = []
    for i in elist:
        # print(i)
        list1 = []
        str1 = ""
        for j in i:
            c = 0
            for m in elist1:
                if j == m:
                    # print("true")
                    x = elist1.index(m)
                    y = elist.index(i)
                    for k in hlist1[x]:
                        # print(k)
                        if k in hlist[y]:
                            list1.append(m+":"+k)
                            c += 1
                            # print(str1)

            if c == 0:
                list1.append(j+":"+"?")
                #str1=str1.join(j+" <> "+"?"+" ")
        list2.append(list1)
        #eng = '_'.join(i)
        #list2.append(eng + '\t' + ' '.join(list1))
    for i in list2:
        str1 = " ".join(i)
        list3.append(str1)
    # print(list2)
    return list3


input_dict1 = sys.argv[1]
input_dict2 = sys.argv[2]

output_dict = sys.argv[3]


# Added below code by Roja
#f = open(sys.argv[4], 'r').readlines()


# Creating dic:


# converting_dictionaries_into_list()
output = meaning_of_every_word_seperately(input_dict1, input_dict2)
with open(output_dict, "w") as out:
    for i in output:
        # print(i)
        out.write(i+"\n")


# converting_dictionaries_into_list()
# meaning_of_every_word_seperately("/home/user/anusaaraka/Anu_data/compound-matching/tech_sample.txt")
