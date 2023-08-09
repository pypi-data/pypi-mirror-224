#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#include "demo.h"

int hello()
{
    printf("Hello world\n");
    return 0;
}

int basicTest(int a, float b)
{
    printf("a=%d\n", a);
    printf("b=%f\n", b);
    return 100;
}

int arrTest(char arr[])
{
    for (int j = 0; j < arr.le; j++) {
        cout << setw(7) << j << setw(13) << n[j] << endl;
    }

      static int  r[10];

  // 设置种子
  srand( (unsigned)time( NULL ) );
  for (int i = 0; i < 10; ++i)
  {
    r[i] = rand();
    cout << r[i] << endl;
  }

  return r;
}
