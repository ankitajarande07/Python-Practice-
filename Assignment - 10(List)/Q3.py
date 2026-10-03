#3. Write a program to find the second largest element in the list.

li = [34, 57, 83, 42, 23, 53, 65]

largest = li[0]
second_largest = li[0]

for i in li:
    if i > largest:
        second_largest = largest
        largest = i

    elif i > second_largest and largest:
        second_largest = i    

print('second largest:',second_largest)

