class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign_stack = []
        ops = '+-'
        last_sign = '+'
        curr_num = 0
        for ch in s:
            if ch ==' ':
                continue
            if ch == '(':
                stack.append(ch)
                sign_stack.append(last_sign)
                last_sign = '+'
            if ch.isdigit():
                curr_num =  curr_num * 10 + int(ch)
            if ch in ops:
                if last_sign == '-':
                    curr_num *= -1
                last_sign = ch
                if curr_num != 0:
                  stack.append(curr_num)
                curr_num = 0
            if ch == ')':
                #process the current closing parenthesis
                if last_sign == '-':
                    curr_num *= -1
                stack.append(curr_num)
                curr_num = 0
                last_sign = '+'
                temp_res = 0
                while stack[-1] != '(':
                    temp_res += stack[-1]
                    stack.pop()
                stack.pop() #remove the parenthesis
                sign = sign_stack[-1]
                sign_stack.pop()
                if sign == '-':
                    temp_res *= -1
                stack.append(temp_res)

        #see if last curr_num is processed
        if curr_num  != 0:
          if last_sign == '-':
              curr_num *= -1
          stack.append(curr_num)

        res = 0
        while stack:
            res += stack[-1]
            stack.pop()
        return res