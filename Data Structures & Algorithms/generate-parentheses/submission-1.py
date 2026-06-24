class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backTrack(openB, closeB, current):
            if openB == closeB == n:
                res.append("".join(current))
                return 

            if openB < n:
                current.append('(')
                backTrack(openB + 1, closeB, current)
                current.pop()

            if closeB < openB:
                current.append(')')
                backTrack(openB, closeB + 1, current)
                current.pop()
        backTrack(0, 0, [])
        return res