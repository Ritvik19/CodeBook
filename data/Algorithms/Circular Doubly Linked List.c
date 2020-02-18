#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<malloc.h>

struct node
{
	int info;
	struct node *prev, *next;
}*first, *ptr, *newptr, *ptr1, *ptr2, *last;

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
		newptr->prev = NULL;
		if(first == NULL)
		{
			first = newptr;
			last = first;
		}
		else
		{
			last->next = newptr;
			newptr->prev = last;
			last = newptr;
		}
		first->prev = last;
		last->next = first;
		printf("Continue(1/0)? ");
		scanf("%d", &cont);
	}while(cont != 0);
}

void display()
{
	ptr = first;
	printf("Beg<->");
	do
	{
		printf(" %d <->", ptr->info);
		ptr = ptr->next;
	}while(ptr != first);
	printf("End");
}

void displayrev()
{
	ptr = last;
	printf("End<->");
	do
	{
		printf(" %d <->", ptr->info);
		ptr = ptr->prev;
	}while(ptr != last);
	printf("Beg");
}

void insertbeg()
{
	newptr = (struct node*)malloc(sizeof(struct node));
	printf("Data? ");
	scanf("%d", &newptr->info);
	newptr->prev = last;
	newptr->next = first;
	first->prev = newptr;
	last->next = newptr;
	first = newptr;
}

void insertend()
{
	newptr = (struct node*)malloc(sizeof(struct node));
	printf("Data? ");
	scanf("%d", &newptr->info);
	newptr->prev = last;
	newptr->next = first;
	first->prev = newptr;
	last->next = newptr;
	last = newptr;
}

void insertmid(int k)
{
	newptr = (struct node*)malloc(sizeof(struct node));
	printf("Data? ");
	scanf("%d", &newptr->info);
	newptr->next = NULL;
	newptr->prev = NULL;
	ptr = first;
	for(int i=1; i<k; i++)
		ptr = ptr->next;
	ptr1 = ptr->next;	
	newptr->next = ptr1;
	ptr1->prev = newptr;
	ptr->next = newptr;
	newptr->prev = ptr;;
}

void deletebeg()
{
	ptr = first;
	first = first->next;
	last->next = first;
	first->prev = last;
	free(ptr);
}

void deleteend()
{
	ptr = last;
	last = last->prev;
	last->next = first;
	first->prev = last;
	free(ptr);
}

void deletemid(int k)
{
	ptr = first;
	for(int i=1; i<k; i++)
		ptr = ptr->next;
	ptr1 = ptr->prev;
	ptr2 = ptr->next;	
	ptr1->next = ptr2;
	ptr2->prev = ptr1;
	free(ptr);
}

int main()
{
	int choice, index;
	system("CLS");
	printf("Implementation of Linear Singly Linked List\n");
	create();
	display();
	printf("\n");
	displayrev();
	getch();
	while(1)
	{
		system("CLS");
		display();
		printf("\n");
		displayrev();
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
		printf("\n");
		displayrev();
		count();
	}
    return 0;
}
