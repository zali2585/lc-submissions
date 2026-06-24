class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        length = 0
        seen = set()
        for r in range(len(s)):
            curr = s[r]
            if curr not in seen:
                seen.add(curr)
                length += 1
                if length > longest:
                    longest = length
            else:
                while s[l] != curr:
                    seen.discard(s[l])
                    l += 1
                    print("changing length")
                    length -= 1
                seen.discard(s[l])
                l += 1
                seen.add(curr)
        return longest 
        

        