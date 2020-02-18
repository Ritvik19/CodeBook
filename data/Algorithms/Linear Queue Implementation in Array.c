#include<stdio.h>
#include<conio.h>
#include<process.h>

#define  MAX 5
int queue[MAX],rear = -1, front = 0;

int isfull()
{
  if(rear == MAX-1)
    return 1;
  return 0;
}

int isempty()
{
  if(front == rear+1)
    return 1;
  return 0;
}

void ins()
{
  if(!isfull())
  {
    rear += 1;
    printf("Element??? ");
    scanf("%d", &queue[rear]);
  }
  else
    printf("Queue is full\n");
}

void del()
{
  if(!isempty())
    front += 1;
  else
    printf("Queue is empty\n");
}

void display()
{
  for(int i=front; i<=rear; i++)
    printf("%d ", queue[i]);
  printf("\n");
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
    printf("F= %d R= %d\n", front, rear);
	printf("Press 1 to insert\n");
    printf("Press 2 to delete\n");
    printf("Press 0 to exit\n");
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
    printf("F= %d R= %d\n", front, rear);
    printf("Continue(1/0)??? ");
    scanf("%d",&cont);
    system("CLS");
  }while(cont != 0);
  getch();
  return 0;
}

