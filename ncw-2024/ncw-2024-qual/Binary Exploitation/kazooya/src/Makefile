# Variables
CC = g++
CFLAGS = -fstack-protector-all
# LDFLAGS = -Wl,-z,relro,-z,now,-dynamic-linker,./lib/ld-linux-x86-64.so.2,-rpath,$ORIGIN/lib
LDFLAGS = -Wl,-z,relro,-z,now
OUTPUT = chall

# Default rule
all: $(OUTPUT)

# Compile rule
$(OUTPUT): chall.o
	$(CC) chall.o -o $(OUTPUT) $(LDFLAGS)
	rm -rf *.o

# Object file creation rule
chall.o: chall.cpp
	$(CC) $(CFLAGS) -c chall.cpp

# Clean rule
clean:
	rm -f $(OUTPUT)

.PHONY: clean