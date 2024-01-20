class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if coins == None or amount == 0:
            return 0
        
        dp = [[0]*(amount+1) for i in range(len(coins)+1)]
        for i in range(amount+1):
            dp[0][i] = amount+1
        
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]

                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]]+1)
        if dp[-1][-1] == amount+1:
            return -1
        return dp[-1][-1]
