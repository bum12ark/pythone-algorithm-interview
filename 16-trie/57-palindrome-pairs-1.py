"""
* 팰린드롬 페어
단어 리스트에서 words[i] + words[j]가 팰린드롬이 되는 모든 인덱스 조합 (i, j)를 구하라
- Example 1
Input: ["abcd", "dcba", "lls", "s", "sssll"]
Output: [[0, 1], [1, 0], [3, 2], [2, 4]]
Explanation: ["dcbaabcd", "abcddcba", "slls", "llsssssll"]이 팰린드롬이다.
- Example 2
Input: ["bat", "tab", "cat"]
Output: [[0, 1], [1, 0]]
Explanation: ["battab", "tabbat"]이 팰린드롬이다.
"""
from typing import List


class Solution:
    # 브루트 포스 방식으로 풀이
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(word: str):
            return word == word[::-1]

        output = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                if isPalindrome(word1 + word2):
                    output.append([i, j])
        return output

if __name__ == '__main__':
    param1: List[str] = ["abcd", "dcba", "lls", "s", "sssll"]
    param2: List[str] = ["bat", "tab", "cat"]

    print(Solution().palindromePairs(param1))
    print(Solution().palindromePairs(param2))