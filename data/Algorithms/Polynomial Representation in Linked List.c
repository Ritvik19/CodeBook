#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<malloc.h>

struct node
{
	float coeff, exp;
	struct node *next;
} *first, *firsta, *firstb, *firstc, *ptr, *newptr, *p, *q, *r;

struct node* create()
{
	first = NULL;
	int cont;
	do
	{
		newptr = (struct node*)malloc(sizeof(struct node));
		printf("Coefficient and Exponent??? ");
		scanf("%f%f", &newptr->coeff, &newptr->exp);
		newptr->next = NULL;
		if(first == NULL)
		{
			first = newptr;
			ptr = newptr;
		}
		else
		{
			ptr->next = newptr;
			ptr = ptr->next;
		}
		printf("Continue???(1/0) ");
		scanf("%d", &cont);		
	}while(cont != 0);
	return first;
}

void display(struct node *first)
{
	ptr = first;
	while(ptr != NULL)
	{
		printf("%f x^%f\t", ptr->coeff, ptr->exp);
		ptr = ptr->next;
	}
}

void addit(struct node *firsta, struct node *firstb)
{
	p = firsta;
	q = firstb;
	firstc = NULL;
	while(p != NULL && q != NULL)
	{
		r = (struct node*)malloc(sizeof(struct node));
		if(p->exp == q->exp)
		{
			r->exp = p->exp;
			r->coeff = p->coeff + q->coeff;
			p = p->next;
			q = q->next;
		}
		else if (p->exp > q->exp)
		{
			r = p;
			p = p->next;
		}
		else
		{
			r = q;
			q = q->next;
		}
		if(firstc == NULL)
		{
			firstc = r;
			ptr = firstc;
		}
		else
		{
			ptr->next = r;
			ptr = ptr->next;
		}
	}	
	if(p != NULL)
		ptr->next = p;
	else if(q != NULL)
		ptr->next = q;
	else
		ptr->next = NULL;
}

int main()
{
	printf("Polynomial Repesentation in Linked List");
	printf("\nPolynomial A\n");
	firsta = create();
	display(firsta);
	printf("\nPolynomial B\n");
	firstb = create();
	display(firstb);
	printf("\nPolynomial Sum\n");
	addit(firsta, firstb);
	display(firstc);
	getch();
	return 0;
}
