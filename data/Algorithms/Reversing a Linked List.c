#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<malloc.h>

struct node
{
	int info;
	struct node *next;
}*first, *ptr, *newptr, *ptr1, *first_rev;

void create()
{
	int cont;
	first = NULL;
	do{
		newptr = (struct node*)malloc(sizeof(struct node));
		printf("Data? ");
		scanf("%d", &newptr->info);
		newptr->next = NULL;
		if(first == NULL)
		{
			first = newptr;
			ptr = first;
		}
		else
		{
			ptr->next = newptr;
			ptr = ptr->next;
		}
		printf("Continue(1/0)? ");
		scanf("%d", &cont);
	}while(cont != 0);
}

void display(struct node *f)
{
	ptr = f;
	while(ptr != NULL)
	{
		printf("%d->", ptr->info);
		ptr = ptr->next;
	}
	printf("End");
}

void reverse()
{
	ptr = first;
	first_rev == NULL;
	while(ptr != NULL)
	{
		newptr = (struct node*)malloc(sizeof(struct node));
		newptr->info = ptr->info;
		if(first_rev == NULL)
			newptr->next = NULL;
		else
			newptr->next = first_rev;
		first_rev = newptr;
		ptr = ptr->next;
	}
}

int main()
{
	int choice, index;
	system("CLS");
	printf("Implementation of Linear Singly Linked List\n");
	create();
	display(first);
	getch();
	reverse();
	printf("\n");
	display(first_rev);
	getch();
    return 0;
}
