#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<malloc.h>

struct node
{
	int info;
	struct node *next;
}*first, *ptr, *newptr, *ptr1, *last;

int count()
{
	int i=0;
	ptr = first;
	do
	{
		i++;
		ptr = ptr->next;
	}while(ptr != first);
	return i;
}

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
			last = first;
		}
		else
		{
			last->next = newptr;
			last = last->next;
		}
		last->next = first;
		printf("Continue(1/0)? ");
		scanf("%d", &cont);
	}while(cont != 0);
}

void display()
{
	ptr = first;
	do
	{
		printf("%d->", ptr->info);
		ptr = ptr->next;
	}while(ptr != first);
	printf("End");
}

void insertbeg()
{
	newptr = (struct node*)malloc(sizeof(struct node));
	printf("Data? ");
	scanf("%d", &newptr->info);
	newptr->next = first;
	first = newptr;
	last->next = first;
}

void insertend()
{
	newptr = (struct node*)malloc(sizeof(struct node));
	printf("Data? ");
	scanf("%d", &newptr->info);
	newptr->next = first;
	last->next = newptr;
	last = newptr;
}

void insertmid(int k)
{
	newptr = (struct node*)malloc(sizeof(struct node));
	printf("Data? ");
	scanf("%d", &newptr->info);
	newptr->next = NULL;
	ptr = first;
	for(int i=1; i<k; i++)
		ptr = ptr->next;
	newptr->next = ptr->next;
	ptr->next = newptr;
}

void deletebeg()
{
	ptr = first;
	last->next = ptr->next;
	first = ptr->next;
	free(ptr);
}

void deleteend()
{
	ptr = first;
	while(ptr != last)
	{
		ptr1 = ptr;
		ptr = ptr->next;
	}
	ptr1->next = first;
	last = ptr1;
	free(ptr);
}

void deletemid(int k)
{
	ptr = first;
	for(int i=1; i<k; i++)
	{
		ptr1 = ptr;
		ptr = ptr->next;
	}
	ptr1->next = ptr->next;
	free(ptr);
}

int main()
{
	int choice, index;
	system("CLS");
	printf("Implementation of Circular Singly Linked List\n");
	create();
	display();
	getch();
	while(1)
	{
		system("CLS");
		display();
		printf("\nCount %d", count());
		printf("\nPress 1 for insertion");
		printf("\nPress 2 for deletion");
		printf("\nPress 0 to exit");
		printf("\nChoice? ");
		scanf("%d", &choice);
		switch(choice)
		{
			case 1 :
				printf("Index? ");
				scanf("%d", &index);
				if(index == 0)
					insertbeg();
				else if(index <= count())
					insertmid(index);
				else
					insertend();
				break;
			case 2 :
				printf("Index? ");
				scanf("%d", &index);
				if(index == 1)
					deletebeg();
				else if(index <= count())
					deletemid(index);
				else
					deleteend();
				break;	
			case 0 :
				return 0;
		}	
		display();
		count();
	}
    return 0;
}
