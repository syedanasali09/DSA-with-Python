def is_matched(expression):
    if not expression:
        return True

    opening_symbols = '([{'
    closing_symbols = ')]}'
    if expression[0] in opening_symbols:
        closing_symbol = closing_symbols[opening_symbols.index(expression[0])]
        count = 1
        index = 1

        while count != 0 and index < len(expression):
            if expression[index] == expression[0]:
                count += 1
            elif expression[index] == closing_symbol:
                count -= 1
            index += 1

        if count == 0:
            if is_matched(expression[1:index-1]) and is_matched(expression[index:]):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

expression1 = "(3 + [4 - {5 * 2}])"
expression2 = "((2 + 3)"
expression3 = "[2 - 5] * (4 + 7)"
print(is_matched(expression1)) 
print(is_matched(expression2))  
print(is_matched(expression3))  
