#2. Write a program to find maximum and minimum element in a list.

li = [34, 57, 83, 42, 23, 53, 65]

max = li[0]
min = li[0]
for i in range(1, len(li)):
    if(li[i] > max):
        max = li[i]

    if(li[i] < min): 
        min = li[i]

print('Maximum number:', max)  
print('Minimum number:', min)      