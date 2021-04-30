#include <stdio.h>
#include <stdlib.h>

#define NUM 100000000
int main()
{
    int x, y, pl, prime;
    int* p = malloc(sizeof(int) * NUM);
    p[0] = 2;
    pl = 1;
    for (x = 2; x != NUM; ++x)
    {
        prime = 1;
        for (y = 0; y != pl; ++y)
        {
            if (p[y]*p[y]>x)
            {
                break;
            }
            if (x % p[y] == 0)
            {
                prime = 0;
                
                break;
            }
        }
        if (prime == 1)
        {
            p[pl++] = x;
        }
    }
    printf("%d", p[pl - 1]);
    return 0;

}