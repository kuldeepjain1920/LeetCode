class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        stack = []
        match = {"]":"[", "}":"{", ")":"("}

        for ch in s:
            if ch in match:
                if not stack or stack[-1] != match[ch]:
                    return False # mismatch or empty stack
                stack.pop()
            else:
                stack.append(ch) #opening bracket -> push

        return not stack

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("()", True), ## matching brackets
        ("()[]{}", True), ## matching brackets, no nesting
        ("(])", False), ## Odd Length
        ("([{}])", True), ## nested matching brackets
        ("([)]", False), ## wrong order
        ("", True), ## Empty String
        ("{", False), ## Single bracket Odd Length
        ("(((", False), ## Odd Length
        ("]})}"), ## Only closing brackets
        ("[{([[[{{{((()))}}}]]])}]", True) ## Deeply nested  
    ]
        