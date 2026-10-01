class TrieNode:
    def __init__(self):
        # Maps character -> next TrieNode
        #
        # Example:
        # children = {
        #     'a': TrieNode(),
        #     'b': TrieNode()
        # }
        self.children = {}

        # True means a complete word ends at this node
        self.word = False


class WordDictionary:
    def __init__(self):
        # Root represents the starting point of the Trie
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        # Start from root
        cur = self.root

        # Go through every character in the word
        for c in word:

            # If this character path does not exist,
            # create a new TrieNode
            if c not in cur.children:
                cur.children[c] = TrieNode()

            # Move to the next node
            cur = cur.children[c]

        # After processing all characters,
        # mark this node as the end of a valid word
        cur.word = True


    def search(self, word: str) -> bool:

        # dfs(j, root)
        #
        # j    = index in the search word
        # root = TrieNode where we should start searching
        #
        # We need DFS because "." can represent ANY character.
        def dfs(j, root):

            # Start from the given TrieNode
            cur = root

            # Continue searching from index j
            for i in range(j, len(word)):

                c = word[i]

                # "." can match any ONE character
                if c == ".":

                    # Try every possible child
                    #
                    # Example:
                    #
                    #        root
                    #       / | \
                    #      a  b  c
                    #
                    # If search character is ".",
                    # we need to try a, b, and c.
                    for child in cur.children.values():

                        # Continue searching the rest of the word
                        # from this child node.
                        #
                        # i + 1 because "." already matched
                        # the current character.
                        if dfs(i + 1, child):
                            return True

                    # None of the possible children worked
                    return False

                else:
                    # Normal character:
                    # It must exist in the current node's children
                    if c not in cur.children:
                        return False

                    # Move to the matching child node
                    cur = cur.children[c]

            # We processed every character in the search word.
            #
            # Return True ONLY if a complete word ends here.
            #
            # Example:
            # Trie contains "bad"
            #
            # search("ba") should return False
            # because "ba" is only a prefix, not a complete word.
            return cur.word

        # Start DFS from index 0 and the Trie root
        return dfs(0, self.root)