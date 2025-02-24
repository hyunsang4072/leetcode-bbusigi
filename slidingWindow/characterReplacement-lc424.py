def characterReplacement(self, s: str, k: int) -> int:
    count = {} # we want to keep track of frequencies of each character
    # so that we can find the most frequent character
    l = 0
    res = 0 # maximum sliding window length

    # condition: len(window) - count(most_freq_char) <= k
    maxF = 0 # count(most_freq_char); this variable lets us avoid scanning through the hashMap
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        maxF = max(maxF, count[s[r]])

        # window size = r - l + 1
        # (r - l + 1) - maxF = # of characters needed to be replaced to get the longest repeating letters
        while (r - l + 1) - maxF > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    return res