# -*- coding: utf-8 -*-
#==============================================================================
# import math
# 
# 
# def is_palindrome(obj):
#     obj_ = list(str(obj))
#     half_ = math.floor(len(obj_)/2)
#     h1 = obj_[:half_]
#     h2 = obj_[-half_:]
#     h2.reverse()
#     return h1 == h2
#==============================================================================


def is_palindrome_(obj):
    return hash(str(obj)) == hash(str(obj)[::-1])


if __name__ == '__main__':
    tests = ['saippuakivikauppias', 1011, 11233211, 12564812]
    obj = tests[0]
    for i in tests:
        print(' Test: {i} {p}is palindrome.'.format(i=i, p=('' if is_palindrome_(i) else 'not ')))

#==============================================================================
# str="Pyt1hon" # initial string
# stringlength=len(str) # calculate length of the list
# slicedString=str[(len(str)//::-1] # slicing 
# print (slicedString) # print the reversed string
#==============================================================================
