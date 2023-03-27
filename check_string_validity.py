# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Input: s = "()"
# Output: true
# Input: s = "()[]{}"
# Output: true
# Input: s = "(]"
# Output: false


def check_string_validity(string):
    open_brackets = ["(", "[", "{"]
    close_brackets = [")", "]", "}"]
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}  # key: open bracket, value: close bracket
    stack = []

    validity = True
    for char in string:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if validity == False:
                return validity
            else:
                last_open_bracket = stack.pop()
                if bracket_pairs[last_open_bracket] != char:
                    validity = False
        else:
            return False
    
    return validity

if __name__ == "__main__":
    print(check_string_validity("([{]]]]}])"))