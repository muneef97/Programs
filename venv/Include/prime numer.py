input = int(input())
c = 0
a = 3
if (input == 1 or input == 2):
    print("no prime numbers")
    exit(0)
while(a!= input+1):
    c = 0
    for i in range(2,a):
        if((a%i)==0):
            c += 1
    if(c == 0):
        print(a)
    a += 1