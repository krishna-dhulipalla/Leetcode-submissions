class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def gen_para(path, openP, closeP):

            if openP == closeP == n:
                res.append(path)
                return
            
            if openP < n:
                gen_para(path + "(", openP + 1, closeP)
            
            if closeP < openP:
                gen_para(path + ")", openP, closeP + 1) 
            
        gen_para('', 0, 0)
    
        return res