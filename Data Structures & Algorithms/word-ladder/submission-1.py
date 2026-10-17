from collections import deque
from typing import List

class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:

        # Convert wordList into a set for O(1) lookup
        wordSet = set(wordList)

        # If endWord is not available, transformation is impossible
        if endWord not in wordSet:
            return 0

        # Queue stores (word, transformation sequence length)
        q = deque([(beginWord, 1)])

        # Remove starting word if present to avoid revisiting
        wordSet.discard(beginWord)

        while q:
            word, length = q.popleft()

            # Reached our destination
            if word == endWord:
                return length

            # Try changing each character position
            for i in range(len(word)):

                # Try all 26 lowercase letters
                for ch in "abcdefghijklmnopqrstuvwxyz":

                    # Generate new word by replacing character at i
                    newWord = word[:i] + ch + word[i + 1:]

                    # Only process words that exist in wordSet
                    if newWord in wordSet:

                        # Mark visited immediately to avoid duplicates
                        wordSet.remove(newWord)

                        # Add new word with incremented sequence length
                        q.append((newWord, length + 1))

        # No valid transformation sequence found
        return 0