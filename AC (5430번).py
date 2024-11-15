# R - 뒤집기, D - 버리기

T = int(input())
answers = []
for _ in range(T):
    now = 1 # 1: 그대로 -1:반대로
    error_flag = 0
    funcs = list(input())
    num = int(input())

    arr = input()

    if arr == '[]':
        arr = []
    else:
        arr = list(map(int,arr[1:-1].split(',')))

    idx1 = 0
    idx2 = num

    # 함수 순서대로 진행
    for func in funcs:
        if func == 'R':
            now = -now
        else:
            if idx2-idx1 <= 0:
                answers.append('error')
                error_flag = 1
                break
            else:
                if now == 1:
                    idx1 += 1
                else:
                    idx2 -= 1

    if error_flag == 1:
        continue

    if now == 1:
        answers.append(arr[idx1:idx2])
    else:
        answers.append(arr[idx1:idx2][::-1])

# 답 출력
for answer in answers:
    if answer == 'error':
        print(answer)
    elif answer == []:
        print(answer)
    else:
        answer2 = '['
        last_number = len(answer)
        for idx, ans in enumerate(answer):
            answer2 += str(ans)
            if idx  == last_number-1:
                answer2 += ']'
                continue 
            answer2 += ','

        print(answer2)