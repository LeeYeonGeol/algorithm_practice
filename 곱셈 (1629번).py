import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def power(a, n, c):
    if n == 1:
        return a % c
    else:
        x =  power(a, n//2, c)

        # n이 짝수일 때
        if n % 2 == 0:
            return x * x % c
        # n이 홀수일 때
        else: 
            return x * x * a % c
    
print(power(A, B, C))