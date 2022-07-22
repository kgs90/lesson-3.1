from random import randint
import math

def get_numbers(n, frst, last):
    return [randint(frst, last) for i in range(n)]

def mult_pairs(mylist):
    return [mylist[i] * mylist[-i - 1] for i in range(math.ceil(len(mylist)/2))]

n = 9
frst = 1
last = 10

mylist = get_numbers(n, frst, last)
print(mylist)
print(mult_pairs(mylist))