#include <stdio.h>
#include <string.h>
#include <stdbool.h>

char filename[] = "input.txt";
int count = 0;

int count_rows(char*);

int main() {
    printf("the counter\n");
    count = count_rows(filename);
    
    FILE* fp = fopen(filename,"r");
    int data_in[count];
    int i = 0;
    char* thisLine;
    while (fscanf(fp,"%s",&thisLine) == 1) {
        if (strcmp(&thisLine,"\n"));
        data_in[i] = atoi(num);
        i++;
    }
    fclose(fp);

    printf("row count: %d\n",count);
    for(int j = 0; i < sizeof(&data_in); i++) {
        printf("data at line %d: %d\n",i,data_in[i]);
    }

    return 0;
}

/*
* figure out the number of rows in the file before allocating the actual data input
*/
int count_rows(char* input) {
    int cnt = 0;

    FILE* file = fopen(input,"r");
    // figure out exactly how many lines are in the file
    char c;
    for (c = getc(file); c != EOF; c = getc(file)) {
        if (c == '\n') {
            cnt = cnt + 1;
        }
    }
    fclose(file);

    return cnt;
}

