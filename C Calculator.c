#include <stdio.h>

int main() {
    char op;
    double first, second;
    int valid = 1;
    char a[1];

    printf("Choose one of the operations: (+, -, *, /)\n");
    scanf(" %c", &op);

    if (op == '+' || op == '-' || op == '*' || op == '/') {
        char op2;
        scanf(" %c", &op2);
        if (op2 == '+' || op2 == '-' || op2 == '*' || op2 == '/' || op2 == '%') {
            printf("Invalid input - consecutive operators\n");
            valid = 0;
        }
        // Check if op2 is a valid operator
        else if (op2 != '+' && op2 != '-' && op2 != '*' && op2 != '/' && op2 != '%') {
            printf("Invalid input\n");
            valid = 0;
        }
    } else {
        printf("Invalid input\n");
        valid = 0;
    }

    if (valid) {
        printf("Enter 2 numbers to operate\n");
        scanf("%lf %lf", &first, &second);
        switch (op) {
            case '+':
                printf("%.1lf + %.1lf = %.1lf", first, second, first + second);
                break;
            case '-':
                printf("%.1lf - %.1lf = %.1lf", first, second, first - second);
                break;
            case '*':
                printf("%.1lf * %.1lf = %.1lf", first, second, first * second);
                break;
            case '/':
                if (second != 0) {
                    printf("%.1lf / %.1lf = %.1lf", first, second, first / second);
                } else {
                    printf("Error! Division by zero.");
                }
                break;
            default:
                printf("Invalid input");
        }
    }

    return 0;
}
