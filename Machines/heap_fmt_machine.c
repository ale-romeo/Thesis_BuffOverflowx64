#include <stdio.h>
#include <stdlib.h>

char date_path[] = "/usr/bin/date";

int main(int argc, char **argv){
    char *s;
    s = (char *)malloc(sizeof(char *)); //La variabile s non si trova nello stack, ma e' allocata dinamicamente nell'heap

    puts("Ciao! Puoi dirmi la data di oggi?");
    fgets(s, 34, stdin);
    printf(s); //ATTENZIONE VULNERABILITA'

    puts("????");
    puts("A quanto pare ti sbagli. La data di oggi e': ");
    system(date_path);
    return 0;
}