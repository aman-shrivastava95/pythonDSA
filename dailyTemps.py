class Solution:
    def dailyTemps(self, temps):
        n = len(temps)
        res = [0] * n
        stack = []
        
        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)

        return res

        
        

