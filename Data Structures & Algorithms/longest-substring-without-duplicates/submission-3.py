class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        seen = set()
        for r in range(len(s)):
            curr = s[r]
            # if the curr element already in substring, move l to make window smaller until that elem not in window anymore
            while curr in seen:
                seen.remove(s[l])
                l += 1
            # add current
            seen.add(curr)
            longest = max(longest, r - l + 1)
        return longest
        

        