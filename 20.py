# 20 有效的括号

# 笨方法
def isValid1(s: str) -> bool:
    if s == "":
        return True
    s = list(s)
    change = True
    while len(s) > 1 and change == True:
        s_len = len(s)
        for i in range(0, s_len - 1):
            s1 = s[i]
            s2 = s[i + 1]
            if isRe(s1,s2):
                s.pop(i + 1)
                s.pop(i)
                change = True
                break
            else:
                change = False

    if len(s) == 0:
        return True
    return False

def isRe(s1: str, s2: str) -> bool:
    if (s1 == "(" and s2 == ")") or (s1 == "[" and s2 == "]") or (s1 == "{" and s2 == "}"):
        return True
    return False

# 栈方法
def isValid(s: str) -> bool:
    if s == "":
        return True
    if len(s) % 2 == 1:
        return False
    stack = []
    kv = {
        ")":"(",
        "]":"[",
        "}":"{",
    }
    for char in s:
        if char in kv:
            if len(stack) == 0:
                return False
            top = stack[-1]
            if top == kv[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    if len(stack) == 0:
        return True
    return False


if __name__ == "__main__":
    print(isValid("[(])"))