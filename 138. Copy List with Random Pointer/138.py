# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # create copyed list without random
        if head == None:
            return None

        i = head
        j = head.next
        while j:
            node = RandomListNode(i.label)
            i.next = node
            node.next = j
            i = j
            j = j.next

        node = RandomListNode(i.label)
        i.next = node

        # link random
        i = head
        while i:
            if i.random:
                i.next.random = i.random.next
            i = i.next.next

        # restore list
        new_head = head.next
        i = head
        j = head.next
        while j.next:
            i.next = j.next
            j.next = j.next.next
            i = i.next
            j = i.next
        i.next = None

        return new_head

