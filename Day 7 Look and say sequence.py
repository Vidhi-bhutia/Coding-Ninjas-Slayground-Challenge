def lookAndSay(s):
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += str(count) + s[i - 1]
            count = 1

    result += str(count) + s[-1]  # Handling the last set of digits
    return result

def lookAndSequence(n):
    term = "1"

    for _ in range(n - 1):
        term = lookAndSay(term)

    return term

def takeInput():
    n = int(input().strip())
    return n

t = int(input().strip())
for i in range(t):
    n = takeInput()
    print(lookAndSequence(n))
