#include <stdio.h>

int check_last(int last[]);
void print_last(int last[]);

int main() {
    FILE *fp;
    int rc, i = 0, last[4] = {0};

    fp = fopen("input", "r");

    while ((rc = fgetc(fp)) != EOF) {
        last[i++ % 4] = rc;

        if (i >= 4 && check_last(last)) {
            printf("%d\n", i);
            break;
        }
    }

    fclose(fp);
}

int check_last(int last[]) {
    int i, j;

    for (i = 0; i < 3; i++) {
        for (j = i + 1; j < 4; j++) {
            if (last[i] == last[j]) {
                return 0;
            }
        }
    }

    return 1;
}

void print_last(int last[]) {
    printf("[%d, %d, %d, %d]\n", last[0], last[1], last[2], last[3]);
}
