#include<stdio.h>
#include<stdlib.h>
 
struct TreeNode {
    int value;
    struct TreeNode* left;
    struct TreeNode* right;
};

struct TreeNode* createnode(int value) {
    struct TreeNode* newnode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    newnode->value = value;
    newnode->left = NULL;
    newnode->right =NULL;
    return newnode;
}

struct TreeNode* insert(struct TreeNode* root, int value) {
    if(root==NULL)
      return createnode(value);
    if(value<root->value) {
        root->left = insert(root->left, value);
    } else if(value>root->value) {
        root->right = insert(root->right, value);
    }
    return root;
}

int search(struct TreeNode* root, int value) {
    if(root==NULL) {
        return 0;
    }
    if(root->value==value) {
        return 1;
    } else if(value<root->value) {
        return search(root->left,value);
    } else {
        return search(root->right,value);
    }
}

struct TreeNode* minvaluenode(struct TreeNode* node) {
    struct TreeNode* current = node;
    while(current->left!=NULL) {
        current = current->left;
    }
    return current;
}

struct TreeNode* deletenode(struct TreeNode* root, int value) {
    if(root==NULL){
        return root;
    }
    if(value<root->value) {
        root->left = deletenode(root->left , value);
    } else if(value>root->value) {
        root->right = deletenode(root->right, value);
    } else {
        if(root->left == NULL) {
            struct TreeNode* temp = root->right;
            free(root);
            return temp;
        }
        struct TreeNode* temp = minvaluenode(root->right);
        root->value = temp->value;
        root->right = deletenode(root->right, temp->value);
    }
    return root;
}

void inorderTraversal(struct TreeNode* root) {
    if(root!=NULL){
        inorderTraversal(root->left);
        printf("%d ", root->value);
        inorderTraversal(root->right);
    }
}

int main() {
    struct TreeNode* root = NULL;
    int elements[] = {6, 2, 5, 1, 4, 8, 3,9};
    int n = sizeof(elements)/sizeof(elements[0]);
    for(int i=0;i<n;i++) {
        root = insert(root, elements[i]);
        printf("Tree as list after insertion of %d: ", elements[i]);
        inorderTraversal(root);
        printf("\n");
    }
    printf("Inorder Traversal:\n");
    inorderTraversal(root);
    printf("\n\n");
    printf("Search 7: %s\n",search(root,7)? "Found" : "Not Found");
    printf("Search 2: %s\n",search(root,2)? "Found" : "Not Found");
    deletenode(root,3);
    printf("Inorder Traversal after deletion of %d is:\n");
    inorderTraversal(root);
    printf("\n");
    return 0;
}