from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        map_els = dict()
        for l in lists:
            while l is not None:
                map_els[l.val] = map_els.get(l.val, 0) + 1
                l = l.next
        map_els = dict(sorted(map_els.items()))
        if not map_els:
            return None
        head_res = ListNode()
        tmp = head_res
        for it, (k, v) in enumerate(map_els.items()):
            for i in range(v):
                tmp.val = k
                if it == len(map_els) - 1 and i == v - 1:
                    break
                tmp.next = ListNode()
                tmp = tmp.next
        return head_res


def FillList(arrs: List[List[int]]) -> List[ListNode]:
    lists = []
    for arr in arrs:
        list_node = ListNode()
        tmp_node = list_node
        for it, val in enumerate(arr):
            tmp_node.val = val
            if it < len(arr) - 1:
                tmp_node.next = ListNode()
                tmp_node = tmp_node.next
        lists.append(list_node)
    return lists


def PrintList(list_node: ListNode) -> None:
    tmp_node = list_node
    while tmp_node is not None:
        print(f'{tmp_node.val} -> ', end='')
        tmp_node = tmp_node.next
    print('None')


s = Solution()
# test1
lists = FillList([[1, 4, 5], [1, 3, 4], [2, 6]])
PrintList(s.mergeKLists(lists))
# test2
lists = FillList([[1, 2, 2], [1, 1, 2]])
PrintList(s.mergeKLists(lists))
