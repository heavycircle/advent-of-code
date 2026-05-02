CC		:= gcc
CFLAGS	:= -Wall -Wextra -pedantic -g

main: main.c
	$(CC) $(CFLAGS) -o $@ $^

run: main
	./main

clean:
	rm -f ./main

.PHONY: main run clean
