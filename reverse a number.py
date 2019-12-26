input1 =  int(input())
sum = 0
while(input1!= 0):
    sum = sum * 10 + input1%10

    input1 = input1 // 10

print(sum)