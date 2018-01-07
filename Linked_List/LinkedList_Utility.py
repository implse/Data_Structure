# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

# Create a linked list from Array
def LinkedList_From_List(a):
    head = ListNode(a[0])
    current = head
    for item in a[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

# Create a list from LinkedList
def List_from_LinkedList(l):
    out = []
    current = l
    while current != None:
        out.append(current.value)
        current = current.next
    return out

# Reverse a Linked List : Iterative Method
def Reverse_LinkedList(l):
    current = l
    next_node = None
    previous_node = None
    while current != None:
        next_node = current.next
        current.next = previous_node
        previous_node = current
        current = next_node
    return previous_node

# Reverse a linked List : Recursive Method
def RecursiveReverse_LinkedList(l, prev = None):
    current = l
    if not current:
        return prev
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
    return RecursiveReverse_LinkedList(current, prev)
