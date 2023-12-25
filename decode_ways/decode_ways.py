#Leetcode 91. Decode Ways
#A message containing letters from A-Z is being encoded to numbers using the following mapping:
#'A' -> 1, 'B' -> 2, ... 'Z' -> 26
#Given a string of digits, determine the number of ways to decode it.

#Dynamic programming solution
#Time complexity: O(n)
#Space complexity: O(n)
def numDecodings(s: str) -> int:
    if len(s) == 0:
        return 0
    #dp[i] is the number of ways to decode s[:i]
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    #base cases
    if s[0] == '0':
        dp[1] = 0
    else:
        dp[1] = 1
    #recursive case
    for i in range(2, len(s) + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        if s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]
    return dp[len(s)]

def main():
    s = "101"
    print(f"numDecodings({s}) = {numDecodings(s)}")

if __name__ == "__main__":
    main()
