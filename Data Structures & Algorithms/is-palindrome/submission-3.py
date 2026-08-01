class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while (start <= end):
            while (start < len(s) - 1 and not s[start].isalnum()):
                start += 1
            while (start < len(s) - 1 and not s[end].isalnum()):
                end -= 1
            #print(f"comparing : |{s[start].lower()}|vs|{s[end].lower()}|")
            if start <= end and s[start].lower() != s[end].lower():
                #print(f"im the culprit : |{s[start].lower()}|vs|{s[end].lower()}|")
                return False
            start += 1
            end -= 1
        return True