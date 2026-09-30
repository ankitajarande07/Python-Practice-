# WAP to find the maximum number...

li = [34, 57, 83, 42, 23, 53, 65]

max = li[0]
for i in range(1, len(li)):
    if(li[i] > max):
        max = li[i]
print('Maximum number:', max)   


# WAP to find the second maximun number...

li =[34, 57, 83, 42, 23, 53, 65]

maximun = li[0]
second_maximun = li[0]

for i in li:
    if i > maximun:
        second_maximun = maximun
        maximun = i

    elif i > second_maximun and maximun:
        second_maximun = i    

print('second maximun:',second_maximun)

