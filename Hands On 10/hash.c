#include <stdio.h>
#include <stdlib.h>

// Define Node structure
typedef struct Node {
    int key;
    int value;
    struct Node* next;
    struct Node* prev;
} Node;

// Define Doubly Linked List structure
typedef struct DoublyLinkedList {
    Node* head;
    Node* tail;
} DoublyLinkedList;

// Initialize a new node
Node* createNode(int key, int value) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->key = key;
    newNode->value = value;
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}

// Append a new node to the doubly linked list
void append(DoublyLinkedList* list, int key, int value) {
    Node* newNode = createNode(key, value);
    if (list->head == NULL) {
        list->head = newNode;
        list->tail = newNode;
    } else {
        list->tail->next = newNode;
        newNode->prev = list->tail;
        list->tail = newNode;
    }
}

// Remove a node from the doubly linked list
void removeNode(DoublyLinkedList* list, Node* node) {
    if (node->prev) {
        node->prev->next = node->next;
    } else {
        list->head = node->next;
    }
    if (node->next) {
        node->next->prev = node->prev;
    } else {
        list->tail = node->prev;
    }
    free(node);
}

// Define HashTable structure
typedef struct HashTable {
    int capacity;
    int size;
    DoublyLinkedList** array;
} HashTable;

// Hash function using multiplication method
int hash_function_multiplication(int key, int capacity) {
    float A = 0.5;
    return (int)(capacity * ((key * A) - (int)(key * A)));
}

// Initialize a new HashTable
HashTable* createHashTable(int initial_capacity) {
    HashTable* table = (HashTable*)malloc(sizeof(HashTable));
    table->capacity = initial_capacity;
    table->size = 0;
    table->array = (DoublyLinkedList**)malloc(initial_capacity * sizeof(DoublyLinkedList*));
    for (int i = 0; i < initial_capacity; i++) {
        table->array[i] = NULL;
    }
    return table;
}

// Resize the hash table
void resize(HashTable* table, int new_capacity);

// Insert a key-value pair into the hash table
void insert(HashTable* table, int key, int value) {
    int index = hash_function_multiplication(key, table->capacity);

    if (table->array[index] == NULL) {
        table->array[index] = (DoublyLinkedList*)malloc(sizeof(DoublyLinkedList));
        table->array[index]->head = NULL;
        table->array[index]->tail = NULL;
    }

    DoublyLinkedList* list = table->array[index];
    Node* current = list->head;
    while (current) {
        if (current->key == key) {
            current->value = value;
            return;
        }
        current = current->next;
    }

    append(list, key, value);
    table->size++;

    if (table->size > table->capacity * 2) {
        resize(table, table->capacity * 2);
    }
}

// Get the value associated with a key from the hash table
int get(HashTable* table, int key) {
    int index = hash_function_multiplication(key, table->capacity);
    DoublyLinkedList* list = table->array[index];

    Node* current = list->head;
    while (current) {
        if (current->key == key) {
            return current->value;
        }
        current = current->next;
    }
    return -1; // Key not found
}

// Remove a key-value pair from the hash table
void removeKey(HashTable* table, int key) {
    int index = hash_function_multiplication(key, table->capacity);
    DoublyLinkedList* list = table->array[index];

    Node* current = list->head;
    while (current) {
        if (current->key == key) {
            removeNode(list, current);
            table->size--;

            if (table->size < table->capacity / 4) {
                resize(table, table->capacity / 2);
            }
            return;
        }
        current = current->next;
    }
}

// Resize the hash table
void resize(HashTable* table, int new_capacity) {
    DoublyLinkedList** old_array = table->array;
    int old_capacity = table->capacity;
    table->capacity = new_capacity;
    table->array = (DoublyLinkedList**)malloc(new_capacity * sizeof(DoublyLinkedList*));

    for (int i = 0; i < new_capacity; i++) {
        table->array[i] = NULL;
    }

    for (int i = 0; i < old_capacity; i++) {
        DoublyLinkedList* list = old_array[i];
        Node* current = list->head;
        while (current) {
            insert(table, current->key, current->value);
            Node* temp = current;
            current = current->next;
            free(temp);
        }
        free(list);
    }
    free(old_array);
}

// Print the hash table
void printTable(HashTable* table) {
    for (int i = 0; i < table->capacity; i++) {
        printf("Index %d: ", i);
        DoublyLinkedList* list = table->array[i];
        if (list != NULL) {
            Node* current = list->head;
            while (current) {
                printf("(%d: %d)%s", current->key, current->value, (current->next != NULL) ? " -> " : "");
                current = current->next;
            }
        }
        printf("\n");
    }
}

int main() {
    HashTable* hash_table = createHashTable(8);
    insert(hash_table, 5, 10);
    insert(hash_table, 6, 50);
    insert(hash_table, 8, 3);
    insert(hash_table, 3, 1000);

    printf("Hash Table:\n");
    printTable(hash_table);

    printf("Value for key 3: %d\n", get(hash_table, 3));
    removeKey(hash_table, 3);
    printf("After removing key 3:\n");
    printTable(hash_table);

    return 0;
}
