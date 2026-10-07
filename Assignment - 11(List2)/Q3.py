#3. Python Program to Sort the List According to the Second Element in Sublist.

li = [[1,20], [2,50], [3,10], [4,40], [5,30]]

li.sort(key = lambda x:x[1])

print('sort list:', li)