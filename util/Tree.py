from typing import List 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return f'{self.val}'


class Tree:
    def make_tree(self, list_tree):
        if not list_tree: return None
        head = TreeNode(list_tree[0])
        cur_head_list = [head]

        for idx in range(1, len(list_tree), 2):
            cur_head = cur_head_list[0]
            if (idx < len(list_tree)) and (list_tree[idx]):
                cur_head.left = TreeNode(list_tree[idx])
                cur_head_list.append(cur_head.left)
            if (idx+1 < len(list_tree)) and (list_tree[idx+1]):
                cur_head.right = TreeNode(list_tree[idx+1])
                cur_head_list.append(cur_head.right)
            del cur_head_list[0]
        return head