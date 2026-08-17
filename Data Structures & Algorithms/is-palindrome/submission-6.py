class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = []
        for w in s:
            if w.isalnum():
                s_clean.append(w.lower())
        
        return s_clean[:] == s_clean[::-1]