CFLAGS = -g -Wall -Wextra
VFLAGS = --leak-check=full

all: part1 part2

part1: part1.c
	gcc $(CFLAGS) part1.c -o part1

part2: part2.c
	gcc $(CFLAGS) part2.c -o part2

run1: part1
	./part1

run2: part2
	./part2

check1: part1
	valgrind $(VFLAGS) ./part1

check2: part2
	vlagrind $(VFLAGS) ./part2

clean:
	rm -f part1 part2
