class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

list1 = [1,2,4]
list2 = [1,3,4]

list3 = list1 + list2

print(sorted(list3))