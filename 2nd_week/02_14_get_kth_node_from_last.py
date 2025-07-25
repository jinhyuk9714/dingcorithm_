class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        cur = self.head
        ll_len = 0
        while cur is not None:
            cur = cur.next
            ll_len += 1
        cur = self.head
        for _ in range(ll_len - k):
            cur = cur.next
        return cur

    def get_kth_node_from_last_new(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
print(linked_list.get_kth_node_from_last_new(2).data)  # 7이 나와야 합니다!
