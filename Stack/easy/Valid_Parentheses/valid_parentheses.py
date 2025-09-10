class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            match c:
                case ']':
                    if (stack != [] and stack[-1]=='['):
                        stack.pop()
                    else:
                        return False
                case '}':
                    if (stack != [] and stack[-1]=='{'):
                        stack.pop()
                    else:
                        return False
                case ')':
                    if (stack != [] and stack[-1]=='('):
                        stack.pop()
                    else:
                        return False
                case _:
                    stack.append(c)
        return (len(stack)==0)