#include <stdio.h>
#include <string.h>

int main(){

    char password[20];
    char input[20];

    /*Assegnamento della password tramite strncpy()*/
    strncpy(password, "sssssssssssssssss", 20);
    printf("Inserisci password:\t");
    gets(input);

    /*Confronto tra la password inserita e quella salvata nello stack.*/
    if(strncmp(input, password, 20) == 0){
        printf("Password esatta!\n");
    }else{
        printf("Password sbagliata.\n");
    }
    /*Funzione puts() utilizzata per creare un breakpoint da gdb.*/
    puts("Break.");

    /*Verifica dello stack: stampa della password e dell'input ricevuto.*/
    printf("Password inserita: %s\n", input);
    printf("Password esatta: %s\n", password);
    return 0;
}