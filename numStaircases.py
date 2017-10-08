"""
Given a number of bricks N, returns the number of staircases that can
be built with exactly N bricks. Staircases must be at least length 2, and
each step must be decreasing in height.
"""
def answer(n):
    dp = [[0 for rows in range(n)] for columns in range(n+1)]
    # 1 and 2 cannot be split into smaller subproblems, base case.
    for currNum in range(3):
        for smallestVal in range(currNum, n):
            dp[currNum][smallestVal] = 1
    for currNum in range(3, n+1):
        for smallestVal in range(2, n):
            # Bubble up previous subproblems.
            dp[currNum][smallestVal] = dp[currNum][smallestVal-1]
            # If your smallest value is less than your current number,
            # add the difference's number of ways. Decrement smallestVal by 1
            # because you cannot reuse smallestVal in the decreasing staircase.
            if smallestVal <= currNum:
                dp[currNum][smallestVal] += dp[currNum-smallestVal][smallestVal-1]
    return dp[n][n-1]
