# -*- coding: utf-8 -*-

#%%Create 2 lists, the first consist of odd numbers, the second consists of even numbers
list_odd = list(range(1,20, 2))
print(list_odd)
list_even = list(range(0, 20,2))
print(list_even)

#%%merge 2 lists, and multiply all values in the list by 2
list_odd.extend(list_even)
#print(list_odd)

list_merged_doubled = list(i*2 for i in list_odd)
print(list_merged_doubled)
#%% create a loop to print the data type of all values in the new list
for i in list_merged_doubled:
    print(type(i))
