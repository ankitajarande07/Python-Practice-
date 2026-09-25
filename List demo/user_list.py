def createList(li):
    n = int(input('How many element you want add:'))
    for i in range(n):
        ele = int(input('enter element:'))
        li.append(ele)

li = []
createList(li)
print(li)        