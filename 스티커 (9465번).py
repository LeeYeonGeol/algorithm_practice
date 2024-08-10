T = int(input())
for _ in range(T):
    N = int(input())

    sticker = []
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for k in range(N):
        sticker.append((a[k], b[k]))
    dp = [[0, 0] for _ in range(N)]
    dp[0][0] = sticker[0][0]
    dp[0][1] = sticker[0][1]

    for k in range(1, N):
        # 순서대로 진행
        dp[k][0] = dp[k-1][1]+sticker[k][0]
        dp[k][1] = dp[k-1][0]+sticker[k][1]

        # 한칸씩 띄우면서
        if k >= 2:
            dp[k][0] = max(dp[k][0], max(dp[k-2])+sticker[k][0])
            dp[k][1] = max(dp[k][1], max(dp[k-2])+sticker[k][1])

    print(max(dp[-1]))
