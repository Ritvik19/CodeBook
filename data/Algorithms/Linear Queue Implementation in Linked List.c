#include<stdio.h>
#include<conio.h>
#include<malloc.h>
#include<stdlib.h>

struct node
{
	int info;
	struct node *next;
}*front = NULL, *rear = NULL, *ptr, *newptr;

int isempty()
{
	if(front == NULL)
		return 1;
	return 0;
}

void ins()
{
	newptr = (struct node*)malloc(sizeof(struct node));
	printf("Data? ");
	scanf("%d", &newptr->info);
	newptr->next = NULL;
	if(front == NULL)
	{
		front = newptr;
		rear = front;
	}
	else
	{
		rear->next = newptr;
		rear = rear->next;
	}
}

void del()
{
	if(!isempty())
	{
		ptr = front;
		front = front->next;
		free(ptr);
	}
}

void display()
{
	if(!isempty())
	{
		ptr = front;
		while(ptr != rear)
		{
			printf("%d ", ptr->info);
			ptr = ptr->next;
		}
		printf("%d", rear->info);
	}
}

int main()
{
  system("CLS");
  int ch, cont;
  do
  {
    printf("Queue Implementation in Array\n");
    printf("Queue: ");
    if(isempty())
      printf("Empty");
    display();
	printf("\nPress 1 to insert");
    printf("\nPress 2 to delete");
    printf("\nPress 0 to exit  ");
    scanf("%d", &ch);
    switch(ch)
    {
      case  1 : ins();
		break;
      case  2 : del();
		break;
      case  0 : exit(0);
      default : printf("\nInvalid Choice\n");
    }
    printf("Queue: ");
    if(isempty())
      printf("Empty");
    display();
    printf("\nContinue(1/0)??? ");
    scanf("%d",&cont);
    system("CLS");
  }while(cont != 0);
  getch();
  return 0;
}
