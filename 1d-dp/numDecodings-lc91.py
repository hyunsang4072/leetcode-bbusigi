def numDecodings(self, s: str) -> int:
    # TC: O(n)
    # SC: O(n)
    dp = {len(s) : 1}

    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == "0": # e.g., "06" is not valid mapping
            return 0
        
        res = dfs(i + 1)
        
        # if "_ _" is in 10~26
        if i + 1 < len(s) and int(s[i] + s[i + 1]) in range(10,  27):
            res += dfs(i + 2)

        # cache
        dp[i] = res

        return res
    
    return dfs(0)