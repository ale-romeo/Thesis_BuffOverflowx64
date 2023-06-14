#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    char buffer[256];

    printf("Benvenuto in questa macchina! Inserisci un messaggio:\n");
    gets(buffer);
    printf("Ricevuto! Alla prossima.\n");
}