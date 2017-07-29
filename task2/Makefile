CC=c++
M_CFLAGS=-std=c++0x -g -D__linux__
M_INCS=-I.

OBJS= main.o
MyApp=test

%.o:%.cpp
	$(CC) -c $(M_CFLAGS) $(M_INCS) $< -o $@
%.o:%.C
	$(CC) -c $(M_CFLAGS) $(M_INCS) $< -o $@
%.o:%.c
	$(CC) -c $(M_CFLAGS) $(M_INCS) $< -o $@

all:$(MyApp)
$(MyApp) : $(OBJS)
	$(CC) $(OBJS) -o $(MyApp)

clean:
	rm -f $(OBJS)
	rm -f $(MyApp)
