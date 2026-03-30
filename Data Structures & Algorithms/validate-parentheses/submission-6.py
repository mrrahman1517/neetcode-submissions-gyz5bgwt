class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            if ch == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                stack.pop()
            if ch == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                stack.pop()
            if ch == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                stack.pop()
        return len(stack) == 0