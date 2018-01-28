# ..................................................................
# : Wind Down: Music, Movie, & Book Recs for your Psyche           :
# : B. Davis, A. M. Rahman, K. Noelsaint, G. Ren | hack@Brown '18  :
# : winddown/utilFuns.py                                           :
# : -- Contains utility functions for parsing through JSON strings,:
# :    and large dictionaries									   :
# :................................................................:

import operator
from numpy import *

def flatten(orig):
    data = {}
    for c in orig['tree']['children']:
        if 'children' in c:
            for c2 in c['children']:
                if 'children' in c2:
                    for c3 in c2['children']:
                        if 'children' in c3:
                            for c4 in c3['children']:
                                if (c4['category'] == 'personality'):
                                    data[c4['id']] = c4['percentage']
                                    if 'children' not in c3:
                                        if (c3['category'] == 'personality'):
                                                data[c3['id']] = c3['percentage']
    return data


def smallest_diff(xs):
    return (min(diff(sort(xs))))


def smallest_distance(xs):
    new = sorted(xs.values())
    want=smallest_diff(new)
    print(want)
    main_want=[]
    acc=0
    while acc!=len(new) :
        if (-1*(new[acc]-new[acc+1]))==want:
            for name,number in xs.items():
                if number==new[acc] or number==new[acc+1]:              
                    main_want.append(name)
            return (main_want)
        else:
            pass
        acc+=1


def best3(xs):
    new_xs = reversed(sorted(xs.items(), key=operator.itemgetter(1)))
    acc=0
    new_dict2= {}
    for key,value in new_xs:
        if acc==0: 
            biggest=key
        if acc<7 : 
            new_dict2[key]=value
        else:
            break
        acc+=1
    print(biggest)
    del new_dict2[biggest]
    distance=smallest_distance(new_dict2)
    distance.append(biggest)
    return distance


def best6(xs):
    new_xs= reversed(sorted(xs.items(), key=operator.itemgetter(1)))
    acc=0
    new_dict2={}
    for key,value in new_xs:
        if acc<6 : 
            new_dict2[key]=value
        else:
            break
        acc+=1
    return new_dict2.keys()

def sort_by_value(dict):
    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
    return sorted_dict


def locator ( dictionary, xs ):
    for key, value in dictionary.items():
        if value==xs:
            return key