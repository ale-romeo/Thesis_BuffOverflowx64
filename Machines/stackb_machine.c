#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int vuln() {
    char buf[80];
    int r;
    r = read(0, buf, 400);
    printf("\nRead %d bytes. buf is %s\n", r, buf);
    puts("No shell for you :(");
    return 0;
}

int main(int argc, char *argv[]) {
    char *ptr;
    ptr = getenv("PWN");
    printf("PWN: %p\n", ptr);
    printf("Try to exec /bin/sh");
    vuln();
    return 0;
}