#include <stdio.h>
#include <stdlib.h>

char date_path[] = "/bin/date";

int main(int argc, char **argv){
    char s[264]; //La variabile s e' salvata nello stack

    puts("Ciao! Puoi dirmi la data di oggi?");
    fgets(s, 256, stdin);
    printf(s); //ATTENZIONE VULNERABILITA '

    puts("????");
    puts("A quanto pare ti sbagli. La data di oggi e ': ");
    system(date_path);
    
    return 0;
}