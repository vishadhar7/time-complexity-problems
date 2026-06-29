s = "anagram"
t = "nagaram"

if len(s) != len(t):
    print(False)
else:
    count = [0] * 26

    for ch in s:
        count[ord(ch) - ord('a')] += 1

    for ch in t:
        count[ord(ch) - ord('a')] -= 1

    if count == [0] * 26:
        print(True)
    else:
        print(False)
