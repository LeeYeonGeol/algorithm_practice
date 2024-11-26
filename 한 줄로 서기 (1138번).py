# 사람 수
N = int(input())

# 자기보다 키가 큰 사람이 왼쪽에 몇 명이 있었는지
info = list(map(int, input().split()))

orders = []
for idx, left in enumerate(info):
    orders.append((left, idx+1))

answers = [0]*N

for left, idx1 in orders:
    cnt = 0
    for idx2 in range(1, N+1):

        if cnt < left and answers[idx2-1] == 0:
            cnt += 1
        elif cnt == left and answers[idx2-1] == 0:
            answers[idx2-1] = idx1
            cnt = 0
            break
   
print(" ".join(map(str, answers)))