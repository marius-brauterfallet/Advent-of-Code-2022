#include <stdio.h>

int check_last(int last[]);
void print_last(int last[]);

int main() {
    FILE *fp;
    int rc, i = 0, last[14] = {0};

    fp = fopen("input", "r");

    while ((rc = fgetc(fp)) != EOF) {
        last[i++ % 14] = rc;

        if (i >= 14 && check_last(last)) {
            printf("%d\n", i);
            break;
        }
    }

    fclose(fp);
}

int check_last(int last[]) {
    int i, j;

    for (i = 0; i < 13; i++) {
        for (j = i + 1; j < 14; j++) {
            if (last[i] == last[j]) {
                return 0;
            }
        }
    }

    return 1;
}
