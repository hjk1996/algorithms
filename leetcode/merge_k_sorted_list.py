# tag: linked-list, sort
# description
'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case
        if not lists:
            return None

        # while there are more than 1 list in lists
        while len(lists) > 1:
            temp = []
            # merge 2 lists at a time
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                temp.append(self.mergeLists(l1, l2))

            # update lists
            lists = temp

        # return the only list in lists
        return lists[0]
    

    def mergeLists(self, list1, list2):
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = ListNode(val=list1.val)
                list1 = list1.next
            else:
                cur.next = ListNode(val=list2.val)
                list2 = list2.next

            cur = cur.next
        
        if list1:
            cur.next = list1
        
        if list2:
            cur.next = list2

        return dummy.next
            