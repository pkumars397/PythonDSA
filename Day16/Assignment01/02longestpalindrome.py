def longestCommonSubsequence( text1, text2):
    
        n = len(text1)
        m = len(text2)
        dpGrid = [[0] * (m + 1) for _ in range(n + 1)]

        for row in range(n - 1, -1, -1):
            for col in range(m - 1, -1, -1):
                if text1[row] == text2[col]:
                    dpGrid[row][col] = 1 + dpGrid[row + 1][col + 1]
                else:
                    dpGrid[row][col] = max(dpGrid[row + 1][col], dpGrid[row][col + 1])

        return dpGrid[0][0]

text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1,text2))