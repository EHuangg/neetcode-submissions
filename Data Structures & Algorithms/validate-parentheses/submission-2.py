class Solution:
    def isValid(self, s: str) -> bool:
        # map each open bracket to its closed bracket
        bracketMap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        # use a stack for the open brackets
        openStack = []

        for c in s:
        # put each open bracket in s into stack
            if c not in bracketMap:
                openStack.append(c)
            # whenever a closed bracket appears, must close most recent open bracket
            else:
                if len(openStack) == 0:
                    return False
                top = openStack.pop()
                # otherwise its not valid
                if top != bracketMap[c]:
                    return False
            print(openStack)
        return len(openStack) == 0
        
    
