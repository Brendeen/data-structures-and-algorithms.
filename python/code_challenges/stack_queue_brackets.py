from data_structures.stack import Stack


def multi_bracket_validation(string):
    s = Stack()
    opening_bracks = ['(', '{', '[']
    closing_bracks = [')', '}', ']']

    for character in string:
        if character in string[0] == ')' or string[0] == '}' or string[0] == ']':
            return False
        if character in opening_bracks:
            s.push(character)
        elif character in closing_bracks:
            if not s:
                return False
            if closing_bracks.index(character) == opening_bracks.index(s.pop()):
                return True
            else:
                return False
