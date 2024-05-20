#include <stdio.h>

int main() {
    int sum, val;
    sum = 0;
    for(int i=0; i<10; i++){
        scanf("%d", &val);
        sum +=val;
    }
    printf("%d",sum);
    return 0;
}