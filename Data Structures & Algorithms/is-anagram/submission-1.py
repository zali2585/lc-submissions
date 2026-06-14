class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #make freq hasmap for s & t
        #if not same length, ret false
        hashS = {}
        hashT = {}
        for char in s:
            hashS[char] = hashS.get(char, 0) + 1
        for char in t:
            hashT[char] = hashT.get(char, 0) + 1
        if len(s) != len(t):
            return False
        for key in hashS:
            if hashS[key] != hashT.get(key, 0):
                return False
        return True
        #if value for every char in s = 0 in t bc of .get, ret false

        