class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"*","/","-","+"}
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                # print(stack)
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                else:
                    if (num1 < 0 or num2 < 0) and not (num1 < 0 and num2 < 0):
                        # print(True)
                        stack.append(abs(num1) // abs(num2) * -1)
                    else:
                       stack.append(num1 // num2) 
        return stack[0]
#tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# 