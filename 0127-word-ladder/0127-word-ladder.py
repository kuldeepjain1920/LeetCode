class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList) # O(1) lookup 
        if endWord not in word_set: return 0
        if beginWord == endWord: return 1 # clarify this in interview

        queue = deque([(beginWord,1)]) # word, steps so far
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()
            if word == endWord: return steps

            for i in range(len(word)): # try each position
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + c + word[i+1:]
                    if next_word == endWord: return steps + 1
                    if next_word in word_set and next_word not in visited:
                        # Mark it VISITED at enqueue time, not at dequeue time.
                        visited.add(next_word) # Avoid infinite loop
                        queue.append((next_word, steps + 1))

        return 0
                   
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
        ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
        ("hit", "cog", ["hot","dog","dog"], 0),
        ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
        ("hit", "hit", ["hit","hot","dot","dog","hit","lot","log"], 1),
        ("hit", "cog", ["hot","dot","hit","dog","lot","log","cog"], 5), #begin word already in wordList
    ]

    for beginWord, endWord, wordList, expected in test_cases:
        output = sol.ladderLength(beginWord, endWord, wordList)
        status = "✅ PASS" if output == expected else "❌ FAIL"
        print(f"{status} | beginword={beginWord} endWord={endWord} wordList={wordList} => {output}")
                
            
        