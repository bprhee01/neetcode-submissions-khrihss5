class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def helper(open_count,close_count, curr):

            if open_count == n:
                while close_count < open_count:
                    curr += ")"
                    close_count += 1
                output.append(curr)
            elif open_count == close_count:
                helper(open_count + 1, close_count, curr + "(")
            else:
                helper(open_count + 1, close_count, curr + "(")
                helper(open_count, close_count + 1, curr + ")")          
            

        helper(0,0, "")
        return output