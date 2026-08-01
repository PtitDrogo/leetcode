class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1, -1]

        countS = {}
        countT = {}
        resLen = float("infinity")

        need, have = 0, 0
        l = 0

        for c in t:
            countT[c] = 1 + countT.get(c, 0) 
        need = len(countT) #Im assuming this return the len of the number of keys
        print(need)
        for r in range(len(s)):
            c = s[r]
            print(c)
            if c in t:
                countS[c] = 1 + countS.get(c, 0)
                if countS[c] == countT[c]:
                    have += 1
            # print(f"need = {need}, have = {have}")
            # print(f"r = {r}, l = {l}")
            print(f"curr substring {s[l:r + 1]}")
            if need == have and (r - l + 1) < resLen: #?
                res = [l, r]
                resLen = len(s[l: r + 1])
                print(f"setting res to {res}")
            while need == have:
                print("Hello, in l moving")
                print(f"(r - l + 1) < resLen : {r} - {l} + 1 < {resLen}")
                if (r - l + 1) < resLen: #?
                    print("Changing res in l moving, curr substring = {s[l:r + 1]}")
                    res = [l, r]
                    resLen = len(s[l: r + 1])
                c = s[l]
                countS[c] = max(countS.get(c, 0) - 1, 0)
                if c in t and countS[c] < countT[c]:
                    have -= 1
                l += 1
        if res == [-1, -1]:
            return ""
        print(f"{s[res[0]: res[1] + 1]}")
        return s[res[0]: res[1] + 1]

            
            
            


