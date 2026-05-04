#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

#ifndef s
#define s 5
#endif

// Стек для вычислений RPN
double *bp = NULL;
int sp = 0;
int capacity = 0;

// Стек для операторов при переводе в RPN
char *op_stack = NULL;
int op_sp = 0;
int op_capacity = 0;

// Функции для стека вычислений
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

// Функции для стека операторов
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

// Приоритет операторов
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

// Проверка, является ли символ оператором
int is_operator(char c)
{
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '^';
}

// Преобразование инфиксного выражения в постфиксное (RPN)
void infix_to_rpn(const char *infix, char *rpn)
{
    int i, j = 0;
    char c;
    int len = strlen(infix);
    
    init_op_stack(s);
    
    for (i = 0; i < len; i++)
    {
        c = infix[i];
        
        // Пропускаем пробелы
        if (isspace(c))
            continue;
        
        // Если число или десятичная точка
        if (isdigit(c) || c == '.')
        {
            while (i < len && (isdigit(infix[i]) || infix[i] == '.'))
            {
                rpn[j++] = infix[i++];
            }
            rpn[j++] = ' ';
            i--; // Компенсируем лишнее увеличение i
        }
        // Если открывающая скобка
        else if (c == '(')
        {
            push_op(c);
        }
        // Если закрывающая скобка
        else if (c == ')')
        {
            while (!is_empty_op() && top_op() != '(')
            {
                rpn[j++] = pop_op();
                rpn[j++] = ' ';
            }
            if (!is_empty_op() && top_op() == '(')
                pop_op(); // Удаляем '('
        }
        // Если оператор
        else if (is_operator(c))
        {
            while (!is_empty_op() && top_op() != '(' &&
                   precedence(top_op()) >= precedence(c))
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
    
    // Выгружаем оставшиеся операторы
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

// Вычисление RPN выражения
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
                // Проверяем, является ли токен числом
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

// Интерактивный калькулятор RPN (старый режим)
void rpn_calculator()
{
    char c;
    
    while ((c = getc(stdin)) != EOF)
    {
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
            return;
        }
    }
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
    scanf("%d", &choice);
    getchar(); // Убираем символ новой строки
    
    if (choice == 1)
    {
        printf("Enter infix expression (e.g., 3+4*2/(1-5)^2): ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0'; // Удаляем символ новой строки
        
        printf("\nInfix: %s\n", input);
        
        // Конвертируем в RPN
        infix_to_rpn(input, rpn);
        printf("RPN: %s\n", rpn);
        
        // Инициализируем стек вычислений
        init_stack(s);
        
        // Вычисляем результат
        result = evaluate_rpn(rpn);
        
        // Выводим результат
        if (result == (int)result)
            printf("Result = %d\n", (int)result);
        else
            printf("Result = %.4f\n", result);
        
        free(bp);
    }
    else if (choice == 2)
    {
        printf("RPN Calculator Mode\n");
        printf("Enter numbers and operators (e.g., 5 3 + =)\n");
        printf("Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) to exit\n\n");
        
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