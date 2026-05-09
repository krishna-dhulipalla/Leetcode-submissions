class Solution:
    def isValid(self, s: str) -> bool:
        pare = {'(': ')', '{': '}', '[': ']'}

        stack = []

        for i in s:
            if i in pare:
                stack.append(i)
            elif not stack or i != pare[stack[-1]]:
                return False
            else:
                stack.pop()
            
        return not stack