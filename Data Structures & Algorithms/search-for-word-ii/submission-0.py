from typing import List


class TrieNode:
    def __init__(self):
        # children maps:
        # character -> next TrieNode
        #
        # Example:
        # {
        #     'a': TrieNode(),
        #     'b': TrieNode()
        # }
        self.children = {}

        # True if a complete word ends at this node
        self.isWord = False


    def addWord(self, word):
        # Start from this TrieNode
        cur = self

        # Add every character of the word into the Trie
        for c in word:

            # If this character path does not exist,
            # create a new TrieNode
            if c not in cur.children:
                cur.children[c] = TrieNode()

            # Move to the next TrieNode
            cur = cur.children[c]

        # Mark the last node as the end of a complete word
        cur.isWord = True


class Solution:
    def findWords(
        self,
        board: List[List[str]],
        words: List[str]
    ) -> List[str]:

        # ---------------------------------------------------
        # STEP 1: Build Trie using all words
        # ---------------------------------------------------

        root = TrieNode()

        for word in words:
            root.addWord(word)


        # Number of rows and columns in the board
        ROWS = len(board)
        COLS = len(board[0])


        # res stores words we successfully find
        #
        # Using a set prevents duplicate words
        res = set()


        # visit stores cells currently being used
        # in the current DFS path.
        #
        # We cannot use the same board cell twice
        # while building one word.
        visit = set()


        # ---------------------------------------------------
        # DFS
        #
        # r, c  = current board position
        # node  = current TrieNode
        # word  = word built so far
        # ---------------------------------------------------

        def dfs(r, c, node, word):

            # Stop DFS if:
            #
            # 1. row is outside board
            # 2. column is outside board
            # 3. this cell is already used
            # 4. current board character is NOT
            #    a valid next character in the Trie
            if (
                r < 0 or
                c < 0 or
                r >= ROWS or
                c >= COLS or
                (r, c) in visit or
                board[r][c] not in node.children
            ):
                return


            # ------------------------------------------------
            # Current cell is valid
            # ------------------------------------------------

            # Mark this board position as being used
            visit.add((r, c))


            # Move down the Trie using the board character
            #
            # Example:
            #
            # node.children = {
            #     'a': TrieNode(),
            #     'b': TrieNode()
            # }
            #
            # board[r][c] = 'a'
            #
            # We move to the TrieNode for 'a'
            node = node.children[board[r][c]]


            # Add current board character to our word
            word += board[r][c]


            # If the current TrieNode marks the end
            # of a complete word, we found a word
            if node.isWord:
                res.add(word)


            # ------------------------------------------------
            # Explore all 4 directions
            # ------------------------------------------------

            # Down
            dfs(r + 1, c, node, word)

            # Up
            dfs(r - 1, c, node, word)

            # Right
            dfs(r, c + 1, node, word)

            # Left
            dfs(r, c - 1, node, word)


            # ------------------------------------------------
            # BACKTRACK
            # ------------------------------------------------
            #
            # We are done exploring paths that use this cell.
            # Remove it so another DFS path can use it.
            visit.remove((r, c))


        # ---------------------------------------------------
        # STEP 2: Try starting DFS from every board cell
        # ---------------------------------------------------

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")


        # Convert set to list
        return list(res)