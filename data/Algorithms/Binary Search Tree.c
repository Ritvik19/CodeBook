#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <malloc.h>

struct node
{
    int info;
    node *left, *right;
} * root, *ptr;

void inorder(node *tree)
{
    if (tree != NULL)
    {
        inorder(tree->left);
        printf("%d  ", tree->info);
        inorder(tree->right);
    }
}

void preorder(node *tree)
{
    if (tree != NULL)
    {
        printf("%d  ", tree->info);
        preorder(tree->left);
        preorder(tree->right);
    }
}

void postorder(node *tree)
{
    if (tree != NULL)
    {
        postorder(tree->left);
        postorder(tree->right);
        printf("%d  ", tree->info);
    }
}

node *insertNode(node *tree, int item)
{
    if (tree == NULL)
    {
        tree = (node *)malloc(sizeof(node));
        tree->left = tree->right = NULL;
        tree->info = item;
    }
    else
    {
        if (item < tree->info)
            tree->left = insertNode(tree->left, item);
        else if (item > tree->info)
            tree->right = insertNode(tree->right, item);
        else
            printf(" Duplicate Element !! Not Allowed !!!");
    }
    return tree;
}

node *minValueNode(node *subtree)
{
    node *current = subtree;
    while (current->left != NULL)
        current = current->left;
    return current;
}

node *deleteNode(node *root, int item)
{
    if (root == NULL)
        return root;

    if (item < root->info)
        root->left = deleteNode(root->left, item);

    else if (item > root->info)
        root->right = deleteNode(root->right, item);

    else
    {
        if (root->left == NULL)
        {
            node *temp = root->right;
            free(root);
            return temp;
        }
        else if (root->right == NULL)
        {
            node *temp = root->left;
            free(root);
            return temp;
        }

        node *temp = minValueNode(root->right);

        root->info = temp->info;

        root->right = deleteNode(root->right, temp->info);
    }
    return root;
}

int main()
{
    int choice, x;
    while (1)
    {
        system("CLS");

        printf("Inorder\n");
        inorder(root);
        printf("\nPreorder\n");
        preorder(root);
        printf("\nPostorder\n");
        postorder(root);

        printf("\nBinary Search Tree\n");
        printf("Press 1 to insert\n");
        printf("Press 2 to delete\n");
        printf("Press 0 to exit\n");
        printf("Choice? ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Element? ");
            scanf("%d", &x);
            root = insertNode(root, x);
            break;
        case 2:
            printf("Element? ");
            scanf("%d", &x);
            root = deleteNode(root, x);
            break;
        case 0:
            exit(0);
        default:
            printf("Wrong Choice");
        }
    }
    return 0;
}
