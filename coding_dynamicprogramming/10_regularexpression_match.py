'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

 
示例 1：

输入：s = "aa" p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2:

输入：s = "aa" p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3：

输入：s = "ab" p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4：

输入：s = "aab" p = "c*a*b"
输出：true
解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5：

输入：s = "mississippi" p = "mis*is*p*."
输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp[i][j] 表示s的前i个字符和p的前j个字符 是否匹配
        #  如果 s[i] == p[j] dp[i][j] = dp[i-1][j-1]
        # p[j] == '.'  dp[i][j] = dp[i-1][j-1]
        # p[j] == '*'
            # 1) p[j-1] != s[i] dp[i][j] = dp[i][j-2]
            # 2) p[j-1] == s[i] :
                    # aa a*  dp[i][j] = d[i-1][j]
                    # ba a* dp[i][j] = dp[i][j-1]
                    # b a*  dp[i][j] = dp[i][j-2]
        m = len(s)
        n = len(p)

        dp = [[False for _ in range(n+1)]for _ in range(m+1)]
        dp[0][0] = True 

        for j in range(2,n+1):
            if p[j-1] =='*':
                dp[0][j] = dp[0][j-2]
        for  i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1]=='*':
                    dp[i][j] = p[j]

