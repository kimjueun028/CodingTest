import sys
input = sys.stdin.readlines
user_input = input()

n = int(user_input[0])
arr = [0] + list(map(int, user_input[1].split()))
# i개가 들어있는 카드팩 가격
# [0,1,5,6,7]
dp = [0] *(n+1)
# 카드 i개 구매하는 최대 비용 저장
# [0,0,0,0,0]
for i in range(1, n+1): 
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+arr[j])
    
print(dp[n])

    # 카드 1개 구매할때 최대 비용 dp[1]
    # i = 1 / j = 1
    # dp[1] = max(dp[1], dp[0]+arr[1]) = max(0, 0+1) = 1** 
    # -> 카드팩1 1개

    # 카드 2개 구매할때 최대 비용 dp[2]
    # i = 2 / j = 1, 2
    # dp[2] = max(dp[2], dp[1]+arr[1]) = max(0, 1+1) = 2 -> 카드팩1 2개
    # 카드 1개 구매한 거에 추가로 하나 더 구매 
    # dp[2] = max(dp[2], dp[0]+arr[2]) = max(2, 0+5) = 5** -> 카드팩2 1개
    # 그거와 별개로 2개짜리 구매하는 경우

    # 카드 3개 구매할때 최대 비용 dp[3]
    # i = 3 / j = 1,2,3
    # dp[3] = max(dp[3], dp[2]+arr[1]) = max(0, 5+1) = 6 -> 카드팩2 1개, 카드팩1 1개
    # 카드 2개 구매한 거에 추가로 하나 더 구매
    # dp[3] = max(dp[3], dp[1]+arr[2]) = max(6, 1+5) = 6 -> 카드팩1 1개, 카드팩2 1개
    # 같은 상황
    # dp[3] = max(dp[3], dp[0]+arr[3]) = max(6, 0+6) = 6** -> 카드팩3 1개
    # 그거와 별개로 3개짜리 구매하는 경우

    # 카드 4개 구매할때 최대 비용 dp[4]
    # i = 4 / j = 1,2,3,4
    # dp[4] = max(dp[4], dp[3]+arr[1]) = max(0, 6+1) = 7 -> 3개 구매한거 + 1개 추가 구매
    # dp[4] = max(dp[4], dp[2]+arr[2]) = max(7, 5+5) = 10 -> 2개 구매한거 + 2개 추가 구매
    # dp[4] = max(dp[4], dp[1]+arr[3]) = max(10, 1+6) = 10 -> 1개 구매한거 + 3개 추가 구매
    # dp[4] = max(dp[4], dp[0]+arr[4]) = max(10, 0+7) = 10 -> 전꺼 사용 x, 4개 추가 구매
    

    # 새거 하나 구매하는 것이 전에 구매했던 것들이 부족한거 몇개 더해서 구매하는 것보다 무조건 높다고 할 수 없어 -> 그러니까 둘을 비교하는 것. 
    # 만일 두개만 비교할라했으면(바로 전꺼에 하나 더하는게 나은지, 지금 이거 사용하는게 나은지) max(dp[3], dp[0]+arr[4]) 했으면 됐을듯?
    # 근데 여기서 몇개 더해서 구매하는 것 자체도 4=3+1, 4=2+2 이런식으로 더 많은 경우가 생길테니까 각각의 상황을 모두 고려해줌.. 이유는 어떤게 낫다고 확신하지 못함. 그때그때 봐야해. 