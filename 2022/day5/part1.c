#include <stdio.h>
#include <ctype.h>

typedef struct node {
    char c;
    struct node* next;
} node;

node* make_node(char c);
void free_stacks(node stacks[], int size);
void free_nodes(node* n) {
void add_node(node stacks[], int i, char c);
void print_res(node stacks[], int size) {

int main() {
    FILE *fp;
    size_t n = 0;
    ssize_t rc;
    char *s = NULL;

    int i;
    node stacks[9] = {0};

    fp = fopen("input", "r");

    while (rc = getline(&s, &n, fp) != -1) {
        if (isdigit(s[1])) {
            rc = getline(&s, &n, fp);
            break;
        }

        i = 1;

        while (i < rc) {
            if (isalpha(s[i])) {
                add_node(stacks, i / 4, s[i])
            }

            i += 4;
        }
    }

    printf("%s", s);
    print_res(stacks, 9);




    fclose(fp);
}



node* make_node(char c) {
    node* n = malloc(sizeof(node));
    n->c = c;
    n->next = NULL;
    return n;
}


void free_stacks(node stacks[], int size) {
    int i;

    for (i = 0; i < size; i++) {
        free_nodes(stacks[i]);
    }
}


void free_nodes(node* n) {
    if (n) {
        free_nodes(n->next);
        free(n);
    }
}


void add_node(node stacks[], int i, char c) {
    node* n = malloc(sizeof(node));

    n->c = c;
    n->next = stacks[i];
    stacks[i] = n;
}


void print_res(node stacks[], int size) {
    int i, j = 0;
    char buf[10]:
    for (i = 0; i < size; i++) {
        if (stacks[i]) {
            buf[j] = stacks[i]->c;
            j++;
        }
    }

    buf[j] = '\0';
    printf("%s\n", buf);
}
