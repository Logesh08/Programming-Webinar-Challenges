// Longest Mirror End String

// The program must accept a string S and print the longest mirror end substring. The mirror end substring is present in the beginning of the string and also at the end of the string in the reverse order. If there is no such mirror end string, then the program must print 0 as the output.

// Boundary Condition(s):
// 1 <= Length of S <= 100

// Input Format:
// The first line contains S.

// Output Format:
// The first line contains a string value.

// Example Input/Output 1:
// Input:
// abefba

// Output:
// ab

// Example Input/Output 2:
// Input:
// abacus

// Output:
// 0

// Example Input/Output 3:
// Input:
// level

// Output:
// level


#include<stdio.h>
#include<stdlib.h>

int main()
{
    char str[101];
    char prnt[101]={'\0'};
    scanf("%s",str);
    int len=strlen(str);
    int left=0,right=len-1;
    while(str[left]==str[right] && right>=0){
        left++; right--;
    }
    if(left==0){
        printf("0");
    }else{
        for(int index=0;index<left;index++){
            printf("%c",str[index]);
        }
    }
    return 0;
}
