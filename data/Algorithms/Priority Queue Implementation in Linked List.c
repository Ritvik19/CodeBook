#include<stdio.h>
#include<conio.h>
#include<malloc.h>
#include<stdlib.h>

struct node
{
	int info, priority;
	struct node *next;
}*front = NULL, *rear = NULL, *ptr, *newptr, *ptr1;

int isempty()
{
	if(front == NULL)
		return 1;
	return 0;
}

void ins()
{
	newptr = (struct node*)malloc(sizeof(struct node));
	printf("Data and Priority? ");
	scanf("%d%d", &newptr->info, &newptr->priority);
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

int gethighestpriority()
{
	if(!isempty())
	{
		int max = front->priority;
		ptr = front;
		while(ptr != NULL)
		{
			if(ptr->priority > max)
				max = ptr->priority;
			ptr = ptr->next;	
		}
		return max;
	}
	return -1;
}

void del()
{
	if(!isempty())
	{
		ptr = front;
		while(ptr->priority != gethighestpriority())
		{
			ptr1 = ptr;
			ptr = ptr->next;
		}
		ptr1->next = ptr->next;
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
			printf("%d: %d\t", ptr->info, ptr->priority);
			ptr = ptr->next;
		}
		printf("%d: %d\t", rear->info, rear->priority);
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
    printf("%d", gethighestpriority());
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
