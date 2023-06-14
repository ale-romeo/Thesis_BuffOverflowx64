#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void vuln_function(){
    char buffer[256];
    gets(buffer);
    printf("Codice: %s !!\n", buffer);
}

int main(int argc, char *argv[]){
    printf("Benvenuto in questa macchina! Potresti spawnare una shell?\n> ");
    vuln_function();

    return 0;
}