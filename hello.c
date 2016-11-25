#include <stdio.h>

int main()
{
  int a = 2;

  if ( a >= 1 )
    {
      printf("Hello World!\n");
    }

  int b = 0;

  if ( b > -1 )
    {
      printf("NULL\n");
    }

  int c = 3;

  if ( c <= 3 )
    {
      c += 1;
    }

  int i;

  for ( i = 0; i < 10; i++ )
    {
      a += 1;
      b *= 2;
      c -= 3;
    }
 
  return 0;
}
