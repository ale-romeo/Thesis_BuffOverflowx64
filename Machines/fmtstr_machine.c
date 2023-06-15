#include <stdio.h>

char data[] = "hackhere";

int main(int argc, char **argv){
    printf("I dati nascosti si trovano all'indirizzo %p\n", &data);

    char buffer[32];
    gets(buffer);
    printf(buffer);
    printf("\n");
}