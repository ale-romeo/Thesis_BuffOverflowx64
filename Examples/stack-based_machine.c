#include <signal.h>
#include <stdio.h>
#include <string.h>

int main(){
    char password[20];
    char input[20];

    strncpy(password, "secretpass", 20);
    printf("Inserisci password:\t");
    gets(input);

    if(strncmp(input, password, 20) == 0){
        printf("Password esatta!\n");
    }else{
        printf("Password sbagliata.\n");
    }
    raise(SIGINT);
    printf("Password inserita: %s\n", input);
    printf("Password esatta: %s\n", password);
    return 0;
}