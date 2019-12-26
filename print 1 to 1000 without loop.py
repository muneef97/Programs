import sys
sys.setrecursionlimit(10000)

def print_numbers(n):
    if(n == 0):
        return n
    else:
        print(n)
        return print_numbers(n-1)

a = int(input())
print_numbers(a)