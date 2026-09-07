#include <stdio.h>
int main() {
    printf("hello world");
    return 0;
}
lets trace every step of the code execution:
1. the program starts executing from the main function:

2. the "#include <stdio.h>" directive is processed by the preprocessor,which includes 
the standard input and output library, allowing the program to use functions like printf.

3. the main function is called, and execution begins at the first statement inside it.

4. the printf function is called with the argument "hello world". this function is responsible for 
printing the specified string to the standard output 

5. the printf function process the string "hello world" and sends it to the output stream, 
which is typically the console or terminal

6. after the printf function completes its execution, control returns to the main function.

7. the return statement is executed, which indicates that the program has completed successfully.

8. the program terminates, and control is returned to the operating system.

/* this is a simple c program i did in day 1*/
#include<stdio.h>
int main()
{
    int a;
    int b;
    int sum;/* variable to store the sum */
    printf("enter the value of a:");/* this is displayed on the screen */
    scanf("%d",&a); /* this reads an integer from the user and stores it in variable a*/
    printf("enter the value of b:");
    scanf("%d",&b);
    sum = a+b;/*this calculates the sum*/
    printf("sum is %d",sum);
    return 0;/* this indicates successful completion of the program */
}


