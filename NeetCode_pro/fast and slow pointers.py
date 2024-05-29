# Q: Find the middle of a linked list
# T:O(n)
# S:O(1)
def middle_of_list(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# Q:Determine if a linked list has a cycle
# T:O(n)
# S:O(1)
def has_cycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


# Q:Determine if a linked list has a cycle and return the head of the cycle, None otherwise
# T:O(n)
# S:O(1)
def cycle_start(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    slow2 = head
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next

    return slow
