#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

#ifndef s
#define s 10
#endif

// ============================================================
//  СТЕК ДЛЯ ВЫЧИСЛЕНИЙ (массив)
// ============================================================

double *bp = NULL;
int sp = 0;          // указатель вершины стека
int capacity = 0;

void init_stack(int initial_capacity) {
    capacity = initial_capacity;
    bp = (double*)malloc(capacity * sizeof(double));
    if (bp == NULL) {
        printf("Ошибка памяти при инициализации стека!\n");
        exit(1);
    }
}

void resize_stack() {
    int new_capacity = capacity * 2;
    double *new_bp = (double*)realloc(bp, new_capacity * sizeof(double));
    
    if (new_bp == NULL) {
        printf("Ошибка: не удалось расширить стек!\n");
        return;
    }
    bp = new_bp;
    capacity = new_capacity;
    printf("Стек расширен: %d -> %d\n", capacity / 2, capacity);
}

void check_stack() {
    if (sp >= capacity) {
        resize_stack();
    }
}

void push(double value) {
    check_stack();
    bp[sp++] = value;
}

double pop() {
    if (sp <= 0) {
        printf("Ошибка: стек пуст!\n");
        return 0;
    }
    return bp[--sp];
}

double peek() {
    if (sp <= 0) {
        printf("Ошибка: стек пуст!\n");
        return 0;
    }
    return bp[sp - 1];
}

void clear_stack() {
    sp = 0;
    printf("Стек очищен\n");
}

// ============================================================
//  ОТОБРАЖЕНИЕ СТЕКА
// ============================================================

void print_stack() {
    printf("  Стек: [");
    for (int i = 0; i < sp; i++) {
        if (bp[i] == (int)bp[i])
            printf("%s%d", i == 0 ? "" : ", ", (int)bp[i]);
        else
            printf("%s%.4f", i == 0 ? "" : ", ", bp[i]);
    }
    printf("]\n");
}

// ============================================================
//  СТРУКТУРА ДЛЯ ОПЕРАТОРОВ (приоритеты и ассоциативность)
// ============================================================

typedef struct {
    char op;
    int priority;     // приоритет (выше = выполняется раньше)
    int rightAssoc;   // правоассоциативный (1 для ^, 0 для остальных)
} Operator;

Operator operators[] = {
    {'+', 1, 0},
    {'-', 1, 0},
    {'*', 2, 0},
    {'/', 2, 0},
    {'^', 3, 1},     // возведение в степень: правоассоциативное
    {'s', 4, 0},     // sin
    {'c', 4, 0},     // cos
    {'t', 4, 0},     // tan
    {'q', 4, 0},     // sqrt
    {'l', 4, 0},     // ln
    {'g', 4, 0}      // log
};

int get_priority(char op) {
    for (int i = 0; i < sizeof(operators) / sizeof(Operator); i++) {
        if (operators[i].op == op)
            return operators[i].priority;
    }
    return 0;
}

int is_right_assoc(char op) {
    for (int i = 0; i < sizeof(operators) / sizeof(Operator); i++) {
        if (operators[i].op == op)
            return operators[i].rightAssoc;
    }
    return 0;
}

int is_operator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/' || c == '^');
}

int is_function(char c) {
    return (c == 's' || c == 'c' || c == 't' || c == 'q' || c == 'l' || c == 'g');
}

// ============================================================
//  ПРИМЕНЕНИЕ ОПЕРАЦИЙ
// ============================================================

double apply_operator(char op, double a, double b) {
    switch (op) {
        case '+': 
            printf("    %.4f + %.4f = %.4f\n", a, b, a + b);
            return a + b;
        case '-': 
            printf("    %.4f - %.4f = %.4f\n", a, b, a - b);
            return a - b;
        case '*': 
            printf("    %.4f * %.4f = %.4f\n", a, b, a * b);
            return a * b;
        case '/': 
            if (b == 0) {
                printf("Ошибка: деление на ноль!\n");
                return 0;
            }
            printf("    %.4f / %.4f = %.4f\n", a, b, a / b);
            return a / b;
        case '^': 
            printf("    %.4f ^ %.4f = %.4f\n", a, b, pow(a, b));
            return pow(a, b);
        default: return 0;
    }
}

double apply_function(char func, double a) {
    switch (func) {
        case 's':  // sin
            printf("    sin(%.4f) = %.4f\n", a, sin(a));
            return sin(a);
        case 'c':  // cos
            printf("    cos(%.4f) = %.4f\n", a, cos(a));
            return cos(a);
        case 't':  // tan
            printf("    tan(%.4f) = %.4f\n", a, tan(a));
            return tan(a);
        case 'q':  // sqrt
            if (a < 0) {
                printf("Ошибка: квадратный корень из отрицательного числа!\n");
                return 0;
            }
            printf("    sqrt(%.4f) = %.4f\n", a, sqrt(a));
            return sqrt(a);
        case 'l':  // ln (натуральный логарифм)
            if (a <= 0) {
                printf("Ошибка: логарифм от неположительного числа!\n");
                return 0;
            }
            printf("    ln(%.4f) = %.4f\n", a, log(a));
            return log(a);
        case 'g':  // log10
            if (a <= 0) {
                printf("Ошибка: логарифм от неположительного числа!\n");
                return 0;
            }
            printf("    log10(%.4f) = %.4f\n", a, log10(a));
            return log10(a);
        default: return 0;
    }
}

// ============================================================
//  АЛГОРИТМ СОРТИРОВОЧНОЙ СТАНЦИИ (обычная запись -> RPN)
// ============================================================

char* infix_to_rpn(const char* expr) {
    static char output[1024];
    char ops[256];           // стек операторов
    int op_sp = 0;           // вершина стека операторов
    int out_pos = 0;
    int i = 0;
    int len = strlen(expr);
    
    while (i < len) {
        char c = expr[i];
        
        // Пропускаем пробелы
        if (isspace(c)) {
            i++;
            continue;
        }
        
        // Числа (целые и десятичные)
        if (isdigit(c) || c == '.') {
            char num[64];
            int num_pos = 0;
            
            // Собираем число
            while (i < len && (isdigit(expr[i]) || expr[i] == '.')) {
                num[num_pos++] = expr[i++];
            }
            num[num_pos] = '\0';
            
            // Добавляем в вывод
            out_pos += sprintf(output + out_pos, "%s ", num);
            continue;
        }
        
        // Переменная/константа pi
        if (c == 'p' && i + 1 < len && expr[i+1] == 'i') {
            out_pos += sprintf(output + out_pos, "3.14159265359 ");
            i += 2;
            continue;
        }
        
        // Константа e
        if (c == 'e' && (i + 1 >= len || !isalnum(expr[i+1]))) {
            out_pos += sprintf(output + out_pos, "2.71828182846 ");
            i += 1;
            continue;
        }
        
        // Унарный минус
        if (c == '-' && (i == 0 || expr[i-1] == '(' || is_operator(expr[i-1]))) {
            out_pos += sprintf(output + out_pos, "0 ");
            // Продолжаем обработку минуса как бинарного оператора
        }
        
        // Функции
        if (c == 's' && i + 2 < len) {
            if (strncmp(expr + i, "sin", 3) == 0) {
                ops[op_sp++] = 's';
                i += 3;
                continue;
            } else if (strncmp(expr + i, "sqrt", 4) == 0) {
                ops[op_sp++] = 'q';
                i += 4;
                continue;
            }
        }
        
        if (c == 'c' && i + 2 < len && strncmp(expr + i, "cos", 3) == 0) {
            ops[op_sp++] = 'c';
            i += 3;
            continue;
        }
        
        if (c == 't' && i + 2 < len && strncmp(expr + i, "tan", 3) == 0) {
            ops[op_sp++] = 't';
            i += 3;
            continue;
        }
        
        if (c == 'l' && i + 1 < len) {
            if (expr[i+1] == 'n') {
                ops[op_sp++] = 'l';
                i += 2;
                continue;
            } else if (strncmp(expr + i, "log", 3) == 0) {
                ops[op_sp++] = 'g';
                i += 3;
                continue;
            }
        }
        
        // Левая скобка
        if (c == '(') {
            ops[op_sp++] = '(';
            i++;
            continue;
        }
        
        // Правая скобка
        if (c == ')') {
            while (op_sp > 0 && ops[op_sp - 1] != '(') {
                output[out_pos++] = ops[--op_sp];
                output[out_pos++] = ' ';
            }
            if (op_sp > 0) op_sp--; // убираем '('
            i++;
            continue;
        }
        
        // Знак равенства (вычисление)
        if (c == '=') {
            i++;
            continue;
        }
        
        // Операторы
        if (is_operator(c)) {
            int curr_priority = get_priority(c);
            
            while (op_sp > 0 && ops[op_sp - 1] != '(') {
                char top_op = ops[op_sp - 1];
                int top_priority = get_priority(top_op);
                
                if ((!is_right_assoc(c) && curr_priority <= top_priority) ||
                    (is_right_assoc(c) && curr_priority < top_priority)) {
                    output[out_pos++] = ops[--op_sp];
                    output[out_pos++] = ' ';
                } else {
                    break;
                }
            }
            ops[op_sp++] = c;
            i++;
            continue;
        }
        
        // Неизвестный символ
        printf("Неизвестный символ: %c\n", c);
        return NULL;
    }
    
    // Выгружаем оставшиеся операторы
    while (op_sp > 0) {
        char op = ops[--op_sp];
        if (op == '(') {
            printf("Ошибка: несогласованные скобки!\n");
            return NULL;
        }
        output[out_pos++] = op;
        output[out_pos++] = ' ';
    }
    
    output[out_pos] = '\0';
    return output;
}

// ============================================================
//  ВЫЧИСЛЕНИЕ RPN
// ============================================================

double evaluate_rpn(const char* rpn) {
    sp = 0;
    char token[64];
    int token_pos = 0;
    
    for (int i = 0; rpn[i] != '\0'; i++) {
        char c = rpn[i];
        
        if (c == ' ') {
            if (token_pos > 0) {
                token[token_pos] = '\0';
                token_pos = 0;
                
                // Число
                if (isdigit(token[0]) || token[0] == '.') {
                    push(atof(token));
                    printf("  + push %.4f\n", atof(token));
                }
                // Оператор или функция
                else if (strlen(token) == 1) {
                    char op = token[0];
                    
                    if (is_operator(op)) {
                        double b = pop();
                        double a = pop();
                        double result = apply_operator(op, a, b);
                        push(result);
                    } else if (is_function(op)) {
                        double a = pop();
                        double result = apply_function(op, a);
                        push(result);
                    }
                }
                print_stack();
            }
        } else {
            token[token_pos++] = c;
            if (token_pos >= 64) {
                printf("Ошибка: слишком длинный токен!\n");
                return 0;
            }
        }
    }
    
    if (sp >= 1) {
        return pop();
    }
    
    printf("Ошибка: некорректное выражение!\n");
    return 0;
}

// ============================================================
//  ФУНКЦИЯ ДЛЯ ПОСТРОЧНОГО ВВОДА 
// ============================================================

void process_line(const char* line) {
    char buffer[1024];
    strcpy(buffer, line);
    
    // Ищем знак '='
    char* eq_pos = strchr(buffer, '=');
    
    if (eq_pos != NULL) {
        // Разделяем выражение до '='
        *eq_pos = '\0';
        
        // Удаляем пробелы в конце
        int len = strlen(buffer);
        while (len > 0 && isspace(buffer[len-1])) {
            buffer[--len] = '\0';
        }
        
        if (strlen(buffer) > 0) {
            printf("\nВычисление: %s\n", buffer);
            
            // Преобразование в RPN
            char* rpn = infix_to_rpn(buffer);
            if (rpn == NULL) {
                printf("Ошибка в выражении!\n");
                return;
            }
            
            printf("\nRPN: %s\n", rpn);
            
            // Вычисление
            double result = evaluate_rpn(rpn);
            
            printf("\n========================================\n");
            printf("РЕЗУЛЬТАТ: %.6f\n", result);
            printf("========================================\n");
            print_stack();
        }
    } else {
        // Обычный RPN-режим (без знака '=')
        char* rpn = infix_to_rpn(buffer);
        if (rpn == NULL) {
            printf("Ошибка в выражении!\n");
            return;
        }
        
        printf("\nRPN: %s\n", rpn);
        double result = evaluate_rpn(rpn);
        
        printf("\nРЕЗУЛЬТАТ: %.6f\n", result);
        print_stack();
    }
}

// ============================================================
//  ОСНОВНАЯ ПРОГРАММА
// ============================================================

int main() {
    char input[1024];
    init_stack(s);
    
    printf("============================================\n");
    printf("    КАЛЬКУЛЯТОР С ПОДДЕРЖКОЙ СКОБОК\n");
    printf("============================================\n");
    printf("Функции: +, -, *, /, ^ (степень), sin, cos, tan\n");
    printf("         sqrt, ln, log, pi, e, скобки ()\n");
    printf("\nСпособы ввода:\n");
    printf("  1. 2 + 3 * 4 =     → автоматическое вычисление\n");
    printf("  2. 2 3 4 * +       → прямой RPN (без '=')\n");
    printf("  3. (2+3)*4 =       → со скобками и '='\n");
    printf("\nКоманды:\n");
    printf("  clear, c           → очистить стек\n");
    printf("  stack, s           → показать стек\n");
    printf("  q, quit            → выход\n");
    printf("============================================\n\n");
    
    while (1) {
        printf("\n> ");
        fflush(stdout);
        
        if (fgets(input, sizeof(input), stdin) == NULL) {
            break;
        }
        
        // Удаляем символ новой строки
        size_t len = strlen(input);
        if (len > 0 && input[len - 1] == '\n') {
            input[len - 1] = '\0';
        }
        
        // Проверка на выход
        if (strcmp(input, "q") == 0 || strcmp(input, "quit") == 0) {
            printf("До свидания!\n");
            break;
        }
        
        if (strlen(input) == 0) {
            continue;
        }
        
        // Команда очистки стека
        if (strcmp(input, "clear") == 0 || strcmp(input, "c") == 0) {
            clear_stack();
            continue;
        }
        
        // Команда показа стека
        if (strcmp(input, "stack") == 0 || strcmp(input, "s") == 0) {
            print_stack();
            continue;
        }
        
        // Обработка выражения
        process_line(input);
    }
    
    free(bp);
    return 0;
}