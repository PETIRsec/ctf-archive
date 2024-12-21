#include <stdio.h>
#include <fcntl.h>
#include <stdbool.h>
#include <stdint.h>
#include <string.h>

extern void _(void);

int bread = 5, drink = 3;
char mykey[104];

void wutthis(){
    char buf[104] = {};
    FILE* fp = fopen("flag.txt", "r");
    fread(buf, 1, 100, fp);
    fclose(fp);
    printf("Gratz! Take your P R I Z E:\n");
    printf("%s\n", buf);
}

__asm__(
    ".globl _\n\t"
    "_:\n\t"
    "pop %rdi\n\t"
    "pop %r8\n\t"
    "pop %r9\n\t"
    "ret\n\t"
    "pop %rsi\n\t"
    "pop %rdx\n\t"
    "pop %rbx\n\t"
    "ret\n\t"
);

void buyFood(){
    char buf[100];
    puts("I see that you're trying to buy more food, what would you like to buy?");
    printf("> ");
    fgets(buf, 520, stdin);
    puts("got it, let me look in the inventory");
}

void init()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void menu()
{
    puts("Welcome to IFEST2024!");
    puts("You got sanity check!");
    puts("1. Drink Water");
    puts("2. Eat Bread");
    puts("3. Buy more food");
    puts("-1. Exit");
}

void drinkWater(){
    if(drink < 0){
        puts("You are out of water!");
        return;
    }
    puts("You are drinking water...");
    puts("Glub Glub Glub...");
    drink--;
}

void eatBread(){
    if(bread < 0){
        puts("You are out of bread!");
        return;
    }
    puts("You are eating bread...");
    puts("Nom nom nom...");
    bread--;
}

int main(){
    init();
    int8_t x, isRunning = 1;
    do{
        menu();
        printf("> ");
        scanf("%hhd", &x);getchar();
        switch(x){
            case 1:
                drinkWater();
                break;
            case 2:
                eatBread();
                break;
            case 3:
                buyFood();
                break;
            case -1:
                isRunning = 0;
                break;
            default:
                puts("Um, maybe pick again?");
                break;
        }
    } while(isRunning);
    puts("Bye Bye!");
    return 0;
}