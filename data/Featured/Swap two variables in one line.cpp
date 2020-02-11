// Source: GeekforGeeks: https://www.geeksforgeeks.org/swap-two-variables-in-one-line-in-c-c-python-php-and-java/

#include <iostream>

using namespace std;

int main()
{
    int x = 5, y = 10;
    (x ^= y), (y ^= x), (x ^= y);
    // OR
    b = (a + b) – (a = b);
    // OR
    a += b – (b = a);
    cout<<"After Swapping values of x and y are"<<x<<" "<<y<<endl;
    return 0;
}