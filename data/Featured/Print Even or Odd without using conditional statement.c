#include<stdio.h> 
int main() 
{ 
    int no; 
    printf("Enter a no: "); 
    scanf("%d", &no); 
    (no & 1 && printf("odd"))|| printf("even"); 
    return 0; 
} 