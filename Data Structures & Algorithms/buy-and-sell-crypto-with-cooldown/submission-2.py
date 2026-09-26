class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Number of days
        n = len(prices)

        # dp[i][0] -> max profit on day i when NOT holding stock
        # dp[i][1] -> max profit on day i when CAN buy stock
        dp = [[0] * 2 for _ in range(n + 1)]

        # Iterate days backwards
        for i in range(n - 1, -1, -1):

            # buying = True  -> can buy
            # buying = False -> holding stock
            for buying in [True, False]:

                if buying:
                    # Option 1: Buy stock today
                    buy = dp[i + 1][0] - prices[i] if i + 1 < n else -prices[i]

                    # Option 2: Do nothing (cooldown)
                    cooldown = dp[i + 1][1] if i + 1 < n else 0

                    # Choose best profit
                    dp[i][1] = max(buy, cooldown)

                else:
                    # Option 1: Sell stock today
                    # After selling, skip one day (cooldown)
                    sell = dp[i + 2][1] + prices[i] if i + 2 < n else prices[i]

                    # Option 2: Do nothing (hold stock)
                    cooldown = dp[i + 1][0] if i + 1 < n else 0

                    # Choose best profit
                    dp[i][0] = max(sell, cooldown)

        # Start at day 0 with ability to buy
        return dp[0][1]
