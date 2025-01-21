"""Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?"""


# My solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        answer = []
        index = 0

        for n_s in range(len(s)):
            if s[n_s] in t:
                for n_t in range(len(t)):
                    if s[n_s] == t[n_t] and index <= n_t:
                        index = n_t
                        answer.append(True)
                        break
            else:
                answer.append(False)
        return all(answer) if len(answer) == n_s else False


s = Solution()
s.isSubsequence("acb", "ahbgdc")


# algo.io solve
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_l = len(s)
        t_l = len(t)
        counter_s = 0
        if s == "":
            return True
        if s_l > t_l:
            return False
        for i in range(t_l):
            if t[i] == s[counter_s]:
                if counter_s == s_l - 1:
                    return True
                counter_s += 1

        return False

    # Time: O(T)
    # Time: O(1)
