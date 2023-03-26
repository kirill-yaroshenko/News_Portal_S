#include <stdio.h>

int main() {

    int x = 3, y = -4;
    char ch_eq = '=';
    char ch_plus = '+'; 
    char ch_minus = '-'; 
    char ch_div = '/'; 
    char ch_mul = '*';
    double res = -0.75;

    printf("%c %d %d \n%d",ch_minus, x, y, x-y);
    printf("%d %c %d %c %d\n", x, ch_plus, y, ch_eq, x+y);
    printf("%c %d %d \n%d", x, ch_minus, y, x-y);
    printf("Result of %c for %d %d = %5.2f", ch_div, x, y, res);
    printf("%c %d %d \n%d",ch_minus, x, y, x-y);

    return 0;
}
