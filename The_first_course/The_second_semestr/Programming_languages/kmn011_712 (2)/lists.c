#include "lists.h"



static void* xmalloc111(size_t size) {
    void *cur = malloc(size);
    if (cur == NULL) exit(123);
    return cur;
}

static t_list1* create_new_node1(int key, int data) {
    t_list1 *new_node = xmalloc111(sizeof(t_list1));
    new_node->key = key;
    new_node->data = data;
    new_node->next = NULL;

    return new_node;
}

static t_list2* xmalloc222(size_t size) {
    t_list2 *cur = malloc(size);
    if (cur == NULL) exit(123);
    return cur;
}

static t_list2* create_new_node2(int key, int data) {
    t_list2 *new_node = xmalloc222(sizeof(t_list2));
    new_node->key = key;
    new_node->data = data;
    new_node->prev = NULL;
    new_node->next = NULL;
    return new_node;
}



t_list1* del_tail1(t_list1 *head) {
    t_list1 *cur = head;
    
    if (head == NULL) return NULL;
    if (head->next == NULL) {
        free(head);
        return NULL;
    }
    
    while (cur->next->next != NULL)
        cur = cur->next;
    
    free(cur->next);
    cur->next = NULL;
    return head;
}

t_list1* del_ptr1(t_list1 *head, t_list1 *ptr) {
    t_list1 *cur = head;
    
    if (head == NULL || ptr == NULL) return head;
    
    if (head == ptr) {
        head = head->next;
        free(ptr);
        return head;
    }
    
    while (cur != NULL && cur->next != ptr)
        cur = cur->next;
    
    if (cur != NULL) {
        cur->next = ptr->next;
        free(ptr);
    }
    
    return head;
}

t_list1* del_key1(t_list1 *head, int key) {
    t_list1 *cur = head, *tmp;
    
    if (head == NULL) return NULL;
    
    if (head->key == key) {
        tmp = head;
        head = head->next;
        free(tmp);
        return head;
    }
    
    while (cur->next != NULL && cur->next->key != key)
        cur = cur->next;
    
    if (cur->next != NULL) {
        tmp = cur->next;
        cur->next = tmp->next;
        free(tmp);
    }
    
    return head;
}

t_list1* add_akey1(t_list1 *head, int key, int data) {
    t_list1 *new_node = create_new_node1(key, data);
    t_list1 *cur = head;
    
    if (head == NULL) return new_node;
    
    while (cur != NULL && cur->key != key)
        cur = cur->next;
    
    if (cur != NULL) {
        new_node->next = cur->next;
        cur->next = new_node;
    } else {
        free(new_node);
    }
    
    return head;
}

t_list1* add_bkey1(t_list1 *head, int key, int data) {
    t_list1 *new_node = create_new_node1(key, data);
    t_list1 *cur = head;
    
    if (head == NULL) {
        head = new_node;
        return head;
    }
    
    if (head->key == key) {
        new_node->next = head;
        return new_node;
    }
    
    while (cur->next != NULL && cur->next->key != key)
        cur = cur->next;
    
    if (cur->next != NULL) {
        new_node->next = cur->next;
        cur->next = new_node;
    } else {
        free(new_node);
    }
    
    return head;
}



t_list2* del_tail2(t_list2 *head) {
    t_list2 *cur = head;
    
    if (head == NULL) return NULL;
    if (head->next == NULL) {
        free(head);
        return NULL;
    }
    
    while (cur->next != NULL)
        cur = cur->next;
    
    cur->prev->next = NULL;
    free(cur);
    return head;
}

t_list2* del_ptr2(t_list2 *head, t_list2 *ptr) {
    if (head == NULL || ptr == NULL) return head;
    
    if (ptr == head) {
        head = ptr->next;
        if (head != NULL) head->prev = NULL;
        free(ptr);
        return head;
    }
    
    if (ptr->prev != NULL) ptr->prev->next = ptr->next;
    if (ptr->next != NULL) ptr->next->prev = ptr->prev;
    
    free(ptr);
    return head;
}

t_list2* del_key2(t_list2 *head, int key) {
    t_list2 *cur = head;
    
    if (head == NULL) return NULL;
    
    while (cur != NULL && cur->key != key)
        cur = cur->next;
    
    if (cur != NULL) {
        if (cur == head) {
            head = cur->next;
            if (head != NULL) head->prev = NULL;
        } else {
            if (cur->prev != NULL) cur->prev->next = cur->next;
            if (cur->next != NULL) cur->next->prev = cur->prev;
        }
        free(cur);
    }
    
    return head;
}

t_list2* add_akey2(t_list2 *head, int key, int data) {
    t_list2 *new_node = create_new_node2(key, data);
    t_list2 *cur = head;
    
    if (head == NULL) return new_node;
    
    while (cur != NULL && cur->key != key)
        cur = cur->next;
    
    if (cur != NULL) {
        new_node->prev = cur;
        new_node->next = cur->next;
        if (cur->next != NULL) cur->next->prev = new_node;
        cur->next = new_node;
    } else {
        free(new_node);
    }
    
    return head;
}

t_list2* add_bkey2(t_list2 *head, int key, int data) {
    t_list2 *new_node = create_new_node2(key, data);
    t_list2 *cur = head;
    
    if (head == NULL) {
        free(new_node);
        return NULL;
    }
    
    if (head->key == key) {
        new_node->next = head;
        head->prev = new_node;
        return new_node;
    }
    
    while (cur != NULL && cur->key != key)
        cur = cur->next;
    
    if (cur != NULL) {
        new_node->prev = cur->prev;
        new_node->next = cur;
        if (cur->prev != NULL) cur->prev->next = new_node;
        cur->prev = new_node;
    } else {
        free(new_node);
    }
    
    return head;
}