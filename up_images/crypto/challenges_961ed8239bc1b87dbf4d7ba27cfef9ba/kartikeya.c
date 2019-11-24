#include<stdio.h>
void main()
{
 char a[10];
char s;

 long long int i;

 printf("enter a mobile no. (char) ");

 scanf("%s",a);

 printf("enter a mobile no.(int) ");

 scanf("%lld",&i);

 printf("enter s to print char type mobile no.\n or \n enter any other key for int type mobile no. \n ");

 scanf("%*c%c",&s);

 if(s =='s')
  {
    printf("%s \n",a);
  }

 else
  {
    printf("%lld \n",i);
  }      
}