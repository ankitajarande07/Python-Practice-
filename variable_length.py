def add(*num):
    sum = 0
    for val in num:
        sum += val    #sum = sum + val
    
    return sum

res = add(10, 20, 30, 40, 50)
print('Addition is:', res)

res = add(1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,6,5,4,3,2,1)
print('Addition is:', res)
