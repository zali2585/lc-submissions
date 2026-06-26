class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        l = 0
        r = 0             
        need = Counter(t)
        windowFreq = Counter()
        have = 0
        needCount = len(need)

        res = [-1, -1]
        # intializes length of string to infinity, so if any substring is found, itll be store
        res_len = float("inf")
        
        for r in range(len(s)):
            c = s[r]
            windowFreq[c] += 1
            if c in need and windowFreq[c] == need[c]:
                have += 1
            # window is valid, just needs to be shrunk now
            # needCount is number of unique chars in t, have = number of chars that have correct freq
            while have == needCount:
                # valid string found, now saving indices (if shorter than current saved string)
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                # remove additional letters from left from window
                leftC = s[l]
                windowFreq[leftC] -= 1

                if leftC in need and windowFreq[leftC] < need[leftC]:
                    have -= 1
                l +=1
        left, right = res
        if res_len == float("inf"):
            return ""
        return s[left:right + 1]



