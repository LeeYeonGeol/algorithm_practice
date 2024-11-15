N = int(input())

arr = [list(map(int, input().split(' '))) for _ in range(N)]
    
global answer 
answer_1 = 0
answer_2 = 0

def dfs(x1, y1, x2, y2, num):
    global answer_1 
    global answer_2

    # 하나인 경우
    if  x2-x1 == 1:
        if arr[x1][y1]:
            answer_2 += 1
        else:
            answer_1 += 1
        return
    
    # 그 외 -> 전체가 1인지 확인
    cnt = 0
    for idx in range(x1, x2):
        cnt += sum(arr[idx][y1:y2])
    
    if cnt == (x2-x1)**2:
        answer_2 += 1
        return
    elif cnt == 0:
        answer_1 += 1
        return
    else:
        new_num = num//2
        dfs(x1, y1, x2-new_num, y2-new_num, new_num)
        dfs(x1, y1+new_num, x2-new_num, y2, new_num)
        dfs(x1+new_num, y1, x2, y2-new_num, new_num)
        dfs(x1+new_num, y1+new_num, x2, y2, new_num)

dfs(0, 0, N, N, N)

print(answer_1)
print(answer_2)