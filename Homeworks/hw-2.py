# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:44:30 2021

@author: LENOVO
homework-2
"""
#%%
"""
create a list and swap the second half of 
the list with the first half of the list and
 print this list on the screen
"""
list1 = list(range(0, 20))
print(list1)

#split list
list_length = len(list1) 
middle = list_length//2

list1_first = list1[:middle]
print(list1_first)

list1_second = list1[middle:]
print(list1_second)

#swap
list1_second.extend(list1_first)
print(list1_second)

#%%
""""
Ask the user to input a single digit integer
to a variable 'n'. Then print out all of the even 
numbers from 0 to n(including n)
"""
n = int(input("Please enter a single digit integer: "))
for i in range(0, n+1, 2):
    print(i)



