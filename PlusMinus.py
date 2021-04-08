'''
Plus Minus


Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  10^-4 are acceptable.

Example

arr= [1,1,0,-1,-1]

There are n=5 elements, two positive, two negative and one zero. Their ratios are 2/5 = 0.40000, 2/5 = 0.40000 and 1/5 = 020000. Results are printed as:

0.400000
0.400000
0.200000

'''

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0.0
    negative = 0.0
    zero = 0.0
    for i in arr:
        if i > 0 :
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    print("{:0.6f}".format(positive/len(arr)))
    print("{:0.6f}".format(negative/len(arr)))
    print("{:0.6f}".format(zero/len(arr)))