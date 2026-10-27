from collections import deque

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            # Handle null node
            if not node:
                res.append("N")
                return

            # Store node value
            res.append(str(node.val))

            # Serialize left subtree
            dfs(node.left)

            # Serialize right subtree
            dfs(node.right)

        dfs(root)

        # Join values
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = deque(data.split(","))

        def dfs():
            # Get next value
            val = vals.popleft()

            # Handle null node
            if val == "N":
                return None

            # Create current node
            node = TreeNode(int(val))

            # Build left subtree
            node.left = dfs()

            # Build right subtree
            node.right = dfs()

            return node

        return dfs()