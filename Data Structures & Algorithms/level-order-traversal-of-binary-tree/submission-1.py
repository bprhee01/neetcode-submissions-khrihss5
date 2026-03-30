# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        q = deque()
        q.appendleft([root,0])
        while q:
            curr, lvl = q.popleft()
            if not curr:
                break
            if curr.right:
                q.appendleft([curr.right, lvl +1])
            if curr.left:
                q.appendleft([curr.left, lvl + 1])
            if lvl>= len(levels):
                levels.append([curr.val])
            else:
                levels[lvl].append(curr.val)
            print(curr.val,lvl)
        return levels

        