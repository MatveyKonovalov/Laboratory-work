#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

typedef struct Node1 {
    int key;
    int data;
    struct Node1 *next;
} t_list1;


t_list1* del_tail1(t_list1 *head);
t_list1* del_ptr1(t_list1 *head, t_list1 *ptr);
t_list1* del_key1(t_list1 *head, int key);
t_list1* add_akey1(t_list1 *head, int key, int data);
t_list1* add_bkey1(t_list1 *head, int key, int data);



typedef struct Node2 {
    int key;
    int data;
    struct Node2 *next;
    struct Node2 *prev;
} t_list2;


t_list2* del_tail2(t_list2 *head);
t_list2* del_ptr2(t_list2 *head, t_list2 *ptr);
t_list2* del_key2(t_list2 *head, int key);
t_list2* add_akey2(t_list2 *head, int key, int data);
t_list2* add_bkey2(t_list2 *head, int key, int data);

#endif