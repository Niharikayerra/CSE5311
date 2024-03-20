#include<stdio.h>
#include<stdbool.h>
#define MAX_SIZE 100
typedef struct
{
    int data[MAX_SIZE];
    int top;
}Stack;
void init(Stack *stack)
{
    stack->top = -1;
}
bool isempty(Stack *stack)
{
    return stack->top == -1;
}
bool isfull(Stack *stack)
{
    return stack->top == MAX_SIZE-1;
}
void push(Stack *stack, int value)
{
    if(isfull(stack))
    {
        printf("stack overflow\n");
        return;
    }
    stack->top++;
    stack->data[stack->top] = value;
}
int pop(Stack *stack)
{
    if(isempty(stack))
    {
        printf("stck underflow\n");
        return -1;
    }
    int value = stack->data[stack->top];
    stack->top--;
    return value;
}
int peek(Stack *stack)
{
    if(isempty(stack))
    {
        printf("stack is empty\n");
        return -1;
    }
    return stack->data[stack->top];
}
int main()
{
    Stack stack;
    init(&stack);
    push(&stack,8);
    push(&stack,9);
    push(&stack,4);
printf("Is the stack empty? %s\n", isempty(&stack) ? "Yes" : "No");
printf("Popped Element : %d\n", pop(&stack));
printf("Popped Element : %d\n", pop(&stack));
printf("Popped Element : %d\n", pop(&stack));
printf("Is the stack empty? %s\n", isempty(&stack) ? "Yes" : "No");
return 0;
}