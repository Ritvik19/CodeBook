#include <iostream>

using namespace std;

void swap1(int x, int y){
    cout<<"call-by-value"<<endl;
    cout<<"Address of x and y inside the function "<<"\t"<<&x<<"\t"<<&y<<endl;
    int temp;
    temp = x;
    x = y;
    y = temp;
}

void swap2(int *x, int *y){
    cout<<"call-by-reference with pointer argument"<<endl;
    cout<<"Address of x and y inside the function "<<"\t"<<x<<"\t"<<y<<endl;
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void swap3(int& x, int& y) {
    cout<<"call-by-reference with reference argument"<<endl;
    cout<<"Address of x and y inside the function "<<"\t"<<&x<<"\t"<<&y<<endl;
    int temp;
    temp = x;
    x = y;
    y = temp;
}

int main()
{
    int a=5, b=10;
    cout<<"Initial values of a and b "<<"\t"<<a<<"\t"<<b<<endl;
    cout<<"Address of a and b "<<"\t"<<&a<<"\t"<<&b<<endl;
    cout<<"Calling Swap1"<<endl;
    swap1(a, b);
    cout<<"Values of a and b "<<"\t"<<a<<"\t"<<b<<endl;
    cout<<"Calling Swap2"<<endl;
    swap2(&a, &b);
    cout<<"Values of a and b "<<"\t"<<a<<"\t"<<b<<endl;
    cout<<"Calling Swap3"<<endl;
    swap3(a, b);
    cout<<"Values of a and b "<<"\t"<<a<<"\t"<<b<<endl;
}