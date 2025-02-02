import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        dummy = ListNode()
        curr = dummy

        min_heap = []

        for i in range(len(lists)):
            if not lists[i]:
                continue
            heapq.heappush(min_heap, (lists[i].val, i))

        while min_heap:
            _, i = heapq.heappop(min_heap)
            curr.next = lists[i]

            curr = curr.next
            
            lists[i] = lists[i].next

            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))

        return dummy.next


def print_ll(ll: ListNode | None) -> None:
    while ll:
        print(ll.val)
        ll = ll.next

a = ListNode(1)
b = ListNode(4)
c = ListNode(5)
a.next = b
b.next = c

d = ListNode(1)
e = ListNode(3)
g = ListNode(4)
d.next = e
e.next = g

h = ListNode(2)
i = ListNode(6)
h.next = i

sol = Solution()
print_ll(sol.mergeKLists(lists=[a, d, h]))
