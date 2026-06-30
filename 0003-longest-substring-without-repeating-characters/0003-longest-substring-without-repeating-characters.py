class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ## Time O(n) and Space  O(min(n,charset)
        ## Runtime 8 ms Beats 87.88%
        ## Memory 19.48MB beats 29.91%
        ## hashmap implementation
        if len(s) == 0: return 0

        left = 0
        max_length = 0
        last_seen = {}
        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1 ## duplicate found INSIDE current window - shrink

            last_seen[ch] = right
            max_length = max(max_length, right - left + 1)

        return max_length

        """
        ## Set implementation
        ## Time is O(n) amortized, Space is O(min(n,charset))
        ## Runtime 15ms Beats 42.72%
        ## Memory 19.37 MB Beats 7.45%
        left = 0
        char_set = set()
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len
        """
              

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("dvdf", 3),
        ("abcdef",6),
        ("a",1),
        ("aAaA", 2)
    ]

    for s, expected in test_cases:
        output = sol.lengthOfLongestSubstring(s)
        status = "✅ PASS" if output == expected else "❌ FAIL"
        print(f"{status} | s={s} => {output}")