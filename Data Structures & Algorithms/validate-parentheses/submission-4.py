class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False

        for c in s:
            # c == open bracket:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                # c == close bracket:
                if not stack:
                    return False
                last = stack.pop()
                if c == ')' and last != '(':
                    return False
                elif c == ']' and last != '[':
                    return False
                elif c == '}' and last != '{':
                    return False
        
        if stack:
            return False
        return True

    