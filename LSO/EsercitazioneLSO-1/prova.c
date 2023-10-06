#include <stdio.h>
#include <stdlib.h>

void main(){
    FILE *fp=fopen("righenum", "w");

    for(int i=1; i<51; i++){
        fprintf(fp, "riga %d\n", i);
    }
    fclose(fp);
    return;
}