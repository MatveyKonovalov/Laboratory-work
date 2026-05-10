from lists.linked_list import *

def merge_lists(list1_head: Node, list2_head: Node) -> Node:
    head_result = Node(None)
    cur = head_result

    while list1_head or list2_head:
        if not list2_head:
            cur.next = list1_head
            break
        elif not list1_head:
            cur.next = list2_head
            break
        else:
            if list1_head.val < list2_head.val:
                cur.next = list1_head
                list1_head = list1_head.next
            else:
                cur.next = list2_head
                list2_head = list2_head.next
            cur = cur.next

    return head_result.next



def get_len_list(head: Node) -> int:
    len_list = 0

    while head:
        len_list += 1
        head = head.next
    
    return len_list



def merge_sort_linked_list(head: Node) -> Node:
    cur = head

    cur_len = get_len_list(head)
    each_len = cur_len // 2

    if cur_len == 1:
        return head
    
    first = Node(None)
    cur_first = first
    for node_ind in range(each_len):
        cur_first.next = cur
        cur = cur.next
        cur_first = cur_first.next
    cur_first.next = None
    first = first.next

    second = cur
    return merge_lists(merge_sort_linked_list(first), merge_sort_linked_list(second))

def print_result(head: Node):
    while head and head.next:
        print(f"{head.val} ->", end=" ")
        head = head.next
    print(head.val)
    

def main():
    linked_list = LinkedListOne()
    linked_list.append(38)
    linked_list.append(27)
    linked_list.append(43)
    linked_list.append(3)
    linked_list.append(9)
    linked_list.append(82)
    linked_list.append(10)
    head = merge_sort_linked_list(linked_list.head)
    print_result(head)

if __name__ == "__main__":
    main()
