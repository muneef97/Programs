list = [0,1,1,0,1,0,0,1,1,1,0,0,0,1]
list1 = []
zero_count = 0
one_count = 0
for i in range(len(list)):
    if(list[i]==0):
        zero_count += 1
    elif(list[i]==1):
        one_count += 1
for i in range(zero_count):
    list1.append(0)
for i in range(one_count):
    list1.append(1)

print(list1)