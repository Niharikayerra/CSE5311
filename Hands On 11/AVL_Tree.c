#include<stdio.h>
#include<stdlib.h>

struct Node {
    int key;
    struct Node *left;
    struct Node *right;
    int height;
};

struct Node *newnode(int key) {
    struct Node *node = (struct Node *)malloc(sizeof(struct Node));
    node->key = key;
    node->left = NULL;
    node->right = NULL;
    node->height = 1;
    return node;
}

int max(int a, int b) {
    return (a>b) ? a:b;
}

int height(struct Node *N) {
    if(N==NULL)
    return 0;
    return N->height;
}

int getbalance (struct Node *N) {
    if(N==NULL)
    return 0;
    return height (N->left) - height(N->right);
}

struct Node *rightrotate(struct Node *y) {
    struct Node *x = y->left;
    struct Node *T2 = x->right;
    x->right = y;
    y->left = T2;
    y->height = max(height(y->left),height(y->right))+1;
    x->height = max(height(x->left), height(x->right))+1;
    return x;
}

struct Node *leftrotate(struct Node *x) {
    struct Node *y = x->right;
    struct Node *T2 = y->left;
    y->left = x;
    x->right =T2;
    x->height = max(height(x->left), height(x->right))+1;
    y->height = max(height(y->left), height(y->right))+1;
    return y;
}

struct Node *insert(struct Node *node, int key) {
    if(node==NULL)
       return newnode(key);
    if(key<node->key)
       node->left = insert(node->left,key);
    else if(key>node->key)
       node->right = insert(node->right, key);
    else
       return node;
    node->height = 1+max(height(node->left), height(node->right));
    int balance = getbalance(node);
    if(balance>1 && key<node->left->key)
       return rightrotate(node);
    if(balance<-1 && key>node->right->key)
       return leftrotate(node);
    if(balance>1 && key>node->left->key){
       node->left = leftrotate(node->left);
       return rightrotate(node);
    }
    if(balance<-1 && key<node->right->key){
        node->right = rightrotate(node->right);
        return leftrotate(node);
    }
    return node;
}

struct Node *minvaluenode(struct Node *node) {
    struct Node *current = node;
    while(current->left!=NULL)
        current =current->left;
    return current;
}

struct Node *deletenode(struct Node *root, int key) {
    if(root==NULL)
       return root;
    if(key<root->key)
       root->left = deletenode(root->left, key);
    else if(key>root->key)
       root->right = deletenode(root->right, key);
    else {
        if((root->left==NULL)||(root->right==NULL)){
            struct Node *temp = root->left ? root->left : root->right;
            if(temp==NULL) {
                temp = root;
                root = NULL;
            } else
                *root = *temp;
            free(temp);
        } else {
            struct Node *temp = minvaluenode(root->right);
            root->key = temp->key;
            root->right = deletenode(root->right, temp->key);
        }
    }
    if(root==NULL)
      return root;
    root->height = 1+ max(height(root->left), height(root->right));
    int balance = getbalance(root);
    if(balance > 1 && getbalance(root->left)>=0)
       return rightrotate(root);
    if(balance<=-1 && getbalance(root->right) <=0)
       return leftrotate(root);
    if(balance>1 && getbalance(root->left)<0) {
        root->left = leftrotate(root->left);
        return rightrotate(root);
    }
    if(balance<-1 && getbalance(root->right)>0) {
        root->right = rightrotate(root->right);
        return leftrotate(root);
    }
    return root;
}

void preorder(struct Node *root) {
    if(root!=NULL) {
       printf("%d ",root->key);
       preorder(root->left);
       preorder(root->right);
    }
}

struct Node *search(struct Node *root, int key) {
    if(root==NULL || root->key==key)
       return root;
    if(root->key<key)
       return search(root->right,key);
    return search(root->left,key);
}

int main() {
    struct Node *root = NULL;
    int keys_to_insert[] = {5, 8, 20, 0, 9, 13, -2, 3, 4};
    int n = sizeof(keys_to_insert) / sizeof(keys_to_insert[0]);
    for (int i = 0; i < n; i++)
        root = insert(root, keys_to_insert[i]);
    printf("AVL tree after insertion:\n");
    preorder(root);
    printf("\n");
    int keys_to_search[] = {9, 7, 20, 4};
    int m = sizeof(keys_to_search) / sizeof(keys_to_search[0]);
    for (int i = 0; i < m; i++) {
        if (search(root, keys_to_search[i]))
            printf("%d found in the AVL tree\n", keys_to_search[i]);
        else
            printf("%d not found in the AVL tree\n", keys_to_search[i]);
    }
    int keys_to_delete[] = {20, 13};
    int k = sizeof(keys_to_delete) / sizeof(keys_to_delete[0]);
    for (int i = 0; i < k; i++) {
        root = deletenode(root, keys_to_delete[i]);
        printf("AVL tree after deleting %d:\n", keys_to_delete[i]);
        preorder(root);
        printf("\n");
    }
    return 0;
}
