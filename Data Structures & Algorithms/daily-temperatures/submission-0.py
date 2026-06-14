class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #stores indices and temperatures
        result = [0] * len(temperatures)
        # for n popped from stack (pop occurs if curr > curr - 1) increment count
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #while list holds a temp and current temp > held temp
                stackT, stackInd = stack.pop()
                result[stackInd] = (i - stackInd)
            stack.append([t, i])
        return result
#pattern: next greater element, first element to right big/smal
                


