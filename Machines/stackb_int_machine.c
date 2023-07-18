#include <stdio.h>
#include <stdlib.h>

char *flag = "CHI FA DA SE', FA PER TRE!";

int main()
{
    int con;
    con = 0;
    int account_balance = 1100;
    while (con == 0)
    {

        printf("Ciao! Benvenuto in questo negozio di consigli.\n");
        printf("Purtroppo per te non ci sono vulnerabilita' qui.\n");

        printf("\n[1] Verifica il tuo bilancio\n");
        printf("\n[2] Compra qualcosa\n");
        printf("\n[3] Esci\n");
        int menu;
        printf("\n Scegli cosa fare:\n");
        fflush(stdin);
        scanf("%d", &menu);
        if (menu == 1)
        {
            printf("\n\n\n Bilancio: %d \n\n\n", account_balance);
        }
        else if (menu == 2)
        {
            printf("Azioni possibili\n");
            printf("[1] Consigli!\n");
            printf("[2] SEGRETO\n");
            int auction_choice;
            fflush(stdin);
            scanf("%d", &auction_choice);
            if (auction_choice == 1)
            {
                printf("I consigli costano 1000 dollari ciascuno, quanti ne desideri?\n");

                int number_flags = 0;
                fflush(stdin);
                scanf("%d", &number_flags);
                if (number_flags > 0)
                {
                    int total_cost = 0;
                    total_cost = 1000 * number_flags;
                    printf("\nIl totale e': %d\n", total_cost);
                    if (total_cost <= account_balance)
                    {
                        account_balance = account_balance - total_cost;
                        printf("\nIl tuo bilancio: %d\n\n", account_balance);
                    }
                    else
                    {
                        printf("Non hai abbastanza fondi.\n");
                    }
                }
            }
            else if (auction_choice == 2)
            {
                printf("Il mio segreto costa 100000 dollari, ho solo un segreto.\n");
                printf("Inserisci 1 per acquistare.\n");
                int bid = 0;
                fflush(stdin);
                scanf("%d", &bid);

                if (bid == 1)
                {

                    if (account_balance > 100000)
                    {
                        printf("Ecco il mio segreto: %s\n", flag);
                    }

                    else
                    {
                        printf("\nNon hai abbastanza fondi.\n\n\n");
                    }
                }
            }
        }
        else
        {
            con = 1;
        }
    }
    return 0;
}