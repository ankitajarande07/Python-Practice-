#7. Python program to find the intersection of two lists.

li1 = [10,20,30,40,50]
li2 = [40,10, 60,70,80]

intersection = list(set(li1) & set(li2))

print(intersection)

