#6. Write a program to remove duplicates from the list.

li = [10, 20, 20, 30, 40, 20, 10, 50]

new_li = []
for i in li:
    if i not in new_li:
        new_li.append(i)

print("original list:", li)
print("remove duplicate:", new_li)        