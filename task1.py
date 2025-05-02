class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def print_list(self):
        print(" -> ".join(map(str, self.to_list())))

    def reverse(self):
        """
        Реверсує список, змінюючи посилання між вузлами
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        """
        Сортує однозв'язний список сортуванням вставками
        """
        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            if not sorted_head or current.value < sorted_head.value:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and temp.next.value < current.value:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node

        self.head = sorted_head

def merge_sorted_lists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    """
    Об'єднує два відсортовані списки в один
    """
    dummy = Node(0)
    tail = dummy
    a, b = l1.head, l2.head

    while a and b:
        if a.value < b.value:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    tail.next = a or b

    merged = LinkedList()
    merged.head = dummy.next
    return merged

if __name__ == "__main__":
    print("=== Тест реверсу ===")
    ll = LinkedList()
    for val in [1, 2, 3, 4]:
        ll.append(val)
    ll.print_list()
    ll.reverse()
    ll.print_list()

    print("\n=== Тест сортування ===")
    ll2 = LinkedList()
    for val in [4, 2, 5, 1, 3]:
        ll2.append(val)
    ll2.insertion_sort()
    ll2.print_list()

    print("\n=== Тест злиття списків ===")
    a = LinkedList()
    b = LinkedList()
    for v in [1, 3, 5]:
        a.append(v)
    for v in [2, 4, 6]:
        b.append(v)
    merged = merge_sorted_lists(a, b)
    merged.print_list()