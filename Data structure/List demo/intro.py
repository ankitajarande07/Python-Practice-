#1. Structure: Denoted by []
li = [10, 50, 30, 20]

#2. Types of data: Heterogeneous
li = [10, 3.14, 'abc']

#3. Sequence: Ordered
li = [20, 11.1, 'xyz']

#4. Changable:  Mutable
print(id(li))
li[0] = 30
print(id(li))
print(li)

#5. Douplication: Allowed
li = [10, 10, 20, 10, 30, 20]
print(li) 