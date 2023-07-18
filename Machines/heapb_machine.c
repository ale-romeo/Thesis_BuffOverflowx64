#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef int(*fp) (const char *);

fp *toInt(){
	fp *ti;
	ti = malloc(sizeof(*ti));
	*ti = atoi;
	return ti;
}

int main(int argc, char **argv){
	unsigned int *array, length, size, i = 0;

	puts("Ciao! Questa e' un semplice macchina che alloca array di unsigned int. (niente shell)");
	puts("************************************* \
	***********************************************");
	length = atoi(argv[1]);
	printf("Lunghezza array: %d\n", length);

	size = sizeof(unsigned int) * length;
	printf("Dimensione allocata: %d\n", size);

	array = malloc(size);

	fp *nt = toInt();

	//printf("Array nell'heap: %p\nPuntatore della funzione: %p\n", array, nt); /*debug purpose*/
	puts("Inserisci valori: ");
	while(i < length){
		printf("%d", i+1);
		puts("> ");
		scanf("%ld",&array[i]);
		if(array[i] == 1)
			break;
		i++;
	}

	(*nt)(argv[2]);

	return 0;
}