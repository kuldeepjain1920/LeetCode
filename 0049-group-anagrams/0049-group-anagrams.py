class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        ## n = number of words in the input list
        ## k = average length of each word
        ## Time O(n.klogk) Space O(n.k)
        ## Runtime 13 ms Beats 50.35%
        ## Memory 22.3 MB Beats 44.55%

        groups = defaultdict(list) ## sorted-string key -> list of original values
        for word in strs:
            key= "".join(sorted(word)) ## canonical form
            groups[key].append(word)
        
        return list(groups.values())
        """

        ## This is the best case provided strs consists of lowercase English letters
        ## n = number of words in the input list
        ## k = average length of each word
        ## Time O(n.k) Space O(n.k)
        ## Runtime 11ms Beats 83.31%
        ## Memory 24.17 MB Beats 9.35%

        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1
            
            key = tuple(count)
            groups[key].append(word)

        return list(groups.values())

        """
        ## n = number of words in the input list
        ## k = average length of each word
        ## Time O(n.klogk) Space O(n.k)
        ## Runtime 7 ms Beats 98.39%
        ## Memory 22.09 MB Beats 65.71% 

        groups = {} ## sorted-string key -> list of original words
        for word in strs:
            key = "".join(sorted(word)) ##canonical form
            groups.setdefault(key, []).append(word)

        return list(groups.values())
        """

        """
        ## This is my version
        ## Runtime 11ms Beats 83.39%
        ## Memory 22.0 MB Beats 79.52%
        map_anagram = {}
        if len(strs) == 0: return []

        for str in strs:
            str_sort = "".join(sorted(str))
            if str_sort not in map_anagram:
                map_anagram[str_sort] = []
            map_anagram[str_sort].append(str)
        
        return list(map_anagram.values())
        """

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (["eat","tea","tan","ate","nat","bat"],[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
        ([""],[[""]]),
        (["a"],[["a"]]),
        ([],[]),
        (["", "", ""],[["", "", ""]]),
        (["abc", "def", "ghi"],[["abc"], ["def"], ["ghi"]]),
        (["abc", "abc"],[["abc", "abc"]]),
        (["abc","ab","bca","cb","cab","ac"],[['abc', 'bca', 'cab'], ['ab'], ['cb'], ['ac']])
    ]

    for anagram_list, expected in test_cases:
        output = sol.groupAnagrams(anagram_list)
        status = "✅ PASS" if output == expected else "❌ FAIL"
        print(f"{status} | strs={anagram_list} => {output}")
        