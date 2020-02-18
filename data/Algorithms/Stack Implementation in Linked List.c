#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<malloc.h>

struct node
{
  int info;
  struct node *next;
};

struct node* push(struct node *top, int data)
{
  struct node *newptr = (struct node*)malloc(sizeof(struct node));
  newptr->info = data;
  if(top == NULL)
    newptr->next = NULL;
  else
    newptr->next = top;
  top = newptr;
  return top;
}

struct node* pop(struct node *top)
{
  struct node *ptr = top;
  top = top->next;
  free(ptr);
  return top;
}

int peak(struct node *top)
{
  return top->info;
}

void display(struct node *top)
{
  struct node *ptr = top;
  printf("Stack :\n");
  while(ptr != NULL)
  {
     printf("\t%d\n", ptr->info);
     ptr = ptr->next;
  }
}

int main()
{
  struct node *top = NULL;
  int data, choice;
  while(1)
  {
  	system("Cls");
    printf("Stack Implementation Using Linked List");
    printf("\nPress 1 to push");
    printf("\nPress 2 to pop");
    printf("\nPress 3 to peak");
    printf("\nChoice??? ");
    scanf("%d", &choice);
    switch(choice)
    {
      case 1 :
        printf("Data??? ");
        scanf("%d", &data);
        top = push(top, data);
        break;
      case 2 :
      	if(top != NULL)
          top = pop(top);
        else
          printf("Stack Under Flow\n");
        break;
      case 3:
        data = peak(top);
        printf("Data = %d", data);
        break;
      case 0:
        return 0;
      deafault:
        printf("Invalid Choice");
    }
    display(top);
    getch();
  }
  getch();
  return 0;
}

