#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct node {
    char c;
    struct node *next, *prev;
} node;

node* make_node(char c);
void add_node_top(node* stacks[], int i, char c);
void free_stacks(node* stacks[], int size);
void free_nodes(node* n);
void print_res(node* stacks[], int size);
void move(node* stacks[], int from, int to, int amount);

int main() {
    FILE *fp;
    size_t n = 0;
    ssize_t rc;
    char *s = NULL;
    int i, amount, from, to;
    node* stacks[9] = {0};

    fp = fopen("input", "r");

    do {
        rc = getline(&s, &n, fp);
        printf("%s", s);

        if (isdigit(s[1])) {
            rc = getline(&s, &n, fp);
            break;
        }

        for (i = 1; i < rc; i += 4) {
            if (isalpha(s[i])) {
                add_node_top(stacks, i / 4, s[i]);
            }
        }
    } while (rc != -1);

    print_res(stacks, 9);

    
    while ((rc = fscanf(fp, "move %d from %d to %d\n", &amount, &from, &to)) != -1) {
        move(stacks, from - 1, to - 1, amount);
    }

    print_res(stacks, 9);


    fclose(fp);
    free_stacks(stacks, 9);
    free(s);
}



node* make_node(char c) {
    node* n = malloc(sizeof(node));
    n->c = c;
    n->next = NULL;
    n->prev = NULL;
    return n;
}


void free_stacks(node* stacks[], int size) {
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


void add_node_top(node* stacks[], int i, char c) {
    node *current, *new = make_node(c);
    
    if (stacks[i]) {
        current = stacks[i];

        while (current->next) {
            current = current->next;
        }

        current->next = new;
        new->prev = current;
        return;
    }

    stacks[i] = new;
}


void print_res(node* stacks[], int size) {
    int i, j = 0;
    char buf[10];

    for (i = 0; i < size; i++) {
        if (stacks[i]) {
            buf[j] = stacks[i]->c;
            j++;
        }
    }

    buf[j] = '\0';
    printf("%s\n", buf);
}


void move(node* stacks[], int from, int to, int amount) {
    int i;
    node *top = stacks[from], *bot = stacks[from];

    for (i = 1; i < amount; i++) {
        bot = bot->next;
    }

    stacks[from] = bot->next;

    if (stacks[from]) {
        stacks[from]->prev = NULL;
    }

    bot->next = stacks[to];
    
    if (stacks[to]) {
        stacks[to]->prev = bot;
    }

    stacks[to] = top;
}