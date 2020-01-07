import sys
sys.setrecursionlimit(10000)
def number(n):
	if(n==1000):
		return n
	else:
		return number(n+1)

