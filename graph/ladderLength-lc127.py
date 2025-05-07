def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    neighbor = defaultdict(list)
    wordList.append(beginWord)

    for word in wordList:
        for i in range(len(word)):
            # e.g., {"*ot": ["hot", "dot", "lot"], ...}
            pattern = word[:i] + "*" + word[i+1:]
            neighbor[pattern].append(word)
    
    visited = set()
    visited.add(beginWord)
    q = deque()
    q.append(beginWord)
    res = 1

    while q:
        for i in range(len(q)): # layer by layer
            # ALWAYS pop first
            word = q.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                # e.g., {"*ot": ["hot", "dot", "lot"], ...}
                pattern = word[:j] + "*" + word[j+1:]
                for nei in neighbor[pattern]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    q.append(nei)
        res += 1
    
    return 0