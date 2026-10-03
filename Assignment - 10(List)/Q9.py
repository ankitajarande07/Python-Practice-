#9. Write a program of having n number of elements in the list and find out even
#   and odd elements in that list and then create two separate lists which will have
#   even elements and other will have odd elements.


li = [13,25,22,10,36,51,740]

even = []
odd = []

for i in li:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)


print("Even Elements:", even)
print("Odd Elements:", odd)