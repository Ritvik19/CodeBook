#include<stdio.h>
#include<conio.h>
#include<process.h>
#define  MAX 20

int stack[MAX],top = -1;

int isfull()
{
  if(top == MAX-1)
    return 1;
  return 0;
}

int isempty()
{
  if(top == -1)
    return 1;
  return 0;
}

void push()
{
  if(isfull() == 0)
  {
    top += 1;
    printf("Element??? ");
    scanf("%d", &stack[top]);
  }
  else
    printf("Stack is full\n");
}

void pop()
{
  if(isempty() == 0)
    top -= 1;
  else
    printf("Stack is empty\n");
}

void display()
{
  printf("\n");	
  for(int i=top; i>=0; i--)
    printf("\t%d\n", stack[i]);
}

void peak()
{
  printf("%d\n", stack[top]);
}

int main()
{
  system("CLS");
  int ch, cont;
  do
  {
    printf("Stack Implementation in Array\n");
    printf("Stack: ");
    if(isempty() == 1)
      printf("Empty");
    display();
    printf("Press 1 to push\n");
    printf("Press 2 to pop\n");
    printf("Press 3 to peak\n");
    printf("Press 0 to exit\n");
    scanf("%d", &ch);
    switch(ch)
    {
      case  1 : push();
		break;
      case  2 : pop();
		break;
      case  3 :  peak();
		break;
      case  0 : exit(0);
      default : printf("\nInvalid Choice\n");
    }
    printf("Stack: ");
    if(isempty() == 1)
      printf("Empty");
    display();
    printf("Continue(1/0)??? ");
    scanf("%d",&cont);
    system("CLS");
  }while(cont != 0);
  getch();
  return 0;
}

