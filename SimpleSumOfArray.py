'''
Simple Array Sum

Given an array of integers, find the sum of its elements.

For example, if the array arr = [1,2,3], 1 + 2 + 3 = 6, so return 6.

Function Description

Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

simpleArraySum has the following parameter(s):

ar: an array of integers

'''

def simpleArraySum(ar):
    sum = 0
    for i in ar:
        sum += i
    return sum