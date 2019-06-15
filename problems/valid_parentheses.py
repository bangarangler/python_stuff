'''
takes a string of parentheses, and determines if the order of the parentheses
is valid. should return true if the string is valid, and false if it's invalid
'''

def valid_parentheses(parens):
    count = 0
    i = 0
    while i < len(parens):
        if (parens[i] == '('):
            count += 1
        if (parens[i] == ')'):
            count -= 1
        if (count < 0):
            return False
        i += 1
    return count == 0
print(valid_parentheses('()')

# print(valid_parentheses('())(()))')

