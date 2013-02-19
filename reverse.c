#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void reverse(char* s);
 
int main(int argc, char **argv)
{
  	char* test = "ILOVECODING";
    	reverse(test);
        return 0;
}

void reverse(char* input)
{
  int length = strlen(input);
	char *end = input+length;
	char * start = input;
    
	while(end > start){
		char t = *end;
		*end = *start;
		*start = t; 	
		end--;
		start++;
	}

  input[length] = '\0'
}
