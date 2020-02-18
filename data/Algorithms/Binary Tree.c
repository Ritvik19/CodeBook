#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<malloc.h>

struct node
{
    char info;
    node *left, *right;
}*root,*ptr;

void inorder(node *tree)
{
    if(tree != NULL)
    {
        inorder(tree->left);
        printf("%c  ", tree->info);
        inorder(tree->right);
    }
}

void preorder(node *tree)
{
    if(tree != NULL)
    {
        printf("%c  ", tree->info);
        preorder(tree->left);
        preorder(tree->right);
    }
}

void postorder(node *tree)
{
    if(tree != NULL)
    {
        postorder(tree->left);
        postorder(tree->right);
        printf("%c  ", tree->info);
    }
}

node *create(char x)
{
    node *n = (node*)malloc(sizeof(node));
    n->info = x;
    n->left = NULL;
    n->right = NULL;
    return n;
}

void setleft(node *tree, char x)
{
    if(tree ==NULL) printf("Void Insertion");
    else if(tree->left != NULL) printf("Invalid Insertion");
    else tree->left = create(x);
}

void setright(node *tree, char x)
{
    if(tree ==NULL) printf("Void Insertion");
    else if(tree->right != NULL) printf("Invalid Insertion");
    else tree->right = create(x);
}

int main()
{
    int choice;
    char data;
    printf("Binary Tree");
    printf("\nRoot Element? ");
    fflush(stdin);
    scanf("%c", &data);
    root = create(data);
    ptr = root;			
    while(1)
    {
        system("CLS");
        printf("Inorder\n");
        inorder(root);
        printf("\nPreorder\n");
        preorder(root);
        printf("\nPostorder\n");
        postorder(root);

        printf("\nBinary Tree\n");
        printf("Press 1 to insert at left\n");
        printf("Press 2 to insert at right\n");
        printf("Press 3 to traverse to root\n");
        printf("Press 4 to traverse left\n");		
        printf("Press 5 to traverse right\n");
        printf("Press 0 to exit\n");
        printf("Choice? ");
        scanf("%d", &choice);
        switch(choice)
        {
            case  1 : printf("Element? ");
                    fflush(stdin);
                    scanf("%c", &data);
                    setleft(ptr, data);
                    break;
            case  2 : printf("Element? ");
                    fflush(stdin);
                    scanf("%c", &data);
                    setright(ptr, data);
                    break;
            case  3 : ptr = root;
                    break;
            case  4 : ptr = ptr->left;
                    break;
            case  5 : ptr = ptr->right;
                    break;
            case  0 : exit(0);
            default : printf("Wrong Choice");			
        }
    }
    return 0;
}
