input = int(input())
sum = 0
temp = 0
i = 1
while(input != 0):
    temp = sum
    sum = sum +i
    i = temp
    input -= 1
    print(sum)