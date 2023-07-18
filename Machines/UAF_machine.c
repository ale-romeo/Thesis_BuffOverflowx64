#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <stdio.h>

struct auth{
    char name[32];
    int auth;
} auth;

struct auth *authVar;
char *service;

int main(int argc, char **argv){
    char line[128];
    char *dump;
    printf("Ciao! Benvenuto nel servizio di autenticazione piu' sicuro in Italia.\n\n");

    while (1){
        printf("************************* \
        **************************\n\n");
        printf("[ auth = %p, service = %p ]\n", authVar, service); /*debug purpose*/
        printf("Comandi disponbili:\n) auth _nome_\n) reset\n) service\n) login\n) exit\n");
        puts("> ");

        if (fgets(line, sizeof(line), stdin) == NULL) break;

        if (strncmp(line, "auth ", 5) == 0){
            authVar = malloc(sizeof(auth));
            memset(authVar, 0, sizeof(auth));
            if (strlen(line + 5) < 31){
                strcpy(authVar->name, line + 5);
            }
        }
        if (strncmp(line, "reset", 5) == 0){
            free(authVar);
        }
        if (strncmp(line, "service", 6) == 0){
            service = strdup(line + 7);
        }
        if (strncmp(line, "login", 5) == 0){
            if (authVar->auth){
                printf("Ci sei riuscito davvero stavolta. Come hai fatto!?\n");
                printf("Ecco la tua shell: \n");
                system("/bin/sh");
            }else{
                printf("Ecco la tua shell: \n");
                scanf("%s", dump);
                printf("Ci hai creduto davvero? Non e' cosi' semplice!\n");
            }
        }
        if (strncmp(line, "exit", 4) == 0){
            printf("A presto!\n");
            return 0;
        }
    }
}