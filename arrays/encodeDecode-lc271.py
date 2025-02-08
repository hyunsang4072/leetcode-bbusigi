def encode(self, strs: list[str]) -> str:
    # e.g., strs = ["neet","code","love","you"]
    # encode(strs) --> "4#neet4#code4#love3#you"
    # TC: O(n)
    res = ''

    for s in strs:
        res = res + str(len(s)) + '#' + s

    return res

def decode(self, s: str) -> list[str]:
    # e.g., s = "4#neet4#code4#love3#you"
    # decode(s) --> ["neet","code","love","you"]
    # TC: O(n), where n = length(all strings combined)
    res = []

    i = 0

    while i < len(s): # "4#  neet  4#  code  4#  love  3#  you"
        j = i

        while s[j] != '#': # i...j# --> find len(i...j)
            j += 1

        length = int(s[i:j]) # length = 4 in "4#neet"
        
        word = s[j+1:j+1+length]
        res.append(word)

        i = j + 1 + length # + 1 so that we start right after the previous word

    return res      
