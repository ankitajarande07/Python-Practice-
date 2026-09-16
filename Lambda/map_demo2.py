def add(n1, n2):
    return n1 + n2

data = [1,2,3,4,5,6,7,8,9,10]
data2 = [1,2,3,4,5,6,7,8,9,10]

res = list(map(add, data, data2, data, data))
print(res)