class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]": "[", "}": "{"}

        for char in s: #checks each c in s
            if char in closeToOpen: #if c is a closing parentheses
                #if stack not empty/ c-1 = matching opening parenthesis to current c
                if stack and stack[-1] == closeToOpen[char]:  
                    #remove open parenthesis from stack
                    stack.pop()
                #means opening parenthesis not directly in front of closing, meaning not matching
                else: 
                    return False
            #since not key in dict (ie: not closing paren), adds to stack
            else: 
                stack.append(char)
        #means all els in s had matching paren
        return True if not stack else False


