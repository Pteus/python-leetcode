from typing import List


n = 3


def generateParenthesis(n: int) -> List[str]:
    # add open parenthesis if open < n
    # add closing parenthesis if closed < open
    # valid when closed == open == n

    stack = []
    res = []

    """
       backtrack basics:
       if(GOAL REACHED)
            Add solution to res
            return
        
        if (constraint)
            make_choice
            backtrack(...)
            undo choice 
    """

    def backtrack(open_count, closed_count):
        if open_count == closed_count == n:
            res.append("".join(stack))
            return

        if open_count < n:
            stack.append("(")
            backtrack(open_count + 1, closed_count)
            stack.pop()

        if closed_count < open_count:
            stack.append(")")
            backtrack(open_count, closed_count + 1)
            stack.pop()

    backtrack(0, 0)
    return res


print(generateParenthesis(n))
