#include<stdio.h>
#include<stdlib.h>
typedef struct Node
{
    int key;
    int value;
    struct Node* next;
    struct Node* prev;
}Node;

//Define doubly linked list structure
typedef struct Doublylinkedlist
{
    Node* head;
    Node* tail;
}Doublylinkedlist;

Node* createNode(int key, int value)
{
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->key = key;
    newNode->value = value;
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}
void append(Doublylinkedlist* list, int key, int value)
{
    Node* newNode = createNode(key,value);
    if(list->head == NULL)
    {
        list->head = newNode;
        list->tail = newNode;
    }
    else
    {
        list->tail->next = newNode;
        newNode->prev = list->tail;
        list->tail = newNode;
    }
}
void removenode(Doublylinkedlist* list, Node* node)
{
    if(node->prev)
    {
        node->prev->next =  node->next;
    }
    else
    {
        list->head = node->next;
    }
    if(node->next)
    {
        node->next->prev = node->prev;
    }
    else
    {
        list->tail = node->prev; 
    }
    free(node);
}
typedef struct Hashtable
{
    int capacity;
    int size;
    Doublylinkedlist** array;
}Hashtable;
int hash_function_multiplication(int key, int capacity)
{
    float A = 0.5;
    return(int)(capacity*((key*A)-(int)(key*A)));
}
Hashtable* createhashtable(int initial_capacity)
{
    Hashtable* table = (Hashtable*)malloc(sizeof(Hashtable));
    table->capacity = initial_capacity;
    table->size = 0;
    table->array = (Doublylinkedlist**)malloc(initial_capacity*sizeof(Doublylinkedlist*));
    for(int i=0;i<initial_capacity;i++)
    {
        table->array[i] = NULL;
    }
    return(table);
}
void resize(Hashtable* table, int new_capacity);
void insert(Hashtable* table, int key, int value)
{
    int index = hash_function_multiplication(key, table->capacity);
    if(table->array[index]== NULL)
    {
        table->array[index] = (Doublylinkedlist*)malloc(sizeof(Doublylinkedlist));
        table->array[index]->head = NULL;
         table->array[index]->tail = NULL;
    }
    Doublylinkedlist* list = table->array[index];
    Node* current = list->head;
    while(current){
        if(current->key == key) {
            current->value == value;
            return;
        }
        current = current->next;
    }
    append(list, key,value);
    table->size++;
    if(table->size > table->capacity*2) {
        resize(table, table->capacity*2);
    }
}
int get(Hashtable* table, int key)
{
    int index = hash_function_multiplication(key, table->capacity);
    Doublylinkedlist* list = table->array[index];
    Node* current = list->head;
    while(current) {
        if(current->key == key) {
            return current->value;
        }
        current = current->next;
    }
    return -1;
}
void removekey(Hashtable* table, int key)
{
    int index = hash_function_multiplication(key, table->capacity);
    Doublylinkedlist* list = table->array[index];
    Node* current = list->head;
    while(current) {
        if(current->key == key) {
            removenode(list, current);
            table->size--;
            if(table->size < table->capacity/4) {
                resize(table, table->capacity/2);
            }
            return;
        }
        current = current->next;
    }
}
void resize(Hashtable* table, int new_capacity)
{
    Doublylinkedlist** old_array = table->array;
    int old_capacity = table->capacity;
    table->capacity = new_capacity;
    table->array = (Doublylinkedlist**)malloc(new_capacity*sizeof(Doublylinkedlist*));
    for(int i=0;i<new_capacity;i++)
    {
        table->array[i]=NULL;
    }
    for(int i=0;i<old_capacity;i++)
    {
        Doublylinkedlist* list = old_array[i];
        Node* current = list->head;
        while(current) {
            insert(table, current->key, current->value);
            Node* temp = current;
            current = current->next;
            free(temp);
        }
        free(list);
    }
    free(old_array);
}

void printtable(Hashtable* table)
{
    for(int i=0; i<table->capacity; i++)
    {
        printf("Index %d:", i);
        Doublylinkedlist* list = table->array[i];
        if(list != NULL)
        {
            Node* current = list->head;
            while(current) {
                printf("(%d: %d)%s", current->key, current->value, (current->next != NULL)? "->" : "");
                current = current->next;
            }
        }
        printf("\n");
    }
}
int main()
{
    Hashtable* hash_table = createhashtable(8);
    insert(hash_table, 4, 8);
    insert(hash_table, 7, 60);
    insert(hash_table, 5, 3);
    insert(hash_table, 3, 2000);
    printf("Hash Table:\n");
    printtable(hash_table);

    printf("Value for key 7 : %d\n", get(hash_table,7));
    removekey(hash_table,7);
    printf("After removing key 7:\n");
    printtable(hash_table);
    return 0;
}