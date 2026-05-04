#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

#ifndef s
#define s 5
#endif

double *bp = NULL;
int sp = 0;
int capacity = 0;

char *op_stack = NULL;
int op_sp = 0;
int op_capacity = 0;

void init_stack(int initial_capacity)
{
    capacity = initial_capacity;
    bp = (double *)malloc(capacity * sizeof(double));
    if (bp == NULL)
    {
        printf("Memory error!");
        exit(1);
    }
}

void resize_stack()
{
    int new_capacity = capacity * 2;
    double *new_bp = (double *)realloc(bp, new_capacity * sizeof(double));

    if (new_bp == NULL)
    {
        printf("Resize failed!");
        return;
    }
    bp = new_bp;
    capacity = new_capacity;
    printf("Stack resized: %d -> %d\n", capacity / 2, capacity);
}

void check_stack()
{
    if (sp >= capacity)
        resize_stack();
}

void push(double value)
{
    check_stack();
    bp[sp++] = value;
}

double pop()
{
    if (sp > 0)
        return bp[--sp];
    printf("Error: Stack underflow\n");
    return 0;
}

void prbp()
{
    printf("  _____\n");
    for (int i = 0; i < sp; i++)
    {
        if (bp[i] == (int)bp[i])
        {
            printf("%d [%4d]\n", i, (int)bp[i]);
        }
        else
        {
            printf("%d [%4.2f]\n", i, bp[i]);
        }
    }
    printf("  -----\n");
}

void init_op_stack(int initial_capacity)
{
    op_capacity = initial_capacity;
    op_stack = (char *)malloc(op_capacity * sizeof(char));
    if (op_stack == NULL)
    {
        printf("Memory error!");
        exit(1);
    }
}

void resize_op_stack()
{
    int new_capacity = op_capacity * 2;
    char *new_op_stack = (char *)realloc(op_stack, new_capacity * sizeof(char));

    if (new_op_stack == NULL)
    {
        printf("Resize failed!");
        return;
    }
    op_stack = new_op_stack;
    op_capacity = new_capacity;
}

void check_op_stack()
{
    if (op_sp >= op_capacity)
        resize_op_stack();
}

void push_op(char op)
{
    check_op_stack();
    op_stack[op_sp++] = op;
}

char pop_op()
{
    if (op_sp > 0)
        return op_stack[--op_sp];
    return '\0';
}

char top_op()
{
    if (op_sp > 0)
        return op_stack[op_sp - 1];
    return '\0';
}

int is_empty_op()
{
    return op_sp == 0;
}
/*                                              */
int precedence(char op)
{
    switch (op)
    {
    case '+':
    case '-':
        return 1;
    case '*':
    case '/':
        return 2;
    case '^':
        return 3;
    default:
        return 0;
    }
}

int is_operator(char c)
{
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '^';
}


int is_left_associative(char op)
{

    return op != '^';
}

void infix_to_rpn(const char *infix, char *rpn)
{
    int i, j = 0;
    char c;
    int len = strlen(infix);
    
    init_op_stack(s);
    
    for (i = 0; i < len; i++)
    {
        c = infix[i];
        
        
        if (isspace(c))
            continue;
        
    
        if (isdigit(c) || c == '.')
        {
            while (i < len && (isdigit(infix[i]) || infix[i] == '.'))
            {
                rpn[j++] = infix[i++];
            }
            rpn[j++] = ' ';
            i--; 
        }
        
        else if (c == '(')
        {
            push_op(c);
        }
       
        else if (c == ')')
        {
            while (!is_empty_op() && top_op() != '(')
            {
                rpn[j++] = pop_op();
                rpn[j++] = ' ';
            }
            if (!is_empty_op() && top_op() == '(')
                pop_op(); 
        }
        
        else if (is_operator(c))
        {
            
            while (!is_empty_op() && top_op() != '(' &&
                   (precedence(top_op()) > precedence(c) ||
                    (precedence(top_op()) == precedence(c) && is_left_associative(c))))
            {
                rpn[j++] = pop_op();
                rpn[j++] = ' ';
            }
            push_op(c);
        }
        else
        {
            printf("Error: Invalid character '%c' in expression\n", c);
            return;
        }
    }
    
    while (!is_empty_op())
    {
        rpn[j++] = pop_op();
        rpn[j++] = ' ';
    }
    
    rpn[j] = '\0';
    
    free(op_stack);
    op_stack = NULL;
    op_sp = 0;
    op_capacity = 0;
}

double evaluate_rpn(const char *rpn)
{
    int i;
    double a, b;
    char token[100];
    int token_index = 0;
    
    for (i = 0; rpn[i] != '\0'; i++)
    {
        if (rpn[i] == ' ')
        {
            if (token_index > 0)
            {
                token[token_index] = '\0';
            
                if (isdigit(token[0]) || (token[0] == '-' && token_index > 1))
                {
                    push(atof(token));
                }
                else if (is_operator(token[0]) && token_index == 1)
                {
                    b = pop();
                    a = pop();
                    switch (token[0])
                    {
                    case '+':
                        push(a + b);
                        break;
                    case '-':
                        push(a - b);
                        break;
                    case '*':
                        push(a * b);
                        break;
                    case '/':
                        if (b != 0)
                            push(a / b);
                        else
                        {
                            printf("Error: Division by zero\n");
                            return 0;
                        }
                        break;
                    case '^':
                        push(pow(a, b));
                        break;
                    }
                }
                token_index = 0;
            }
        }
        else
        {
            token[token_index++] = rpn[i];
        }
    }
    
    return pop();
}

void rpn_calculator()
{
    char c;
    
    printf("RPN Calculator Mode\n");
    printf("Enter numbers and operators (e.g., 5 3 + =)\n");
    printf("Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) to exit\n\n");
    
    while (1)
    {
        c = getc(stdin);
        
        if (c == EOF)
            break;
            
        switch (c)
        {
        case '0':
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9':
            ungetc(c, stdin);
            check_stack();
            fscanf(stdin, "%lf", &bp[sp]);
            ++sp;
            prbp();
            break;
            
        case '+':
            if (sp < 2)
            {
                printf("Error: Not enough operands for +\n");
                break;
            }
            bp[sp-2] += bp[sp-1];
            --sp;
            prbp();
            break;
            
        case '-':
            if (sp < 2)
            {
                printf("Error: Not enough operands for -\n");
                break;
            }
            bp[sp-2] -= bp[sp-1];
            --sp;
            prbp();
            break;
            
        case '*':
            if (sp < 2)
            {
                printf("Error: Not enough operands for *\n");
                break;
            }
            bp[sp-2] *= bp[sp-1];
            --sp;
            prbp();
            break;
            
        case '/':
            if (sp < 2)
            {
                printf("Error: Not enough operands for /\n");
                break;
            }
            if (bp[sp-1] == 0)
            {
                printf("Error: Division by zero\n");
                break;
            }
            bp[sp-2] /= bp[sp-1];
            --sp;
            prbp();
            break;
            
        case '^':
            if (sp < 2)
            {
                printf("Error: Not enough operands for ^\n");
                break;
            }
            bp[sp-2] = pow(bp[sp-2], bp[sp-1]);
            --sp;
            prbp();
            break;
            
        case '=':
            if (sp < 1)
            {
                printf("Error: Stack is empty\n");
                break;
            }
            if (bp[sp-1] == (int)bp[sp-1])
                printf("Result = %d\n", (int)bp[sp-1]);
            else
                printf("Result = %.4f\n", bp[sp-1]);
            --sp;
            prbp();
            break;
            
        case ' ':
        case '\t':
        case '\n':
            break;
            
        default:
            printf("Input error: unknown character '%c'\n", c);
            while ((c = getc(stdin)) != '\n' && c != EOF);
            break;
        }
    }
}

void clear_input_buffer()
{
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int main()
{
    char input[1000];
    char rpn[1000];
    double result;
    int choice;
    
    printf("=== RPN Calculator & Compiler ===\n");
    printf("1. Convert infix to RPN and evaluate\n");
    printf("2. RPN calculator (direct mode)\n");
    printf("Choose mode (1 or 2): ");
    
    if (scanf("%d", &choice) != 1)
    {
        printf("Invalid input\n");
        return 1;
    }
    clear_input_buffer(); 
    
    if (choice == 1)
    {
        printf("Enter infix expression (e.g., 3+4*2/(1-5)^2^3): ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0'; 
        
        printf("\nInfix: %s\n", input);
        
        
        infix_to_rpn(input, rpn);
        printf("RPN: %s\n", rpn);
        
      
        init_stack(s);
        
        
        result = evaluate_rpn(rpn);
        
        
        if (result == (int)result)
            printf("Result = %d\n", (int)result);
        else
            printf("Result = %.4f\n", result);
        
        free(bp);
    }
    else if (choice == 2)
    {
        init_stack(s);
        rpn_calculator();
        free(bp);
    }
    else
    {
        printf("Invalid choice\n");
        return 1;
    }
    
    printf("\nExit\n");
    return 0;
}