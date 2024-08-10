N = int(input())

stars = []

for n in range(N):
    blank = N - (n+1)
    stars.append(' '*blank + '*'*(n+1))

for star in stars:
    print(star)